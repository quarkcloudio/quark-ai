#coding: utf-8
from flask import Flask
from api.home import home_bp
from api.ocr import ocr_bp

# 创建一个app
app = Flask(__name__)

# 设置debug模式
app.config["DEBUG"] = True

# 注册蓝图
app.register_blueprint(home_bp)
app.register_blueprint(ocr_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)