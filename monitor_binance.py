import ccxt
import json
import os
import time

def monitor_binance():
    try:
        with open('binance_keys.json', 'r') as f:
            keys = json.load(f)
        
        exchange = ccxt.binance({
            'apiKey': keys['api_key'],
            'secret': keys['secret_key'],
            'enableRateLimit': True,
        })
        
        # 1. Fetch Balance
        balance = exchange.fetch_balance()
        total_usdt = balance['total'].get('USDT', 0)
        
        # 2. Fetch Prices for Top Coins
        tickers = exchange.fetch_tickers(['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'SOL/USDT'])
        
        report = {
            "timestamp": int(time.time()),
            "total_usdt": total_usdt,
            "prices": {symbol: data['last'] for symbol, data in tickers.items()},
            "assets": {k: v for k, v in balance['total'].items() if v > 0}
        }
        
        # Save state for historical comparison
        history_file = 'binance_history.json'
        history = []
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
        
        history.append(report)
        # Keep last 100 checks
        history = history[-100:]
        
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=4)
            
        print(f"Kontrol tamamlandı. Toplam USDT: {total_usdt}")
        return report

    except Exception as e:
        print(f"Hata: {str(e)}")
        return None

if __name__ == "__main__":
    monitor_binance()
