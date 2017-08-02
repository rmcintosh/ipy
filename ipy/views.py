from ipy import app
from flask import request, jsonify
from flask_limiter.util import get_remote_address


@app.route('/', methods=['GET'])
def get_ip():
    output = request.args.get('output', None)
    ip = get_remote_address()
    if output == 'json':
        ip = jsonify(ip=ip)
    return ip
