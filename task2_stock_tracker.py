# Stock Portfolio Tracker
# Uses manually defined sample prices (not live market prices).

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 175
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices))

while True:
    stock = input("\\nEnter stock symbol (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    portfolio.append((stock, quantity, price, value))
    print(f"{stock}: {quantity} shares = ${value:.2f}")

print("\\n===== PORTFOLIO SUMMARY =====")
if not portfolio:
    print("No stocks were added.")
else:
    for stock, quantity, price, value in portfolio:
        print(f"{stock}: {quantity} shares x ${price:.2f} = ${value:.2f}")

    print(f"Total investment: ${total_investment:.2f}")

    save = input("Save summary to CSV? (yes/no): ").lower().strip()
    if save == "yes":
        import csv
        with open("portfolio_summary.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            writer.writerows(portfolio)
            writer.writerow(["", "", "Total Investment", total_investment])
        print("Summary saved as portfolio_summary.csv")
