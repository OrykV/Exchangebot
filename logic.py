import requests
from bs4 import BeautifulSoup
counter = 0

# Functions, which get tickers from exchanges and format them
def gvrl_get_tickers():
    page_content = requests.get('https://goverla.ua/').content
    soup = BeautifulSoup(page_content,'html.parser')

    usd_bid_locator = soup.find(id="usd").contents[3]
    for child in usd_bid_locator.children:
        usd_bid = child
        gvrl_usd_bid = format(float(usd_bid[10:12] + '.' + usd_bid[12:14]), '.2f')
    usd_ask_locator = soup.find(id="usd").contents[5]
    for child in usd_ask_locator.children:
        usd_ask = child
        gvrl_usd_ask = format(float(usd_ask[10:12] + '.' + usd_ask[12:14]), '.2f')

    eur_bid_locator = soup.find(id="eur").contents[3]
    for child in eur_bid_locator.children:
        eur_bid = child
        gvrl_eur_bid = format(float(eur_bid[10:12] + '.' + eur_bid[12:14]))
    eur_ask_locator = soup.find(id="eur").contents[5]
    for child in eur_ask_locator.children:
        eur_ask = child
        gvrl_eur_ask = format(float(eur_ask[10:12] + '.' + eur_ask[12:14]), '.2f')

    pln_bid_locator = soup.find(id="pln").contents[3]
    for child in pln_bid_locator.children:
        pln_bid = child
        gvrl_pln_bid = format(float(pln_bid[10:11] + '.' + pln_bid[11:12]), '.2f')
    pln_ask_locator = soup.find(id="pln").contents[5]
    for child in pln_ask_locator.children:
        pln_ask = child
        gvrl_pln_ask = format(float(pln_ask[10:11] + '.' + pln_ask[11:12]), '.2f')

    return(gvrl_usd_bid, gvrl_usd_ask, gvrl_eur_bid, gvrl_eur_ask, gvrl_pln_bid, gvrl_pln_ask)


def niko_get_tickers():
    page_content = requests.get('https://niko-lutsk.com.ua/').content
    soup = BeautifulSoup(page_content,'html.parser')
    selector = 'div.pay'
    selector2 = 'div.bye'

    usd_bid = format(float(soup.select(selector)[0].contents[0]), '.2f')
    usd_ask = format(float(soup.select(selector2)[0].contents[0]), '.2f')

    eur_bid = format(float(soup.select(selector)[1].contents[0]), '.2f')
    eur_ask = format(float(soup.select(selector2)[1].contents[0]), '.2f')

    pln_bid = format(float(soup.select(selector)[5].contents[0]), '.2f')
    pln_ask = format(float(soup.select(selector2)[5].contents[0]), '.2f')

    return (usd_bid, usd_ask, eur_bid, eur_ask, pln_bid, pln_ask)


def west_get_tickers():
    page_content = requests.get('https://westfinance.ub.ua/').content
    soup = BeautifulSoup(page_content, 'html.parser')
    selector = 'div.packet-rowset p'
    selector = soup.select(selector)

    usd_bid = format(float(selector[4].contents[0]), '.2f')
    usd_ask = format(float(selector[5].contents[0]), '.2f')

    eur_bid = format(float(selector[7].contents[0]), '.2f')
    eur_ask = format(float(selector[8].contents[0]), '.2f')

    pln_bid = format(float(selector[10].contents[0]), '.2f')
    pln_ask = format(float(selector[11].contents[0]), '.2f')

    return (usd_bid, usd_ask, eur_bid, eur_ask, pln_bid, pln_ask)


gvrl_result = gvrl_get_tickers()
west_result = west_get_tickers()
niko_result = niko_get_tickers()

# compares bid prices and shows the best bid proposition
def bid_compare(i):
    if gvrl_result[i] < west_result[i] and niko_result[i] < west_result[i]:
        result = f'West Finance: {west_result[i]}.'
    elif west_result[i] < gvrl_result[i] and niko_result[i] < gvrl_result[i]:
        result = f'Goverla: {gvrl_result[i]}.'
    elif west_result[i] < niko_result[i] and gvrl_result[i] < niko_result[i]:
        result = f'Niko Lutsk: {niko_result[i]}.'
    elif west_result[i] == niko_result[i] > gvrl_result[i]:
        result = f'West Finance: {west_result[i]}.\n Niko Lutsk: {niko_result[i]}'
    elif west_result[i] == gvrl_result[i] > niko_result[i]:
        result = f'West Finance: {west_result[i]}.\n Goverla: {gvrl_result[i]}'
    elif niko_result[i] == gvrl_result[i] > west_result[i]:
        result = f'Niko Lutsk: {niko_result[i]}.\n Goverla: {gvrl_result[i]}'
    return result

# compares ask prices and shows the best ask proposition
def ask_compare(i):
    if gvrl_result[i] > west_result[i] and niko_result[i] > west_result[i]:
        result = f'West finance: {west_result[i]}.'
    elif west_result[i] > gvrl_result[i] and niko_result[i] > gvrl_result[i]:
        result = f'Goverla: {gvrl_result[i]}.'
    elif west_result[i] > niko_result[i] and gvrl_result[i] > niko_result[i]:
        result = f'Niko Lutsk: {niko_result[i]}.'
    elif west_result[i] == niko_result[i] < gvrl_result[i]:
        result = f'West Finance: {west_result[i]}.\n Niko Lutsk: {niko_result[i]}'
    elif west_result[i] == gvrl_result[i] < niko_result[i]:
        result = f'West Finance: {west_result[i]}.\n Goverla: {gvrl_result[i]}'
    elif niko_result[i] == gvrl_result[i] < west_result[i]:
        result = f'Niko Lutsk: {niko_result[i]}.\n Goverla: {gvrl_result[i]}'
    return result

# updates all tickers. Counts all requests and write result to the file count.txt
def startf():
    west_get_tickers()
    niko_get_tickers()
    gvrl_get_tickers()
    with open('count.txt', 'w') as file:
        global counter
        counter += 1
        file.write(f'{counter} - requests done!')






