def parse_http(response):
    response_parsed = {}

    response = response.decode()

    response_structure, response_headers = response.split('\r\n', maxsplit=1)

    response_parsed["method"], temp_response = response_structure.split(sep=" /", maxsplit=1)

    response_parsed["url"], temp_response = temp_response.split(' ', maxsplit=1)

    if " " in temp_response:
        response_parsed["version"], response_parsed["code"] = temp_response.split(" ", maxsplit=1)
    else:
        response_parsed["version"] = temp_response

    headers = {}

    for line in response_headers.split('\r\n'):
        if line:
            header, body = line.split(": ", maxsplit=1)
            headers[header] = body

    response_parsed["headers"] = headers

    response_parsed["body"] = ""
    if response_headers.split('\r\n')[-2]:
        _, response_parsed["body"] = response_headers[-2].split(": ")

    return response_parsed