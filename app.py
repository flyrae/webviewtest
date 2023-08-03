from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
app = Flask(__name__, static_url_path='/webview/static',static_folder='webview/static')
CORS(app)
@app.route('/webview/')
def home():
    return render_template('index.html')

@app.route('/webview/api/v1/data', methods=['POST'])
def receive_post_request():
    data = request.form
    custom_header = dict(request.headers)

    print("Received data:", data)
    print("Custom header value:", custom_header)

    response = {
        'status': 'success',
        'message': 'Data received successfully',
        'received_data': data.to_dict(),
        'received_header':custom_header
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4399)
