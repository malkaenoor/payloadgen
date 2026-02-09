import base64
import urllib.parse
import html

class Encoder:

    def base64_encode(self, payload):
        return base64.b64encode(payload.encode()).decode()

    def url_encode(self, payload):
        return urllib.parse.quote(payload)

    def html_encode(self, payload):
        return html.escape(payload)

    def hex_encode(self, payload):
        return payload.encode().hex()

    def reverse(self, payload):
        return payload[::-1]

    def wrap(self, payload, template):
        return template.replace("[[VALUE]]", payload)
