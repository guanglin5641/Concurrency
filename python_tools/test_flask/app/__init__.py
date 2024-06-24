from flask import Flask
from app.controllers.ware_controller import ware_bp
from app.controllers.shenquan_controller import shenqun_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.register_blueprint(ware_bp)
    app.register_blueprint(shenqun_bp)
    return app
