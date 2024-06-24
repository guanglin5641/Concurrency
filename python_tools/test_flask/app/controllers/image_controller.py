import os
import random
import string
from flask import Blueprint, request, jsonify, current_app, send_file
from werkzeug.utils import secure_filename

image_bp = Blueprint('image', __name__)

def allowed_file(filename):
    """
    检查文件名是否包含后缀，并且后缀是否在允许的扩展名列表中。

    这个函数用于验证上传的文件是否符合规定的文件类型。
    它通过检查文件名中是否包含点字符（.）来确定是否有后缀名，
    然后将后缀名与应用配置中定义的允许的文件扩展名列表进行比较。

    参数:
    filename (str): 待检查的文件名。

    返回:
    bool: 如果文件名包含在允许的扩展名列表中，则返回True，否则返回False。
    """
    # 检查文件名中是否包含点字符，以确定是否有后缀名
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
def generate_random_filename():
    """
    生成一个随机的文件名。

    该函数用于创建一个由小写字母组成的长度为10的随机字符串，用作文件名。
    这样生成的文件名在大多数情况下是唯一的，除非在极罕见的情况下发生重复。

    Returns:
        str: 一个长度为10的随机字符串，用作文件名。
    """
    # 定义可用字符集，这里使用了所有小写字母
    letters = string.ascii_lowercase
    # 生成一个长度为10的随机字符串
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@image_bp.route('/upload', methods=['POST'])
def upload_file():
    """
    处理图像上传的请求。

    该函数检查上传的文件是否符合要求（存在、有文件名、文件类型允许），
    然后为文件生成一个随机的文件名，保存到指定的上传目录，并返回文件的URL。

    :return: 根据上传结果返回不同的JSON响应，包括错误信息或上传成功的文件URL。
    """
    # 检查请求中是否存在文件部分
    if 'file' not in request.files:
        return jsonify({'error': '没有文件部分'}), 400

    # 获取上传的文件对象
    uploaded_file = request.files['file']

    # 检查文件名是否为空
    if uploaded_file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400

    # 检查文件类型是否允许
    if uploaded_file and allowed_file(uploaded_file.filename):
        # 生成安全的文件名
        filename = secure_filename(uploaded_file.filename)
        # 生成随机文件名，并保留原始文件扩展名
        random_filename = generate_random_filename() + os.path.splitext(filename)[1]

        # 获取上传目录路径
        # 确认上传目录存在
        upload_folder = current_app.config['UPLOAD_FOLDER']
        # 如果目录不存在，则创建
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # 拼接文件的完整路径并保存文件
        filepath = os.path.join(upload_folder, random_filename)
        uploaded_file.save(filepath)

        # 构造文件的URL
        file_url = request.host_url + 'uploads/' + random_filename
        # 返回上传成功的消息和文件URL
        return jsonify({'message': '文件上传成功', 'url': file_url}), 200
    else:
        # 返回文件类型不允许的错误消息
        return jsonify({'error': '文件类型不允许'}), 400


@image_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    处理上传文件的请求。

    该函数路由到上传文件的URL，并返回指定文件。此功能确保用户可以通过浏览器访问上传的图像文件。

    参数:
    - filename: 上传文件的名称，由URL路径传递。

    返回:
    - send_file返回值: 一个响应对象，它将触发浏览器下载指定的文件。
    """
    # 根据上传文件的配置信息，构造文件的完整路径
    return send_file(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

