from flask import Blueprint, request, jsonify
from service.detect import Detect

# 创建蓝图
detect_bp = Blueprint('detect', __name__)

# 定义路由
@detect_bp.route('/api/detect', methods=['GET', 'POST'])
def get_data():
    url = request.args.get('url', '')
    if url == '':
        return 'url is empty'
    
    return Detect.get_detect_data(url)