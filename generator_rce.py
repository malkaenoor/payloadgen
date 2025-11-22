class RCEGenerator:
    def __init__(self, payload):
        self.payload = payload

    def generate(self):
        return f"[SAFE-RCE] {self.payload}"
