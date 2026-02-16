import random
import datetime

def simulate_trade(starting_balance):
    # Mock data for demonstration
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT"]
    symbol = random.choice(symbols)
    
    # Simulate a small overnight price movement (-2% to +3%)
    change_pct = random.uniform(-0.02, 0.03)
    ending_balance = starting_balance * (1 + change_pct)
    profit = ending_balance - starting_balance
    
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    log_entry = (
        f"[{timestamp}] Trade Simulation: {symbol}\n"
        f"Initial: {starting_balance:.2f} USDT | Final: {ending_balance:.2f} USDT | Profit: {profit:+.4f} USDT\n"
        f"--------------------------------------------------\n"
    )
    
    with open("trading_sim.log", "a") as f:
        f.write(log_entry)
    
    return log_entry

if __name__ == "__main__":
    result = simulate_trade(10.0)
    print(result)
