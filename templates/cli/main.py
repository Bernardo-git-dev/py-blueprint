# main.py
import argparse
import os
from commands import greet, health

def main():
    """Função principal da CLI."""
    parser = argparse.ArgumentParser(
        prog="PROJECT_NAME",
        description="Uma CLI de exemplo gerada pelo PyGen.",
        epilog="Aproveite a sua nova CLI!"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis')
    
    # Add greet command
    greet_parser = subparsers.add_parser('greet', help='Sauda um usuário')
    greet_parser.add_argument("name", nargs='?', default=os.getenv("USER", "Usuário"), help="Nome para saudar")
    greet_parser.add_argument("-v", "--verbose", action="store_true", help="Ativa modo verboso")
    
    # Add health command
    health_parser = subparsers.add_parser('health', help='Verifica a saúde do sistema')
    health_parser.add_argument("-v", "--verbose", action="store_true", help="Ativa modo verboso")
    
    args = parser.parse_args()
    
    if args.command == 'greet':
        greet.execute(args.name, args.verbose)
    elif args.command == 'health':
        health.execute(args.verbose)
    else:
        # Default behavior - greet with system username
        username = os.getenv("USER", "Usuário")
        print(f"Olá, {username}! Use --help para ver os comandos disponíveis.")

if __name__ == "__main__":
    main()