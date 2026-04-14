# Task 2: Stock Portfolio Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "META": 350,
    "AMZN": 500,
    "GOOGL": 2800
}

# Ask user for input
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares → ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optionally save to file
save_choice = input("Do you want to save results to a file? (y/n): ").lower()
if save_choice == "y":
    with open("portfolio_tracker.csv", "w") as f:
        f.write("Stock,Quantity,Value\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock] * qty}\n")
        f.write(f"Total,,{total_value}\n")
    print("Portfolio saved to portfolio_tracker.csv")
