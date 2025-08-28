import os
import shutil
import subprocess
import sys
import argparse
import json
import locale
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

# --- Initial Setup ---
console = Console()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = {
    "1": "fastapi",
    "2": "flask",
    "3": "django",
    "4": "cli",
}

# --- Language and Translations ---

def get_language():
    """Detects the system language."""
    try:
        lang, _ = locale.getdefaultlocale()
        return lang.split('_')[0] if lang else 'en'
    except Exception:
        return 'en'

def load_translations(lang):
    """Loads translations from the JSON file."""
    try:
        with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
            all_translations = json.load(f)
        return all_translations.get(lang, all_translations['en'])
    except FileNotFoundError:
        console.print("[bold red]Error: translations.json not found.[/bold red]")
        sys.exit(1)
    except json.JSONDecodeError:
        console.print("[bold red]Error: Could not decode translations.json.[/bold red]")
        sys.exit(1)

LANG = get_language()
t = load_translations(LANG)

# --- UI Functions ---

def print_welcome():
    """Displays the welcome message."""
    console.print(Panel(
        Text(t["welcome"], justify="center", style="bold green"),
        border_style="bold blue"
    ))
    console.print()

def ask_project_name():
    """Asks for the project name."""
    return Prompt.ask(f"[bold yellow]{t['ask_project_name']}[/bold yellow]", default=t["default_project_name"])

def ask_project_type():
    """Asks for the project type to be generated."""
    options = "\n".join([f"  [cyan]{key}[/cyan] - {value}" for key, value in TEMPLATES.items()])
    console.print(Panel(f"[bold]{t['choose_template']}[/bold]\n{options}", title=t["available_templates"], border_style="blue"))
    choice = Prompt.ask(f"[bold yellow]{t['prompt_template_number']}[/bold yellow]", choices=TEMPLATES.keys(), show_choices=False)
    return TEMPLATES[choice]

# --- Core Functions ---

def replace_in_file(file_path, old_str, new_str):
    """Replaces a string in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(old_str, new_str)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except UnicodeDecodeError:
        console.print(f"[dim]{t['cannot_process_file'].format(file_path=file_path)}[/dim]")

def scaffold_project(name, template, venv, git, docker):
    """Main function that creates the project structure."""
    console.print(Panel(t["creating_project"].format(name=name, template=template), title=f"[bold green]{t['status']}[/bold green]"))

    # 1. Copy template
    source_dir = os.path.join(TEMPLATES_DIR, template)
    dest_dir = os.path.join(os.getcwd(), name)

    if os.path.exists(dest_dir):
        console.print(f"[bold red]{t['error_dir_exists'].format(name=name)}[/bold red]")
        sys.exit(1)

    console.print(f"  - {t['copying_template_files'].format(template=template)}")
    shutil.copytree(source_dir, dest_dir)

    # 2. Replace placeholders
    console.print(f"  - {t['configuring_project_name'].format(name=name)}")
    for root, dirs, files in os.walk(dest_dir):
        # Rename Django's special directory
        if "PROJECT_NAME" in dirs:
            os.rename(os.path.join(root, "PROJECT_NAME"), os.path.join(root, name))

        for file in files:
            replace_in_file(os.path.join(root, file), "PROJECT_NAME", name)

    # 3. Create README
    readme_content = t["readme_content"].format(name=name, template=template)
    with open(os.path.join(dest_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)

    # 4. Docker
    if docker:
        console.print(f"  - {t['adding_docker']}")
        dockerfile = f"""
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"] 
"""
        docker_compose = f"""
version: '3.8'
services:
  web:
    build: .
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - .:/app
    ports:
      - \"8000:8000\"
    environment:
      - PROJECT_NAME={name}
"""
        with open(os.path.join(dest_dir, "Dockerfile"), 'w') as f:
            f.write(dockerfile)
        with open(os.path.join(dest_dir, "docker-compose.yml"), 'w') as f:
            f.write(docker_compose)
        readme_content += t["docker_readme"]


    # 5. Virtualenv
    if venv:
        console.print(f"  - {t['creating_venv']}")
        venv_path = os.path.join(dest_dir, ".venv")
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True, capture_output=True)
        
        pip_executable = os.path.join(venv_path, "bin", "pip")
        req_path = os.path.join(dest_dir, "requirements.txt")
        
        if os.path.exists(req_path):
            console.print(f"  - {t['installing_deps']}")
            subprocess.run([pip_executable, "install", "-r", req_path], check=True, capture_output=True)
        
        readme_content += t["local_setup_readme"]

    # 6. Git
    if git:
        console.print(f"  - {t['initializing_git']}")
        gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
virtual/
ENV/
env.bak/
virtual.bak/

# IDEs
.idea/
.vscode/
"""
        with open(os.path.join(dest_dir, ".gitignore"), 'w') as f:
            f.write(gitignore_content)
        
        subprocess.run(["git", "init"], cwd=dest_dir, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=dest_dir, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", t["git_initial_commit"]], cwd=dest_dir, check=True, capture_output=True)

    # Update final README
    with open(os.path.join(dest_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)

    console.print(Panel(
        t["project_created_successfully"].format(name=name),
        title=f"[bold green]{t['finished']}[/bold green]",
        border_style="green"
    ))


def main():
    """CLI entry function."""
    parser = argparse.ArgumentParser(description=t["cli_description"])
    parser.add_argument("--name", help=t["cli_name_help"])
    parser.add_argument("--template", choices=TEMPLATES.values(), help=t["cli_template_help"])
    parser.add_argument("--venv", action="store_true", help=t["cli_venv_help"])
    parser.add_argument("--git", action="store_true", help=t["cli_git_help"])
    parser.add_argument("--docker", action="store_true", help=t["cli_docker_help"])

    args = parser.parse_args()

    if args.name and args.template:
        # Direct argument mode
        scaffold_project(args.name, args.template, args.venv, args.git, args.docker)
    else:
        # Interactive mode
        print_welcome()
        project_name = ask_project_name()
        project_type = ask_project_type()
        use_venv = Confirm.ask(f"[bold yellow]{t['ask_create_venv']}[/bold yellow]", default=True)
        use_git = Confirm.ask(f"[bold yellow]{t['ask_init_git']}[/bold yellow]", default=True)
        use_docker = Confirm.ask(f"[bold yellow]{t['ask_add_docker']}[/bold yellow]", default=False)
        
        scaffold_project(project_name, project_type, use_venv, use_git, use_docker)


if __name__ == "__main__":
    main()