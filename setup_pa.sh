#!/bin/bash
# PythonAnywhere 一键安装脚本
# 用法：登录 PA 后，打开 "Bash" 控制台，粘贴下面这一整段并执行：
#
#   curl -sL https://raw.githubusercontent.com/zhuzhu866/ayi-calendar/main/setup_pa.sh | bash
#
# 脚本会：克隆仓库 -> 建虚拟环境 -> 安装依赖。
# 装完后请到 Web 面板完成最后两步（见 README「方案二」）。

set -e
cd ~
echo "==> 克隆仓库"
rm -rf ayi-calendar
git clone --depth 1 https://github.com/zhuzhu866/ayi-calendar.git
cd ayi-calendar

echo "==> 创建虚拟环境并安装依赖"
python3 -m venv venv
source venv/bin/activate
pip install --quiet --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ 安装完成！"
echo "接下来请在 PythonAnywhere 的 Web 面板里："
echo "  1) Source code 目录设为：/home/$USER/ayi-calendar"
echo "  2) 虚拟环境 设为：/home/$USER/ayi-calendar/venv"
echo "  3) 用本仓库 wsgi.py 的内容覆盖 WSGI 配置文件"
echo "  4) 点 Reload $USER.pythonanywhere.com"
echo "然后访问 https://$USER.pythonanywhere.com ，输入密码 260416 即可。"
