from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Import and register Blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
