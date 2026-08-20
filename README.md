# 王阿姨工作日历 · 共享记录表（公网部署版）

多人共享 + 密码保护（密码：`260416`）的在线记录表。
任何人、任何地点，打开网址并输入密码即可查看；谁改了内容，其他人几秒内自动同步。

## 本地运行（开发/自测）

```bash
pip install -r requirements.txt
python app.py            # 默认 http://127.0.0.1:3000
# 或生产模式：
gunicorn --bind 0.0.0.0:3000 app:app
```

打开浏览器 → 输入密码 `260416` 进入。

## 部署到公网（免费，Render）

> 数据会随部署包一起上传（server_data.json 已包含初始 184 天 / 6 期数据），
> 部署后所有修改保存在服务器磁盘，家人实时共享。

1. 注册 GitHub 账号（免费）：https://github.com
2. 新建仓库（New repository），仓库名随意（如 `ayi-calendar`），**选 Public 或 Private 均可**
3. 把本文件夹全部内容（app.py / server_data.json / web/ / requirements.txt / Procfile / render.yaml）上传到该仓库
   - 方式 A：GitHub 网页 → 仓库里点 "Add file" → "Upload files" 直接拖拽
   - 方式 B：本地 `git push`（见文末）
4. 注册 Render 账号（免费，可用 GitHub 登录）：https://render.com
5. 右上角 "New" → "Blueprint" → 连接你的 GitHub 仓库 → 选中 `ayi-calendar` → "Apply"
6. 等待约 1–2 分钟构建完成，Render 会给出一个形如 `https://ayicalendar.onrender.com` 的公网网址
7. 把这个网址发给家人，输入密码 `260416` 即可使用

### 本地 git 推送方式（可选，替代步骤 3 网页上传）

```bash
cd deploy_cloud
git init && git add -A && git commit -m "init"
git branch -M main
git remote add origin https://github.com/<你的用户名>/ayi-calendar.git
git push -u origin main
```

## 部署到公网（免费，PythonAnywhere · 无需信用卡）⭐推荐

> 优点：**完全不需要信用卡**、免费、且**硬盘持久化**——家人改的数据不会因重启/休眠丢失。
> 缺点：比 Render 多三四步鼠标操作（但都给你做成复制粘贴了）。

1. 注册 PythonAnywhere 免费账号（**不用绑卡**）：https://www.pythonanywhere.com
2. 登录后，点顶部 **Bash** 打开控制台，粘贴执行下面这一整段（自动装好环境）：
   ```bash
   curl -sL https://raw.githubusercontent.com/zhuzhu866/ayi-calendar/main/setup_pa.sh | bash
   ```
3. 执行完后，点顶部 **Web** → **Add a new web app** → 一路 Next 选 **Manual configuration** → Python 版本选 **3.11** → 创建。
4. 在刚创建的 Web app 页面里：
   - **Source code**：填 `/home/<你的用户名>/ayi-calendar`
   - **Virtualenv**：填 `/home/<你的用户名>/ayi-calendar/venv`
   - 点 **WSGI configuration file** 那个链接，把文件内容**整段替换**为仓库里的 `wsgi.py` 内容（也就是 `from app import app as application` 那段），Save。
5. 回到 Web app 页面，点 **Reload**，等几秒。
6. 访问 `https://<你的用户名>.pythonanywhere.com`，输入密码 **260416** 即可使用，转发给家人。

> 提示：PythonAnywhere 免费版域名为 `*.pythonanywhere.com`，自带 HTTPS，密码传输是加密的。

## 重要说明

- **密码 260416 在服务端校验**：不输或输错 → 接口直接拒绝（401），页面只显示密码框。
- **数据保存位置**：服务器上的 `server_data.json`。
  - 在 **PythonAnywhere** 上：磁盘**持久化**，改了长期保留，无需频繁备份。
  - 在 **Render** 免费版上：磁盘会在「重新部署」时重置为初始数据；日常访问/休眠唤醒不会丢。建议定期用页面内「导出 Excel」备份改动。
- **改密码**：编辑 `app.py` 里的 `PASSWORD = "260416"` 后重新部署即可。
- **换数据**：用页面内导出 Excel 拿到最新数据；要改初始数据，编辑 `server_data.json` 后重新部署。

## 目录结构

```
app.py              后端（Flask + 密码校验 + 共享存储）
server_data.json    共享数据（184 天 / 6 期，初始值）
web/index.html      前端（日历/列表双视图、可编辑、4 秒自动同步）
wsgi.py             PythonAnywhere 部署入口
setup_pa.sh         PythonAnywhere 一键安装脚本
requirements.txt    依赖
Procfile            gunicorn 启动命令
render.yaml         Render 一键部署蓝图
```
