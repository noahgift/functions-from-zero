import click
from mylib.bot import scrape

@click.command()
@click.option('--name', help='Wikipedia word')
@click.option('--length',  help='number of sentences')
def cli(name, length):
    """
    just scraping
    """
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}", fg="red"))
    return result

if __name__=='__main__':
    cli()