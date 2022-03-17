import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="Web page we want to scrape")
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", fg="blue"))


if __name__ == "__main__":
    cli()
