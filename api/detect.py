from flask import Blueprint, request, jsonify
from service.detect.detect import Detect

# 创建蓝图
detect_bp = Blueprint('detect', __name__)

# 定义路由
@detect_bp.route('/api/detect/getData', methods=['GET', 'POST'])
def get_data():
    url = request.args.get('url', '')
    if url == '':
        return 'url is empty'

    # print()
    
    return Detect.get_data(url)

# 定义路由
@detect_bp.route('/api/detect/train', methods=['GET'])
def train():
    return Detect.train()