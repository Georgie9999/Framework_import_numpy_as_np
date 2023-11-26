import asyncio

from http_parser import parse_http
from parser.HttpParser import HTTPParser


class BestApi:
    def __init__(self):
        self.get_dict = {}
        self.post_dict = {}
        self.put_dict = {}
        self.delete_dict = {}

        self.loop = asyncio.get_event_loop()

        self.server = self.loop.run_until_complete(
            asyncio.start_server(
                self.__route, port=1337
            )
        )

    def run(self):
        self.loop.run_forever()

    def get(self, path: str):
        def inner_get(func):
            self.get_dict[path] = func

        return inner_get

    def put(self, path: str):
        def inner_put(func):
            self.put_dict[path] = func

        return inner_put

    def post(self, path: str):
        def inner_post(func):
            self.post_dict[path] = func

        return inner_post

    def delete(self, path: str):
        def inner_delete(func):
            self.delete_dict[path] = func

        return inner_delete

    async def __route(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        request_data = b""

        print(self.get_dict)

        while True:
            data = await asyncio.wait_for(
                reader.read(1024), timeout=10
            )

            if not data:
                break

            request_data += data

            if b'\r\n\r\n' in request_data:
                break

        parser = HTTPParser(request_data.decode())
        parsed = parser.get_parsed_data()

        body = ""

        if parsed["method"] == "GET":
            body = await self.__handle_method(parsed["path"], self.get_dict)

        elif parsed["method"] == "POST":
            body = await self.__handle_method(parsed["path"], self.post_dict)

        elif parsed["method"] == "PUT":
            body = await self.__handle_method(parsed["path"], self.put_dict)

        elif parsed["method"] == "DELETE":
            body = await self.__handle_method(parsed["path"], self.delete_dict)

        response = f"HTTP/1.1 {200}\r\nContent-Length: {len(body)}\r\n\r\n{body}\r\n\r\n"
        writer.write(response.encode())

        await writer.drain()

    async def __handle_method(self, path, method_dict):
        part = path
        if "{" in path:
            part = path[0:path.find("{")]

        for key in method_dict.keys():
            if part in key:
                return await method_dict[key]()

        return "Not Found"

app = BestApi()


@app.get('/hi')
async def hi_rand_func():
    return 'hi'


@app.get('/hello')
async def rand_func():
    return 'hello'

@app.delete('/hello')
async def rand_func_2():
    return "delete hello"

app.run()
