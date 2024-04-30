from flask import Blueprint

# 创建蓝图对象
home_bp = Blueprint('home', __name__)

# 创建路由
@home_bp.route('/')
def index() -> str:
    return 'Hello World!'