import os
from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import hashlib  # 导入哈希算法库

app = Flask(__name__)

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


@app.route('/upload' , methods=['POST'])
def upload_file() :
    # 检查是否有文件部分
    if 'file' not in request.files :
        return jsonify({ 'error' : 'No file part' }) , 400
    file = request.files['file']
    # 如果用户没有选择文件
    if file.filename == '' :
        return jsonify({ 'error' : 'No selected file' }) , 400
    if file and allowed_file(file.filename) :
        filename = secure_filename(file.filename)

        # 计算文件ID和加密后的文件名（使用SHA-256哈希算法）
        file_id = hashlib.sha256(filename.encode()).hexdigest()
        encrypted_filename = hashlib.sha256(filename.encode()).hexdigest()

        # 保存文件
        filepath = os.path.join(app.config['UPLOAD_FOLDER'] , filename)
        file.save(filepath)

        # 将文件路径和加密后的文件名、文件ID存储在数据库中
        new_image = Image(filename=filename , encrypted_filename=encrypted_filename , file_id=file_id)
        db.session.add(new_image)
        db.session.commit()

        file_url = request.host_url + 'uploads/' + filename
        return jsonify({ 'message' : 'File successfully uploaded' , 'url' : file_url }) , 200
    else :
        return jsonify({ 'error' : 'File type not allowed' }) , 400


if __name__ == '__main__' :
    app.run(debug=True)


