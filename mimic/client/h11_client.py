# import json
# import requests
#
#
# def execute(host, port, func_name, params):
#     result = requests.post(
#         f"https://{host}:{port}/rpc/{func_name}",
#         headers={'Content-Type': 'application/json'},
#         data=json.dumps(params),
#         verify=False
#     )
#     return result
#
#
# if __name__ == "__main__":
#     response = execute("127.0.0.1", "50000", "biz_6", {"a": 123, "b": "shit", "c": [1, 1, 0]})
#     print(response.status_code)
#     print(response.headers)
#     print(response.text)
