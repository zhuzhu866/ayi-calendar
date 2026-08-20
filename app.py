import json, os, datetime
from flask import Flask, request, send_from_directory, jsonify

BASE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(BASE, "web")
STORE = os.path.join(BASE, "server_data.json")
PASSWORD = "260416"

app = Flask(__name__, static_folder=None)


def load_data():
    """读取共享数据；若文件缺失则回退到最小化默认结构，避免崩溃。"""
    if not os.path.exists(STORE):
        default = {
            "meta": {"total": 0, "work": 0, "rest": 0, "legal": 0,
                     "period_start": "", "period_end": "", "month_count": 0},
            "months": {}, "records": [], "periods": [],
            "updatedAt": datetime.datetime.now().isoformat(),
        }
        save_data(default)
        return default
    return json.load(open(STORE, encoding="utf-8"))


def save_data(data):
    data["updatedAt"] = datetime.datetime.now().isoformat()
    tmp = STORE + ".tmp"
    json.dump(data, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    os.replace(tmp, STORE)  # 原子写，避免并发写损坏文件


def check_pw():
    return request.headers.get("X-Password") == PASSWORD


@app.route("/")
def index():
    return send_from_directory(WEB, "index.html")


@app.route("/api/data", methods=["GET"])
def get_data():
    if not check_pw():
        return jsonify({"error": "unauthorized"}), 401
    return jsonify(load_data())


@app.route("/api/data", methods=["POST"])
def post_data():
    if not check_pw():
        return jsonify({"error": "unauthorized"}), 401
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict) or "records" not in data or "periods" not in data:
        return jsonify({"error": "bad data"}), 400
    save_data(data)
    return jsonify({"ok": True, "updatedAt": data["updatedAt"]})


@app.route("/api/health")
def health():
    return jsonify({"ok": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
