class Exporter:
    def to_txt(self, payloads, out_file):
        with open(out_file, "w") as f:
            for p in payloads:
                # write only payload string
                payload_str = p.get("example_safe", "")
                f.write(payload_str + "\n")

    def to_json(self, payloads, out_file):
        import json
        with open(out_file, "w") as f:
            json.dump(payloads, f, indent=4)
