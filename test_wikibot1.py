from mylib.bot import scrape
from wikibot1 import cli
from click.testing import CliRunner

def test_scrape():
    assert "Microsoft" in scrape("Microsoft",1)

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Microsoft', '--length', '1'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output