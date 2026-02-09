class CSRFGenerator:
    def __init__(self, payload):
        self.payload = payload

    def generate(self):
        return f"[SAFE-CSRF] {self.payload}"
