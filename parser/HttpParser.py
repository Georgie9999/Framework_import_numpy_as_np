import re


class HTTPParser:
    def __init__(self, raw):
        self.raw = raw
        self.parsed_data = {}
        self.parse_request()

    def parse_request(self):
        lines = self.raw.splitlines()

        match = re.match(r'(\w+) (\S+) (\S+)', lines[0])
        if match:
            method, path, version = match.groups()
            self.parsed_data['method'] = method
            self.parsed_data['path'] = path
            self.parsed_data['version'] = version

            headers = {}
            for line in lines[1:]:
                if not line:
                    break
                key, value = re.split(r':\s*', line, 1)
                headers[key] = value
            self.parsed_data['headers'] = headers

            if '' in lines:
                body_start = lines.index('')
                body = '\r\n'.join(lines[body_start + 1:])
                self.parsed_data['body'] = body
            else:
                self.parsed_data['body'] = ''

    def get_parsed_data(self):
        return self.parsed_data


if __name__ == "__main__":
    raw = """GET /example HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0

Hello, this is the request body."""
    parser = HTTPParser(raw)
    parsed_data = parser.get_parsed_data()
    print(parsed_data)
