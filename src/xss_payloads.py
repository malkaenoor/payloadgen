class XSSGenerator:
    def __init__(self):
        self.payloads = {}

        for i in range(1, 31):
            self.payloads[f"xss_test_{i}"] = f"<XSS_PAYLOAD_{i}>"

    def list_ids(self):
        return self.payloads.keys()

    def generate(self, payload_id):
        return self.payloads.get(payload_id)
