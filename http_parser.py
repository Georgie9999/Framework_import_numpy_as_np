def parse_http(response):
    response_parsed = {}

    response = response.decode()

    response_list = response.split('\r\n')

    response_parsed["method"], response_parsed["url"], response_parsed["version"] = response_list[0].split(sep="/")

    _, response_parsed["host"] = response_list[1].split(": ", maxsplit=1)

    headers = {}

    for i in range(2, len(response_list) - 2):
        header, body = response_list[i].split(": ", maxsplit=1)
        headers[header] = body

    response_parsed["headers"] = headers

    response_parsed["body"] = ""
    if response_list[-2]:
        _, response_parsed["body"] = response_list[-2].split(": ")

    return response_parsed
