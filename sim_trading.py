import ccxt
import json
import os
import time
import random

def simulate_trading():
    try:
        with open('binance_keys.json', 'r') as f:
            keys = json.load(f)
        
        exchange = ccxt.binance({
            'apiKey': keys['api_key'],
            'secret': keys['secret_key'],
            'enableRateLimit': True,
        })
        
        history_file = 'trading_simulation.json'
        if not os.path.exists(history_file):
            state = {
                "initial_balance": 10.0,
                "current_balance": 10.0,
                "trades": []
            }
        else:
            with open(history_file, 'r') as f:
                state = json.load(f)

        # Simulation logic: pick a volatile coin from top 5
        pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT', 'AVAX/USDT']
        pair = random.choice(pairs)
        ticker = exchange.fetch_ticker(pair)
        price = ticker['last']
        
        # Decide Buy or Sell (Random for simulation purposes, but could use EMA logic)
        action = random.choice(['BUY', 'SELL'])
        
        # Calculate theoretical PnL (simulating a trade duration of 5 mins)
        # We'll just record the entry and wait for the next cron cycle to "close" it or just log it
        
        trade = {
            "timestamp": int(time.time()),
            "pair": pair,
            "action": action,
            "price": price,
            "amount": 10.0 / price # Using full simulated 10$
        }
        
        state['trades'].append(trade)
        
        # Simple PnL logic for the LAST trade if it exists
        if len(state['trades']) > 1:
            prev_trade = state['trades'][-2]
            # Mock profit/loss between -1% and +1.5%
            pnl_pct = random.uniform(-0.01, 0.015)
            profit = state['current_balance'] * pnl_pct
            state['current_balance'] += profit
            prev_trade['pnl'] = profit
            prev_trade['pnl_pct'] = pnl_pct * 100

        with open(history_file, 'w') as f:
            json.dump(state, f, indent=4)
            
        print(f"Simülasyon işlemi kaydedildi: {action} {pair} @ {price}")
        print(f"Güncel Simüle Bakiye: {state['current_balance']:.2f} USDT")

    except Exception as e:
        print(f"Simülasyon Hatası: {str(e)}")

if __name__ == "__main__":
    simulate_trading()
