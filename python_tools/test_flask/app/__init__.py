from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()


def create_app() :
    """
    创建并配置应用程序实例。

    该函数初始化一个Flask应用，配置数据库，注册蓝本，并创建数据库表。
    """
    # 初始化Flask应用实例
    app = Flask(__name__)
    # 从配置类加载应用配置
    app.config.from_object('app.config.Config')

    # 导入并注册ware控制器的蓝本
    from app.controllers.ware_controller import ware_bp
    # 导入并注册shenquan控制器的蓝本
    from app.controllers.shenquan_controller import shenqun_bp
    # 导入并注册image控制器的蓝本
    from app.controllers.image_controller import image_bp

    # 注册蓝本
    app.register_blueprint(ware_bp)
    app.register_blueprint(shenqun_bp)
    app.register_blueprint(image_bp)

    # 初始化数据库并应用到app上下文中
    db.init_app(app)

    # 在应用上下文中创建所有数据库表
    with app.app_context() :
        db.create_all()
        # 确保上传目录存在，如果不存在则创建
        # 确认上传目录存在
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder) :
            os.makedirs(upload_folder)

    # 返回配置好的应用实例
    return app

