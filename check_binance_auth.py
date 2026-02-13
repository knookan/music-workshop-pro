import ccxt
import json

def check_permissions():
    try:
        with open('binance_keys.json', 'r') as f:
            keys = json.load(f)
        
        exchange = ccxt.binance({
            'apiKey': keys['api_key'],
            'secret': keys['secret_key'],
        })
        
        # Try to fetch account info which often includes permissions
        account_info = exchange.fapiPrivateGetAccount() if hasattr(exchange, 'fapiPrivateGetAccount') else exchange.privateGetAccount()
        
        print(f"Hesap Tipi: {account_info.get('accountType', 'Bilinmiyor')}")
        print(f"Komisyon Oranları: {account_info.get('makerCommission', 0)/10000}% / {account_info.get('takerCommission', 0)/10000}%")
        print("Kontrol yetkisi aktif.")
        
    except Exception as e:
        print(f"Hata veya Sınırlı Yetki: {str(e)}")

if __name__ == "__main__":
    check_permissions()
