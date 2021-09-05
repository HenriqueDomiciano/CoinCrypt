from requests import Session
import json

class coincrypt:
    """
        This class is a project to make more easy to use the CoinMarketCap API
        it haves the objective of been of simple usage for basic methods in this API

    """
    def __init__(self,token):

        """ url: APIs URL
            token : Credentials of the API
        """
        
        self.url = 'https://pro-api.coinmarketcap.com/v1/'
        self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    
    def get_price_by_symbol(self,symbol ='BTC',max_search=100):
        """
            This method is made for getting the actual price(USD) given an symbol ex (BTC,ETE,LTC...)
            Parameters:
                symbol :: str -- The symbol of the crypto
                max_search :: int -- the maximun number of cryptos the method will search

        """
        symbol = symbol.split(',')
        coins= []
        parameters = {
            'start' : 1,
            'limit' : max_search
        }
        url = self.url + 'cryptocurrency/listings/latest'
        resposta = self.session.get(url,params=parameters)
        k = json.loads(resposta.text)
        k = k['data']
        for i in range(len(k)):
            if k[i]['symbol'] in symbol:
                coins.append([k[i]['symbol'],k[i]['quote']['USD']['price']])
        return dict(coins)
    
    def get_by_price(self,min_price,max_price,max_search = 100):
        
        """
        This method is made to give an python dictionary with all the coins inside the parameters given
        Parameters:
            max_price :: float -- The maximum price of the coin
            min_price :: float -- The minimum price of the coin
            max_search :: int -- the maximun number of cryptos the method will search
        """
        
        parameters={
            'start': 1, 
            'limit':max_search
        }
        coins = []        
        url = self.url + 'cryptocurrency/listings/latest'
        resposta = self.session.get(url,params=parameters)
        k = json.loads(resposta.text)['data']
        for i in range(len(k)):
            if k[i]['quote']['USD']['price']<=max_price and k[i]['quote']['USD']['price']>=min_price:
                coins.append([(k[i]['symbol']),k[i]['quote']['USD']['price']])
        return dict(coins)

    
    def get_price_by_name(self,name):
        
        """
        This methods get the price by the name of the coin ex : cardano, bitcoin, ethereum ...
        Parameters:
            name :: str -- The name of the coin
        """
        name = name.split(',')
        coins = []
        url = self.url + 'cryptocurrency/listings/latest'
        resposta = self.session.get(url)
        k = json.loads(resposta.text)['data']
        
        for i in range(len(k)):
            if k[i]['slug'] in name:
                coins.append([k[i]['slug'],k[i]['quote']['USD']['price']])
        
        return dict(coins)
    
    
    def get_by_volume(self,min_vol ,max_vol,period = 0 ,max_search = 100):
        
        """
        This method returns an python dictionary with the coins symbols and the volume in certain period 
        Parameters :
            min_vol :: float -- minimun volume for search
            max_vol :: float -- maximum volume for search
            period :: int -- the period you want to volume to be analized
                period == 0 --> volume in 24 hours
                period == 1 --> moving average of the last 7 days 
                period == 2 -->moving average of the last 30 days 
            max_search :: int -- the maximun number of cryptos the method will search   

        """
        periods = ['volume_24h','volume_7d','volume30d']
        parameters = {
            'start': 1 , 
            'limit': max_search
        }
        url = self.url + 'cryptocurrency/listings/latest'
        coins = []
        resposta = self.session.get(url,params=parameters)
        k = json.loads(resposta.text)['data']
        for i in range(len(k)):
            if k[i]['quote']['USD'][periods[period]]<=max_vol and k[i]['quote']['USD'][periods[period]]>=min_vol:
                coins.append([(k[i]['symbol']),k[i]['quote']['USD'][periods[period]]])
        return dict(coins)
    
    
    def get_by_change(self,min_change ,max_change ,period = 0,max_search = 100):
        
        '''
        This method returns a python dictionary with the coins that are inside the interval of changes 
        Parameters :
            min_change :: float -- the minimum of the interval of change 
            max_change :: float -- the maximun of the interval of change 
            period :: int -- the period you want the interval of chage to be analized
                period == 0 --> change in percentage of 1 hour
                period == 1 --> change in percentage in 24 hours 
                period == 2 --> change in percentage in 7 days
                period == 3 -->> change in percentage in 30 days  

        '''
        
        def get_change(p,k):
            coins =[]
            periods = ["percent_change_1h","percent_change_24h","percent_change_7d","percent_change_30d"]
            for i in range(len(k)):
                if k[i]['quote']['USD'][periods[p]]<=max_change and k[i]['quote']['USD'][periods[p]]>= min_change:
                    coins.append([(k[i]['symbol']),k[i]['quote']['USD'][periods[p]]])
            return dict(coins)
        parameters = {
            'start': 1 ,
            'limit': max_search
        }
        url = self.url + 'cryptocurrency/listings/latest'
        resposta = self.session.get(url,params=parameters) 
        k = json.loads(resposta.text)['data']
        return get_change(period,k)
    
    
    def get_historical(self,symbol='BTC',max_search=100):
        
        '''
        this method gives the historical features of the coin 
        Parameters : 
            symbol :: str -- The symbol of the coin you want to know the history of 
        '''
        
        parameters = {
            'start': 1 ,
            'limit':max_search,
            'symbol':symbol
        }
        url = self.url + 'cryptocurrency/map'
        resposta = self.session.get(url,params=parameters)
        return json.loads(resposta.text)['data']

    def convert_crypto(self,converte_from = 'BTC',convert_to = 'USD',amount = 1):
        
        """
        This method converts criptos(BTC,ETH,ADA...) in their value in flat coins such as BRL,EUR,USD,GBP...
        Parameters : 
            converte_from :: str -- The symbol of the cryptocurrency you want to be converted 
            convert_to :: str -- The symbol of the flat coin you want to be converted to 
            amount :: float -- The amount of cryptocurrency you want to be converted 
        """
        
        values = []
        coins = convert_to.split(',')
        parameters = {
            'symbol': converte_from,
            'amount' : amount,
            'convert': convert_to
        }
        url = self.url + 'tools/price-conversion'
        resposta = self.session.get(url,params=parameters)
        k = json.loads(resposta.text)['data']['quote']
        for i in range(len(k)):
            values.append([coins[i],k[coins[i]]['price']])
        return dict(values)

    def get_global_metrics(self,convert_to='USD'):
        
        '''
        This method gives the global metrics of the crytptocurrencies market 
        Parameters :
            convert_to :: str -- The symbol of the currency wich the data will be showed 
        '''
        
        if convert_to == 'USD':
            parameters= {}
        else:
            parameters ={
                'convert': convert_to
            }
        url = self.url+ 'global-metrics/quotes/latest'
        resposta = self.session.get(url,params=parameters)
        return dict(json.loads(resposta.text))['data']
    
    def get_FCAS_latest(self,slug = None, symbol = None):
        
        '''

        Show the latest FCAS (Fundamental Crypto Asset Score) of the crypto
        Parameters : 
            slug :: str -- The name of the crypto you want to have tha data information
            symbol :: str -- The symbol of the crypto you want to have the data information
        
        '''
        if slug is None and (not(symbol is None)):
            parameters = {
                'symbol': symbol
            }
        elif (symbol is None) and (not(slug) is None):
            parameters = {
                'slug':slug
            }
        else :
            print('Error you cannot use slug and symbol at the same time')
            return 
        url = self.url + 'partners/flipside-crypto/fcas/quotes/latest'
        resposta = self.session.get(url,params=parameters)
        return dict(json.loads(resposta.text)['data'])
    
    def get_variaton(value,older_value):
        return str((older_value-value)/value) + ' %'

    def get_data_by_string(self,slug =None,symbol = None ,max_search =100):
        parameters = {
                'start': 1 , 
                'limit': max_search
            }
        url = self.url + 'cryptocurrency/listings/latest'
        resposta = self.session.get(url,params=parameters)
        k = json.loads(resposta.text)['data']
        coins_temp = []
        if slug is None and (not(symbol is None)):
                
            symbol = symbol.split(',')
            for i in range(len(k)):
                if k[i]['symbol'] in symbol:
                    coins_temp.append(k[i])
            return coins_temp

        elif (symbol is None) and (not(slug) is None):
            slug = slug.split(',')
            for i in range(len(k)):
                if k[i]['slug'] in slug:
                    coins_temp.append(k[i])
            return coins_temp
            
        else :
            print('Error you cannot use slug and symbol at the same time')
            return None

    def how_much_can_buy(self,symbol = None, slug = None, max_search = None, fiat_coin = "USD",amount = 0):
        '''
            Returns an dict with the number of coins such amount of fiat coin can buy 
                - Parameters: 
                - slug :: str -- The name of the crypto you want to 'buy'
                - symbol :: str -- the symbol of the crypto you want to 'buy'
                - fiat_coin :: str -- the code of the fiat coin you want to buy from 
                - amount :: float -- the amount of fiat coin you have to buy in that cryptocurrencies

        '''
        amounts = []
        if fiat_coin == 'USD':
            
            if slug is None and (not(symbol is None)):    
                prices = self.get_price_by_symbol(symbol=symbol,max_search=max_search)
                symbols = symbol.split(',')
                for i in symbols:
                    amounts.append([i,amount/prices[i]])
                return dict(amounts)

            elif (symbol is None) and (not(slug is None)):
                prices = self.get_price_by_name(slug=slug,max_search=max_search)
                slugs = slug.split(',')
                for i in slugs:
                    amounts.append([i,amount/prices[i]])
                return dict(amounts)
            else :
                print('Error you cannot use slug and symbol at the same time')
                return None
        else:
            
            if slug is None and (not(symbol is None)):    
                symbols = symbol.split(',')
                for i in symbols:
                    price = self.convert_crypto(convert_to=fiat_coin,converte_from=i)
                    amounts.append([i,amount/price[fiat_coin]])
                return dict(amounts)
            else :
                print('Error you cannot use slug in an other coin that is not the USD')
                return None
       


