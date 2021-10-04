from bs4 import BeautifulSoup
import requests

def statChecker(url):
    parsedStats = [url[32:].lower()]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rawStats = soup.findAll('div', attrs={"class":"di-tc al pl8 fs12 fw-b"})
    for title in rawStats:
        parsedStats.append(float(title.text[6:]))
    return parsedStats