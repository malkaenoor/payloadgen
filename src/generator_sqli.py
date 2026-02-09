import json
import os

class SQLiGenerator:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, "sqli_templates.json")

        with open(path, "r") as f:
            self.payloads = json.load(f)

    def list_ids(self):
        return [item["id"] for item in self.payloads]

    def generate_by_number(self, number):
        pid = f"SQLI_{number}"
        for item in self.payloads:
            if item["id"] == pid:
                return item["payload"]
        return None
