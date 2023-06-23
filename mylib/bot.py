import wikipedia

def scrape(name, length):
    result = wikipedia.summary(name, sentences=length)
    return result