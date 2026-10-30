
"""
Project Name : Stock Portfolio Tracker
Internship   : CodeAlpha - Python Programming
Developer    : Debmalya Chaki

Description:
A simple Python application that calculates the total
investment value of stocks using predefined stock prices.
"""

import csv


# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

# List to store purchased stock details
portfolio = []


def display_stock_prices():
    """Display available stocks and their prices."""

    print("\n========== AVAILABLE STOCKS ==========")

    print(f"{'Stock':<15}{'Price ($)':>12}")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock:<15}{price:>12.2f}")

    print("-" * 30)


def add_stock():
    """Add a stock and its quantity to the portfolio."""

    display_stock_prices()

    stock_name = input("\nEnter stock symbol: ").strip().upper()

    if stock_name not in stock_prices:
        print("Sorry! This stock is not available.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Invalid quantity! Please enter a whole number.")
        return

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append({
        "stock": stock_name,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    print("\nStock added successfully!")
    print(f"Stock Name      : {stock_name}")
    print(f"Stock Price     : ${price:.2f}")
    print(f"Quantity        : {quantity}")
    print(f"Investment Value: ${investment:.2f}")


def view_portfolio():
    """Display all stocks added to the portfolio."""

    if not portfolio:
        print("\nYour portfolio is currently empty.")
        return

    print("\n================ YOUR PORTFOLIO ================")

    print(f"{'Stock':<12}{'Price':>10}{'Quantity':>12}{'Value':>14}")
    print("-" * 48)

    for item in portfolio:
        print(
            f"{item['stock']:<12}"
            f"${item['price']:>9.2f}"
            f"{item['quantity']:>12}"
            f"${item['investment']:>13.2f}"
        )

    print("-" * 48)


def calculate_total():
    """Calculate the total investment value."""

    total = sum(item["investment"] for item in portfolio)

    print("\n========== INVESTMENT SUMMARY ==========")

    print("Number of stock entries:", len(portfolio))
    print(f"Total Investment Value : ${total:.2f}")

    print("=========================================")


def export_portfolio():
    """Save portfolio details into a CSV file."""

    if not portfolio:
        print("\nNothing to export. Your portfolio is empty.")
        return

    try:
        with open(
            "stock_portfolio.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            # Write column headings
            writer.writerow([
                "Stock Name",
                "Stock Price",
                "Quantity",
                "Investment Value"
            ])

            # Write portfolio details
            for item in portfolio:
                writer.writerow([
                    item["stock"],
                    item["price"],
                    item["quantity"],
                    item["investment"]
                ])

            total = sum(item["investment"] for item in portfolio)

            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])

        print("\nPortfolio exported successfully!")
        print("File created: stock_portfolio.csv")

    except OSError as error:
        print("Unable to save the file:", error)


def main():
    """Main function to control the application."""

    print("\n==========================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("==========================================")
    print("Welcome! Manage your stock investments here.")

    while True:

        print("\n--------------- MAIN MENU ---------------")
        print("1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View My Portfolio")
        print("4. Calculate Total Investment")
        print("5. Export Portfolio to CSV")
        print("6. Exit")
        print("-----------------------------------------")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_stock_prices()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            view_portfolio()

        elif choice == "4":
            calculate_total()

        elif choice == "5":
            export_portfolio()

        elif choice == "6":
            print("\nThank you for using Stock Portfolio Tracker!")
            print("Developed by Debmalya Chaki")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


# Start the application
if __name__ == "__main__":
    main()
