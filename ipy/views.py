from ipy import app
from flask import request, jsonify


@app.route('/', methods=['GET'])
def get_ip():
    output = request.args.get('output', None)
    ip = request.remote_addr
    if output == 'json':
        ip = jsonify(ip=ip)
    return ip
