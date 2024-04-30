from flask import Blueprint
from ai.ocr.ocr import OCR

# 创建蓝图ocr_bp
ocr_bp = Blueprint('ocr', __name__)

# 定义路由
@ocr_bp.route('/api/ocr', methods=['GET', 'POST'])
def ocr():
    return OCR.getImageText()