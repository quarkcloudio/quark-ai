from flask import Blueprint,request
from ai.ocr.ocr import OCR

# 创建蓝图ocr_bp
ocr_bp = Blueprint('ocr', __name__)

# 定义路由
@ocr_bp.route('/api/ocr', methods=['GET', 'POST'])
def ocr():
    url = request.args.get('url', '')
    if url == '':
        return 'url is empty'

    return OCR.get_image_text(url)