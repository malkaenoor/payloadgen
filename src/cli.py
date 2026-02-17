import click

from generator_xss import XSSGenerator
from generator_sqli import SQLiGenerator
from encoder import Encoder
from mutate import Mutator
from mutate_sqli import SQLiMutator
from exporter import Exporter

@click.group()
def cli():
    """Payload Generator CLI"""
    pass


# --------------------------------------------------
# LIST PAYLOAD IDS
# --------------------------------------------------
@cli.command()
@click.option("--type", required=True, type=click.Choice(["xss", "sqli"]))
def list(type):
    if type == "xss":
        g = XSSGenerator()
        click.echo("\nAvailable XSS Payloads:")
        for pid in g.list_ids():
            click.echo(f" - {pid}")

    elif type == "sqli":
        g = SQLiGenerator()
        click.echo("\nAvailable SQLi Payloads:")
        for pid in g.list_ids():
            click.echo(f" - {pid}")


# --------------------------------------------------
# GENERATE PAYLOAD (XSS: 1–20)
# --------------------------------------------------
@cli.command()
@click.option("--type", required=True, type=click.Choice(["xss", "sqli"]))
@click.option("--id", type=str, required=True)
def generate(type, id):
    if type == "xss":
        g = XSSGenerator()
        payload = g.generate_by_number(id)

    elif type == "sqli":
        g = SQLiGenerator()
        payload = g.generate_by_number(id)

    if payload:
        click.echo("\nGenerated Payload:\n")
        click.echo(payload)
    else:
        click.echo("Invalid ID. Please choose a valid number.")


# --------------------------------------------------
# ENCODER
# --------------------------------------------------
@cli.command()
@click.option(
    "--method",
    required=True,
    type=click.Choice(["base64", "url", "html", "hex", "reverse", "wrap"]),
)
@click.option("--payload", required=True)
def encode(method, payload):
    e = Encoder()

    if method == "base64":
        out = e.base64_encode(payload)
    elif method == "url":
        out = e.url_encode(payload)
    elif method == "html":
        out = e.html_encode(payload)
    elif method == "hex":
        out = e.hex_encode(payload)
    elif method == "reverse":
        out = e.reverse(payload)
    elif method == "wrap":
        out = e.wrap(payload, "<<WRAP>>[[VALUE]]<<END>>")

    click.echo("\nEncoded Payload:\n")
    click.echo(out)


# --------------------------------------------------
# MUTATION GROUP
# --------------------------------------------------
@cli.group()
def mutate():
    """Mutate payloads"""
    pass


@mutate.command()
@click.option(
    "--method",
    required=True,
    type=click.Choice(["case-flip", "reverse", "shuffle", "inject-null"]),
)
@click.option("--payload", required=True)
def run(method, payload):
    m = Mutator()

    if method == "case-flip":
        out = m.case_flip(payload)
    elif method == "reverse":
        out = m.reverse(payload)
    elif method == "shuffle":
        out = m.shuffle(payload)
    elif method == "inject-null":
        out = m.inject_null(payload)

    click.echo("\nMutated Payload:\n")
    click.echo(out)

# --------------------------------------
# SQLI MUTATION
# --------------------------------------
@cli.command()
@click.option("--type", required=True)
@click.option("--method", required=True,
              type=click.Choice([
                  "case-flip",
                  "comment",
                  "keyword-split",
                  "null",
                  "random"
              ]))
@click.option("--payload", required=True)
def mutate_sqli(type, method, payload):

    if type != "sqli":
        click.echo("Only SQLi supported here")
        return

    m = SQLiMutator()

    if method == "case-flip":
        out = m.case_flip(payload)
    elif method == "comment":
        out = m.comment_obfuscate(payload)
    elif method == "keyword-split":
        out = m.keyword_split(payload)
    elif method == "null":
        out = m.inject_null(payload)
    elif method == "random":
        out = m.random_mix(payload)

    click.echo("\nMutated SQLi Payload:\n")
    click.echo(out)
#______________________________________________
#  Export support
#_____________________________________________
@cli.command()
@click.option("--type", required=True)
@click.option("--export", type=click.Choice(["txt", "json"]))
@click.option("--out", required=True)
def export(type, export, out):

    if type == "xss":
        g = XSSGenerator()
    elif type == "sqli":
        g = SQLiGenerator()
    else:
        click.echo("Invalid type")
        return

    payloads = g.get_all_payloads()
    e = Exporter()

    if export == "txt":
        e.to_txt(payloads, out)
    elif export == "json":
        e.to_json(payloads, out)

    click.echo(f"\nPayloads exported to {out}")

if __name__ == "__main__":
    cli()
