class SSTIGenerator:
    def __init__(self, payload):
        self.payload = payload

    def generate(self):
        return f"[SAFE-SSTI] {self.payload}"
