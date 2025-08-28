# main.py
from flask import Flask, jsonify
import os

# Import routes
from routes import health, greeting

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(health.bp)
    app.register_blueprint(greeting.bp)
    
    @app.route("/")
    def index():
        username = os.getenv("USER", "Developer")
        return jsonify(message=f"Hello {username} from Flask!")
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')