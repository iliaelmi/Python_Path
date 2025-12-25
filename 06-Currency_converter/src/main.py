import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Fetch the exchange rate between two currencies using ExchangeRate-API.

    Parameters:
    - base_currency (str): The currency you want to convert from (e.g., 'USD').
    - target_currency (str): The currency you want to convert to (e.g., 'EUR').

    Returns:
    - float: The exchange rate if successful.
    - None: If the currency code is invalid or API fails.
    """
    url = f"https://v6.exchangerate-api.com/v6/0d41627ff1429995d6eb9583/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    # Check if API returned conversion rates and the target currency exists
    if 'conversion_rates' in data and target_currency in data['conversion_rates']:
        return data['conversion_rates'][target_currency]
    else:
        return None


def convert_currency(amount, exchange_rate):
    """
    Convert an amount using the given exchange rate.

    Parameters:
    - amount (float): The amount in base currency.
    - exchange_rate (float): The exchange rate from base to target currency.

    Returns:
    - float: Converted amount in target currency.
    """
    return amount * exchange_rate


def main_menu():
    """
    Display a terminal menu for currency conversion and exchange rate checking.
    
    Options:
    1. Convert Currency: Convert an amount from base to target currency.
    2. Check Exchange Rate: Show the current exchange rate between two currencies.
    3. Exit: Quit the program.
    """
    while True:
        # Display menu
        print("\n=== Currency Converter Menu ===")
        print("1. Convert Currency")
        print("2. Check Exchange Rate")
        print("3. Exit")

        # Get user choice
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            # Convert currency
            base = input("Enter base currency (e.g., USD): ").upper().strip()
            target = input("Enter target currency (e.g., EUR): ").upper().strip()
            amount = float(input(f"Enter amount in {base}: "))
            rate = get_exchange_rate(base, target)
            if rate:
                converted = convert_currency(amount, rate)
                print(f"{amount} {base} = {converted:.2f} {target}")
            else:
                print("Error: Could not get exchange rate. Check currency codes.")
        
        elif choice == '2':
            # Check exchange rate
            base = input("Enter base currency (e.g., USD): ").upper().strip()
            target = input("Enter target currency (e.g., EUR): ").upper().strip()
            rate = get_exchange_rate(base, target)
            if rate:
                print(f"Exchange rate {base} -> {target} = {rate:.4f}")
            else:
                print("Error: Could not get exchange rate. Check currency codes.")
        
        elif choice == '3':
            # Exit program
            print("Exiting program. Goodbye!")
            break
        
        else:
            # Invalid menu choice
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == '__main__':
    # Start the terminal menu
    main_menu()
