import mechanicalsoup
import re
browser = mechanicalsoup.StatefulBrowser()
url = "https://www.investopedia.com/simulator/portfolio"
browser.open(url)
def nesto():
    response = self.fetch('/simulator/portfolio/')

    parsed_html = browser.page

    # The ids of all the account information values
    acct_val_id = "ctl00_MainPlaceHolder_currencyFilter_ctrlPortfolioDetails_PortfolioSummary_lblAccountValue"
    buying_power_id = "ctl00_MainPlaceHolder_currencyFilter_ctrlPortfolioDetails_PortfolioSummary_lblBuyingPower"
    cash_id = "ctl00_MainPlaceHolder_currencyFilter_ctrlPortfolioDetails_PortfolioSummary_lblCash"
    return_id = "ctl00_MainPlaceHolder_currencyFilter_ctrlPortfolioDetails_PortfolioSummary_lblAnnualReturn"

    # Use BeautifulSoup to extract the relevant values based on html ID tags
    account_value = parsed_html.find('span', attrs={'id': acct_val_id}).text
    buying_power = parsed_html.find('span', attrs={'id': buying_power_id}).text
    cash = parsed_html.find('span', attrs={'id': cash_id}).text
    annual_return = parsed_html.find('span', attrs={'id': return_id}).text

    # We want our returned values to be floats
    # Use regex to remove non-numerical or decimal characters
    # But keep - (negative sign)
    regexp = "[^0-9.-]"
    account_value = float(re.sub(regexp, '', account_value))
    buying_power = float(re.sub(regexp, '', buying_power))
    cash = float(re.sub(regexp, '', cash))
    annual_return = float(re.sub(regexp, '', annual_return))

acct_val_id = "ctl00_MainPlaceHolder_currencyFilter_ctrlPortfolioDetails_PortfolioSummary_lblAccountValue"

print(browser.page)
from investopedia_trading_api.InvestopediaApi import ita 

#portfollio =  ita.Account()
#status = portfollio.get_current_securities()


'''
from InvestopediaApi import ita

client = ita.Account("rroge036@gmail.com", "https://khm3zlce.r.us-east-1.awstrack.me/L0/https:%2F%2Fauth.investopedia.com%2Frealms%2Finvestopedia%2Flogin-actions%2Fauthenticate%3Fexecution=fe337119-f07c-4b7b-8123-e6abd20d841e%26client_id=finance-simulator%26tab_id=NtNhrPHroPY%26emailCode=89596/1/01000196dca63664-563a20fa-43ff-4f46-b7ad-96c5e1484896-000000/vySPjFuMdAw7hz6ydv78IzgbL5o=426")

portfolio = client.get_current_securities()

# Portfolio is not a list, it is a namedtuple object with 3 attributes: bought, shorted, options.
# Each of bought, shorted, and options is a list of Security objects, which have attributes
# symbol, description, quantity, purchase_price, current_price, current_value, and gain_loss

bought_securities = portfolio.bought
shorted_securities = portfolio.shorted
options = portfolio.options

for bought in bought_securities:
    print(bought.symbol)
    print(bought.description)
    print(bought.purchase_price)
    # etc.
'''
# Repeat above loop for shorted securities and options
