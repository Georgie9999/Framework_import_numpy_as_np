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

    line_number = 0
    response_headers = response_headers.split('\r\n')
    while response_headers[line_number]:
        header, body = response_headers[line_number].split(": ", maxsplit=1)
        headers[header] = body
        line_number += 1

    response_parsed["headers"] = headers

    line_number += 1

    body = ""
    while response_headers[line_number]:
        body += response_headers[line_number]
        line_number += 1

    response_parsed["body"] = body

    return response_parsed