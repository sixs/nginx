# encoding: utf-8
"""
desc: 简易路由转换器
author: SixSeven
"""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/v1/<user_id>/enterprises/access-token", methods=["POST"])
def access_token(user_id):
    url = "https://api-ivm.myhuaweicloud.com" + request.path

    headers = dict(request.headers)
    del_header_keys = ["Host"]
    for header_key in del_header_keys:
        if header_key in headers:
            del headers[header_key]

    req = requests.request(request.method, url, headers=headers, data=request.get_data(), params=request.get_data(),
                           timeout=5, verify=False)
    return req.content, req.status_code


@app.route("/v1/<user_id>/messages/callback", methods=["POST, DELETE, GET"])
def access_token(user_id):
    url = "https://api-ivm.myhuaweicloud.com" + request.path

    headers = dict(request.headers)
    del_header_keys = ["Host"]
    for header_key in del_header_keys:
        if header_key in headers:
            del headers[header_key]

    req = requests.request(request.method, url, headers=headers, data=request.get_data(), params=request.get_data(),
                           timeout=5, verify=False)
    return req.content, req.status_code


def start_nginx():
    app.run("0.0.0.0", 5235, debug=True)


if __name__ == "__main__":
    start_nginx()
