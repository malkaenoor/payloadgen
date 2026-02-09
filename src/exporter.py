import json

class Exporter:

    def to_txt(self, payloads, outfile):
        with open(outfile, "w") as f:
            for p in payloads:
                f.write(p + "\n")

    def to_json(self, payloads, outfile):
        with open(outfile, "w") as f:
            json.dump(payloads, f, indent=2)
