import requests

def get_realtime_data(symbol):
    # Binance API örneği (API key gerektirmez)
    url = f'https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return {
        'price': float(data['lastPrice']),
        'volume': float(data['volume'])
    }
