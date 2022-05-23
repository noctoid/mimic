from typing import Awaitable, Callable, Union, List
from importlib import import_module
from inspect import iscoroutinefunction, isfunction, getmembers
from os import walk
from functools import reduce
from operator import add

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse


class CallRegisterException(Exception):
    pass


def rpc_wrapper(func):
    try:
        assert iscoroutinefunction(func)
    except AssertionError as e:
        raise CallRegisterException(f"{func} is not an awaitable coroutine function!")

    async def execute(request):
        params = await request.json()
        return JSONResponse(await func(**params))

    return execute


def create_route_for_rpc(func) -> Route:
    api_prefix = '/rpc'
    return Route('/'.join([api_prefix, func.__name__]), rpc_wrapper(func), methods=['POST'])


def get_app(config=None, routes: List[Union[Awaitable, Callable]] = None) -> Starlette:
    """
    :param config:
        A Dict with customized config
    :param routes: 
        A list of functions to be registered as RPCs 
    :return:
        A Starlette app loaded with RPCs
    """
    sources = []
    if config is None:
        config = {}
    for (root, dir_, filenames) in walk(config.get("root", "rpc")):
        parent_module_name = ".".join(root.split("/"))
        for filename in filenames:
            if filename.endswith(".py"):
                module_name, _ = filename.split(".")
                sources.append(".".join([parent_module_name, module_name]))

    if routes is None:
        routes = reduce(add, ([i[1] for i in getmembers(import_module(source), isfunction)] for source in sources))

    return Starlette(
        debug=config,
        routes=[create_route_for_rpc(i) for i in routes]
    )


if __name__ == "__main__":
    app = get_app()
