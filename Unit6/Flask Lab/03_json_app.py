from flask import Flask, request, jsonify

app = Flask(__name__)

# 示例JSON数据
sample_data = {
    "name": "John Doe",
    "age": 25,
    "city": "New York"
}

# 处理接收到的JSON数据
@app.route('/api/receive_json', methods=['POST'])
def receive_json():
    try:
        # 获取JSON数据
        json_data = request.get_json()
        if json_data:
            print("Received JSON data:", json_data)
            response_data = json_data

            # 返回JSON格式的响应
            return jsonify(response_data), 200
        else:
            return jsonify({"error": "Invalid JSON data"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
