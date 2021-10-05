from bs4 import BeautifulSoup
import requests


def getUsername(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    username = soup.find('title')
    return username.text[1:-29]

def statChecker(url):
    url = 'https://myanimelist.net/profile/'+url
    parsedStats = [getUsername(url)]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rawStats = soup.findAll('div', attrs={"class":"di-tc al pl8 fs12 fw-b"})
    for title in rawStats:
        parsedStats.append(float(title.text[6:]))
    return parsedStats # list formatted like so: ['username', anime days (float), manga days (float)]