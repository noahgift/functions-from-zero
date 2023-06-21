import click
import wikipedia


@click.command()
@click.option('--name', default='Microsoft', help='Wikipedia word')
def scrape(name="Microsoft", length=1):
    """
    just scraping
    """
    result = wikipedia.summary(name, sentences=length)
    click.echo(click.style(f"{result}", fg="red"))
    return result

if __name__=='__main__':
    scrape()