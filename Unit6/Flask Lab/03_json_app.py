from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/receive_json', methods=['POST'])
def receive_json():
    try:
        json_data = request.get_json()
        if json_data:
            print("Received JSON data:", json_data)
            response_data = json_data

            return jsonify(response_data), 200
        else:
            return jsonify({"error": "Invalid JSON data"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
