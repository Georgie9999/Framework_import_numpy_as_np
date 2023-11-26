import asyncio
import re

from parser.HttpParser import HTTPParser

import templating_engine_like.template_engine as te


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

        body = await self.__handle_method(parsed["method"], parsed["path"])

        response = f"HTTP/1.1 {200}\r\nContent-Length: {len(body)}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{body}\r\n\r\n"
        writer.write(response.encode())

        await writer.drain()

    async def __handle_method(self, method, path):
        method_dict = {}

        if method == "GET":
            method_dict = self.get_dict
        elif method == "POST":
            method_dict = self.post_dict
        elif method == "PUT":
            method_dict = self.put_dict
        elif method == "DELETE":
            method_dict = self.delete_dict

        for key, handler in method_dict.items():
            if path == key:
                return await handler()
            if self.__path_matches(key, path):
                params = self.__extract_path_parameters(key, path)
                if params is not None:
                    return await handler(**params)

        return "Not Found"

    def __path_matches(self, pattern, path):
        pattern_parts = pattern.split('/')
        path_parts = path.split('/')

        if len(pattern_parts) != len(path_parts):
            return False

        for pattern_part, path_part in zip(pattern_parts, path_parts):
            if '{' in pattern_part and '}' in pattern_part:
                continue
            if pattern_part != path_part:
                return False

        return True

    def __extract_path_parameters(self, pattern, path):
        pattern_parts = pattern.split('/')
        path_parts = path.split('/')

        if len(pattern_parts) != len(path_parts):
            return None

        params = {}
        for pattern_part, path_part in zip(pattern_parts, path_parts):
            if '{' in pattern_part and '}' in pattern_part:
                param_name = pattern_part[1:-1]
                params[param_name] = path_part

        return params if params else None


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

@app.get('/user/{username}/hi/{user2}')
async def get_user(username, user2):
    return f"{username} say hi to {user2}"

@app.get('/template')
async def main():
    temp = te.TemplateEngine()

    temp.set_template_from_html('templates/first_html.html')
    temp.set_parameters(="mem", lastname="cringe")
    final = temp.get_rendered()
    print(final)
    return final

app.run()
