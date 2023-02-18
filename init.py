# encoding: utf-8
"""
desc: 简易路由转换器
author: SixSeven
"""
import json
import importlib


# 根据配置文件及模板文件生成nginx.py
def init():
    with open("config/config.json", encoding="utf-8", mode="r") as config_fp, \
            open("template/route_template.txt", encoding="utf-8", mode="r") as route_tmp_fp, \
            open("template/nginx_template.txt", encoding="utf-8", mode="r") as nginx_tmp_fp, \
            open("nginx.py", encoding="utf-8", mode="w") as nginx_fp:
        config_json = json.loads(config_fp.read())
        route_text_list = []
        rout_tmp_text = route_tmp_fp.read()
        for path, config in config_json.items():
            path = path.replace("{", "<").replace("}", ">")
            method_list = config.get("methods", [])
            param_list = config.get("params", [])
            endpoint = config.get("endpoint", "")
            route_text = rout_tmp_text.replace("{path_placeholder}", path) \
                .replace("{methods_placeholder}", ", ".join(method_list)) \
                .replace("{params_placeholder}", ", ".join(param_list)) \
                .replace("{endpoint_placeholder}", endpoint)
            route_text_list.append(route_text)

        nginx_text = nginx_tmp_fp.read()
        nginx_text = nginx_text.split("# route begin")[0] + "\n\n\n".join(route_text_list) \
                     + nginx_text.split("# route end")[1]

        nginx_fp.write(nginx_text)


# 执行nginx.py启动路由转换器
def start_nginx():
    nginx_module = importlib.import_module("nginx")
    getattr(nginx_module, "start_nginx")()


if __name__ == "__main__":
    init()
    # start_nginx()
