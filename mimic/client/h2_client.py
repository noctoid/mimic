import json
import ssl
import httpx
from asyncio import new_event_loop


def get_connection_pool():
    pass


async def execute(host, port, func, params):
    context = ssl.create_default_context()
    context.load_verify_locations(cafile="/Users/yoko/Documents/workspace/mimic_example/example_cert.pem")
    client = httpx.AsyncClient(http2=True, verify=context)
    result = await client.post(
        f"https://{host}:{port}/rpc/{func}",
        headers={'Content-Type': 'application/json'},
        json=params,
    )
    return result


if __name__ == "__main__":
    loop = new_event_loop()
    response = loop.run_until_complete(execute("127.0.0.1", "50000", "biz_6", {"a": 114514, "b": "shit", "c": [1, 1, 0]}))
    print(response.http_version)
    print(response.status_code)
    print(response.headers)
    print(response.text)
