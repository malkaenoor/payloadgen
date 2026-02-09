import random

class SQLiMutator:

    def case_flip(self, payload):
        return "".join(
            c.upper() if random.choice([True, False]) else c.lower()
            for c in payload
        )

    def comment_obfuscate(self, payload):
        return payload.replace(" ", "/**/")

    def keyword_split(self, payload):
        keywords = ["SELECT", "UNION", "WHERE", "AND", "OR"]
        out = payload
        for kw in keywords:
            out = out.replace(
                kw,
                kw[0] + "/**/" + kw[1:]
            )
        return out

    def inject_null(self, payload):
        return payload.replace("'", "'%00")

    def random_mix(self, payload):
        methods = [
            self.case_flip,
            self.comment_obfuscate,
            self.keyword_split,
            self.inject_null
        ]
        return random.choice(methods)(payload)
