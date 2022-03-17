import wikipedia

def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result