# CoinCrypt

An code to handle basic methods in the coin market cap API.
To use this code initialize an class Coincrypt
[Link to Github](https://github.com/HenriqueDomiciano/CoinCrypt)
## Getting Started 

Simple Code to connect the API :
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
```
## Methods

**get_price_by_symbol :** 

This method is made for getting the actual price(USD) given an symbol ex (BTC,ETE,LTC...)
Obs - in version >=2.10.0 you can also use list of strings
- Parameters:
    - symbol :: str -- The symbol of the crypto (for multiple prices use , inside the string )
    - max_search :: int -- the maximun number of cryptos the method will search

Code Example:
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_price_by_symbol('BTC,ADA,ETH')
```

**get_by_price :**

This method is made to give an python dictionary with all the coins inside the parameters given
- Parameters:
    - max_price :: float -- The maximum price of the coin
    - min_price :: float -- The minimum price of the coin
    - max_search :: int -- the maximun number of cryptos the method will search

Code Example : 
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_by_price(min_price = 0.2,max_price = 1, max_search = 100)# will return a python dict with the coins inside this values  
```

get_price_by_name : 

This methods get the price by the name of the coin ex : cardano, bitcoin, ethereum ...
    Parameters:
    name :: str -- The name of the coin,(To use multiple coins separte then by , )

Code Example : 
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_price_by_name(name = 'cardano,bitcoin')
```
**get_by_volume :** 
    
This method returns an python dictionary with the coins symbols and the volume in certain period 
- Parameters :
    - min_vol :: float -- minimun volume for search
    - max_vol :: float -- maximum volume for search
    - period :: int -- the period you want to volume to be analized
        - period == 0 --> volume in 24 hours
        - period == 1 --> moving average of the last 7 days 
        - period == 2 --> moving average of the last 30 days 
    - max_search :: int -- the maximun number of cryptos the method will search  

Code Example:
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_price_by_volume(min_vol = 0 , max_vol = 100000, period = 0 )# get all the coins with the volume of 0 to 100000 in 24 hours in a dict with vol 
```

**get_by_change :**
       
This method returns a python dictionary with the coins that are inside the interval of changes 
- Parameters :.
    - min_change :: float -- the minimum of the interval of change
    - max_change :: float -- the maximun of the interval of change
    - period :: int -- the period you want the interval of chage to be analized
        - period == 0 --> change in percentage of 1 hour
        - period == 1 --> change in percentage in 24 hours 
        - period == 2 --> change in percentage in 7 days
        - period == 3 --> change in percentage in 30 days  

Code Example : 
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_price_by_volume(min_change = 0 , max_change = 1, period = 0) # will return a dict with all coins with the variation between 0 and 1 in 1 hour  
```
**get_historical :** 
    
This method gives the historical features of the coin 
- Parameters : 
    - symbol :: str -- The symbol of the coin you want to know the history of (only accepts one)

Code Example : 
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_historical('BTC')# returns historical features of bitcoin in json Object
```

**convert_crypto :** 

This method converts criptos(BTC,ETH,ADA...) in their value in fiat coins such as BRL,EUR,USD,GBP...
Obs - in version >=2.10.0 you can also use list of strings in convert_to
- Parameters : 
    - converte_from :: str -- The symbol of the cryptocurrency you want to be converted (can use multiple entrance depending on your api plan) 
    - convert_to :: str -- The symbol of the flat coin you want to be converted to 
    - amount :: float -- The amount of cryptocurrency you want to be converted 
        
Code Example : 
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.convert_crypto('BTC','USD,1)# returns a dict with the realtion between USD and the price of 1 bitcoin
```
**get_global_metrics :** 

This method gives the global metrics of the crytptocurrencies market 
- Parameters :
    - convert_to :: str -- The symbol of the currency wich the data will be showed 

Code Example:
```python    
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.convert_crypto('BRL') # return global market data in dict format converted to BRL('Brazilian Real)
```
**get_FCAS_latest**:
    
Show the latest FCAS (Fundamental Crypto Asset Score) of the crypto
- Parameters : 
    - slug :: str -- The name of the crypto you want to have tha data information
    - symbol :: str -- The symbol of the crypto you want to have the data information

Code Example:

```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_FCAS_latest('BTC')# returns json Object with the FCAS data 
```

**get_data_by_string:** 

Get all the data avaliable by the API given an string of symbols or names of coins
Obs - in version >=2.10.0 you can also use list of strings 
- Parameters :
    - slug :: str -- The name of the crypto you want to have tha data information
    - symbol :: str -- The symbol of the crypto you want to have the data information

Code Example:
```python
from CoinCrypt import Coincrypt as cp
cr = cp.coincrypt('API_KEY')
cr.get_data_by_string(symbol = 'BTC,ETH,BNB') 
```
**how_much_can_buy**

Returns an dict with the number of coins such amount of fiat coin can buy
Obs - in version >=2.10.0 you can also use list of strings
- Parameters: 
    - slug :: str -- The name of the crypto you want to 'buy'
    - symbol :: str -- the symbol of the crypto you want to 'buy'
    - fiat_coin :: str -- the code of the fiat coin you want to buy from 
    - amount :: float -- the amount of fiat coin you have to buy in that cryptocurrencies
Code Example : 
```python
from CoinCrypt import Coincrypt as cp
cr = coincrypt('API_KEY') 
amount = cr.how_much_can_buy(symbol='ADA,ETH',amount=80))    
```
if you like to help me here is my cardano,BitCoin and Ethereum wallet:

    ADA : addr1q9rm6tavahr3qda2dje7vsac6l0yyqxuj3x82l9ckjpm7fxj7y2w4rym5f6psf5v4kw5dcezdjmw29625sews2zqtjhql2dlxj
    BTC : bc1qazdaj8at50mcs5fsm5vj8wzfn6yxac9nes3ktg
    ETH : 0x62786833a10436B394512E8F42F26C6BD3c4040c

Created by Henrique Domiciano Osinski