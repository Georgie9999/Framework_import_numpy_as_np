import asyncio


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
        while True:
            data = await asyncio.wait_for(
                reader.readline(), timeout=10
            )

            response = f"HTTP/1.1 {200}\r\nContent-Length: {len('da')}\r\n\r\n{'da'}"
            writer.write(response.encode())
            # # if data is not None:
            # #     raw_response = await self.get_dict['/hello']()

app = BestApi()

@app.get('/hello')
async def rand_func():
    return 'hello'

app.run()
