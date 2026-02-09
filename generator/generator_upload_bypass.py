class UploadBypassGenerator:
    def __init__(self, payload):
        self.payload = payload

    def generate(self):
        return f"[SAFE-UPLOAD] {self.payload}"
