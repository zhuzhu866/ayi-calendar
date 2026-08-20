import sys, os

# PythonAnywhere 部署用 WSGI 入口
# 在 PA 的 Web 面板里，把 WSGI 配置文件替换为本文件内容即可。
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app as application
