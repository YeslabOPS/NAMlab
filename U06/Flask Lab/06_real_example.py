from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

def convert_dot_in_path(path):
    # 将路径中的 %2E 转换为小数点 "."
    decoded_path = urllib.parse.unquote(path)
    return decoded_path.replace("%2E", ".")

def handle_request():
    path = convert_dot_in_path(request.path)
    data = request.json
    return jsonify({"path": path, "data": data})

@app.route("/", methods=["GET"])
def test():
    return "OK"

@app.route("/api/v1/configuration/users/user-roles/user-role/rest-userrole1/web/web-bookmarks/bookmark", methods=["POST"])
def handle_configuration_endpoint():
    return handle_request()

@app.route("/api/v1/totp/user-backup-code", methods=["POST"])
def handle_totp_endpoint():
    return handle_request()

@app.route("/api/v1/system/maintenance/archiving/cloud-server-test-connection", methods=["POST"])
def handle_maintenance_endpoint():
    return handle_request()

@app.route("/api/v1/license/keys-status", methods=["POST"])
def handle_license_endpoint():
    return handle_request()

@app.route("/api/v1/system/system-information", methods=["POST"])
def handle_system_information_endpoint():
    return handle_request()

@app.route("/api/v1/cav/client/status", methods=["POST"])
def handle_client_status_endpoint():
    return handle_request()

@app.route("/api/v1/cav/admin/options", methods=["POST"])
def handle_admin_options_endpoint():
    return handle_request()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)