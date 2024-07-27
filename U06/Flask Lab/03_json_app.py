from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Please use /api/receive_json to POST data!'

@app.route('/api/receive_json', methods=['POST'])
def receive_json():
    try:
        json_data = request.get_json()
        if json_data:
            issue_list = automation(json_data)
            return jsonify({'result': issue_list}), 201
        else:
            return jsonify({"error": "Invalid JSON data"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def automation(json_data):
    try:
        issue_port = []
        if 'if_list' in json_data:
            if_list = json_data['if_list']
            for if_info in if_list:
                if if_info['if_status'] != 'UP':
                    issue_port.append(if_info['if_name'])
        return issue_port
    except:
        return ['error']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
