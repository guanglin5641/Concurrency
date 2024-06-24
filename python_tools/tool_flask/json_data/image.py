import os
from flask_sqlalchemy import SQLAlchemy
# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir , 'uploads.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 配置上传文件夹和允许的文件扩展名
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = { 'png' , 'jpg' , 'jpeg' , 'gif' }

if not os.path.exists(app.config['UPLOAD_FOLDER']) :
    os.makedirs(app.config['UPLOAD_FOLDER'])


# 数据库模型
class Image(db.Model) :
    id = db.Column(db.Integer , primary_key=True)
    filename = db.Column(db.String(128) , unique=True , nullable=False)
    encrypted_filename = db.Column(db.String(128) , unique=True , nullable=False)  # 加密后的文件名
    file_id = db.Column(db.String(64) , unique=True , nullable=False)  # 加密后的文件ID

    def __repr__(self) :
        return f'<Image {self.filename}>'


# 在应用上下文中创建所有数据库表
with app.app_context() :
    db.create_all()


def allowed_file(filename) :
    return '.' in filename and \
        filename.rsplit('.' , 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']