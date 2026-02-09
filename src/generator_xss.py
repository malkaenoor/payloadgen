import json

class XSSGenerator:
    def __init__(self):
        with open("xss_templates.json", "r") as f:
            self.payloads = json.load(f)

    def list_ids(self):
        return [p["id"] for p in self.payloads]

    def generate_by_id(self, pid):
        for p in self.payloads:
            if p["id"] == pid:
                return p.get("example_safe", "")
        return None

    def generate_by_number(self, num):
        if 1 <= num <= len(self.payloads):
            return self.payloads[num - 1].get("example_safe", "")
        return None

    def get_all_payloads(self):
        return self.payloads
