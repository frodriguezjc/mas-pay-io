"""Initialize Flask app."""



from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize and config DB
    assets = Environment()
    assets.init_app(app)
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .assets import compile_static_assets
        from .home import home
        from .products import products
        from .profile import profile
        
        #Get models to be used by SqlAlchemy
        from .models import Employee

        db.create_all()  # Create sql tables for our data models

        # Register Blueprints
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        # Compile static assets
        compile_static_assets(assets)

        return app
