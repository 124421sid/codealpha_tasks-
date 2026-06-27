stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 170,
    "META": 320,
    "NFLX": 420
}


def display_available_stocks():
    print("\n" + "="*50)
    print("AVAILABLE STOCKS AND PRICES")
    print("="*50)
    for stock, price in stock_prices.items():
        print(f"{stock:10} : ₹{price:6}")
    print("="*50 + "\n")


def get_stock_input():
    portfolio = {}
    
    print("\n" + "="*50)
    print("STOCK PORTFOLIO TRACKER")
    print("="*50)
    display_available_stocks()
    
    while True:
        print("\n--- Add Stock to Portfolio ---")
        stock_name = input("Enter stock name (or 'DONE' to finish): ").upper().strip()
        
        if stock_name == "DONE":
            if not portfolio:
                print("❌ Error: Please add at least one stock!")
                continue
            break
        
        if stock_name not in stock_prices:
            print(f"❌ Error: '{stock_name}' not found in available stocks!")
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity <= 0:
                print("❌ Error: Quantity must be greater than 0!")
                continue
        except ValueError:
            print("❌ Error: Please enter a valid integer quantity!")
            continue
        
        stock_investment = stock_prices[stock_name] * quantity
        
        if stock_name in portfolio:
            portfolio[stock_name]["quantity"] += quantity
            portfolio[stock_name]["investment"] = stock_prices[stock_name] * portfolio[stock_name]["quantity"]
        else:
            portfolio[stock_name] = {
                "price": stock_prices[stock_name],
                "quantity": quantity,
                "investment": stock_investment
            }
        
        print(f"✓ Added {quantity} shares of {stock_name} @ ₹{stock_prices[stock_name]} = ₹{stock_investment}")
    
    return portfolio


def calculate_total_investment(portfolio):
    total = sum(stock["investment"] for stock in portfolio.values())
    return total


def display_portfolio(portfolio):
    total_investment = calculate_total_investment(portfolio)
    
    print("\n" + "="*80)
    print("PORTFOLIO SUMMARY")
    print("="*80)
    print(f"{'Stock':<10} {'Price':>10} {'Quantity':>10} {'Total Value':>15}")
    print("-"*80)
    
    for stock_name, details in portfolio.items():
        print(f"{stock_name:<10} ₹{details['price']:>9} {details['quantity']:>10} ₹{details['investment']:>14}")
    
    print("-"*80)
    print(f"{'TOTAL INVESTMENT:':<30} ₹{total_investment:>14}")
    print("="*80 + "\n")
    
    return total_investment


def save_to_file(portfolio, total_investment, file_format="txt"):
    filename = f"portfolio_report.{file_format}"
    
    try:
        if file_format.lower() == "txt":
            with open(filename, "w") as file:
                file.write("="*80 + "\n")
                file.write("STOCK PORTFOLIO TRACKER - REPORT\n")
                file.write("="*80 + "\n\n")
                file.write(f"{'Stock':<10} {'Price':>10} {'Quantity':>10} {'Total Value':>15}\n")
                file.write("-"*80 + "\n")
                
                for stock_name, details in portfolio.items():
                    file.write(f"{stock_name:<10} ₹{details['price']:>9} {details['quantity']:>10} ₹{details['investment']:>14}\n")
                
                file.write("-"*80 + "\n")
                file.write(f"{'TOTAL INVESTMENT:':<30} ₹{total_investment:>14}\n")
                file.write("="*80 + "\n")
        
        elif file_format.lower() == "csv":
            with open(filename, "w") as file:
                file.write("Stock,Price,Quantity,Total_Value\n")
                for stock_name, details in portfolio.items():
                    file.write(f"{stock_name},{details['price']},{details['quantity']},{details['investment']}\n")
                file.write(f"\nTotal_Investment,,{total_investment}\n")
        
        print(f"✓ Portfolio saved to '{filename}'")
        return True
    
    except IOError as e:
        print(f"❌ Error saving file: {e}")
        return False


def main():
    try:
        portfolio = get_stock_input()
        
        total_investment = display_portfolio(portfolio)
        
        print("\n--- Save Report ---")
        save_choice = input("Do you want to save this portfolio report? (yes/no): ").lower().strip()
        
        if save_choice in ["yes", "y"]:
            file_format = input("Choose format (txt/csv) [default: txt]: ").lower().strip()
            if file_format not in ["txt", "csv"]:
                file_format = "txt"
            save_to_file(portfolio, total_investment, file_format)
        
        print("\n✓ Thank you for using Stock Portfolio Tracker!")
    
    except KeyboardInterrupt:
        print("\n\n⚠ Program interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
