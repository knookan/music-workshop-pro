import ccxt
import json

def check_trade_permissions():
    try:
        with open('binance_keys.json', 'r') as f:
            keys = json.load(f)
        
        exchange = ccxt.binance({
            'apiKey': keys['api_key'],
            'secret': keys['secret_key'],
            'enableRateLimit': True,
        })
        
        # Test if we can fetch account info (Spot)
        account = exchange.privateGetAccount()
        can_trade = account.get('canTrade', False)
        
        print(f"Spot Alım-Satım Yetkisi: {can_trade}")
        
        # Check if Futures is enabled (requires fapi)
        try:
            futures_exchange = ccxt.binanceusdm({
                'apiKey': keys['api_key'],
                'secret': keys['secret_key'],
            })
            futures_account = futures_exchange.fapiPrivateGetAccount()
            can_trade_futures = True
            print("Futures (Vadeli İşlem) Yetkisi: Aktif")
        except:
            can_trade_futures = False
            print("Futures (Vadeli İşlem) Yetkisi: Kapalı veya Erişim Yok")
            
        return can_trade, can_trade_futures

    except Exception as e:
        print(f"Hata: {str(e)}")
        return False, False

if __name__ == "__main__":
    check_trade_permissions()
