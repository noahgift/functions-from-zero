from mylib.bot import scrape

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")
