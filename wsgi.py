import sys, os

# PythonAnywhere 部署用 WSGI 入口
# vendor/ 里已内置 flask 等依赖（纯 Python，无需在 PA 上 pip install）
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
sys.path.insert(0, HERE)

from app import app as application
