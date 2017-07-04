from flask import Flask, request, jsonify
from flask_limiter.util import get_remote_address


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_ip():
    format = request.args.get('format', None)
    ip = get_remote_address()
    if format == 'json':
        ip = jsonify(ip=ip)
    return ip


if __name__ == '__main__':
    app.run()
