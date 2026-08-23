# A currency converter using fixed exchange rates
# NB- These rates are hardcoded, not live. Check out the "Live Currency Converter"
# project later on for a version that pulls real-time rates from an API.

# A dictionary storing how much 1 USD is worth in each currency
rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "NGN": 1550.0,
    "JPY": 149.0
}

print("====== Currency Converter ======")
print("Available currencies:", ", ".join(rates.keys()))  # ".join()" turns the list into text
print()

# Get the conversion details from the user
amount = float(input("Enter the amount: "))
from_currency = input("Convert from (e.g. USD): ").upper()  # ".upper()" avoids case issues
to_currency = input("Convert to (e.g. EUR): ").upper()

# Make sure both currencies exist in our dictionary
if from_currency not in rates or to_currency not in rates:
    print("Sorry, one of those currencies isn't supported.")
else:
    # Step 1: convert the amount into USD first (our "base" currency)
    amount_in_usd = amount / rates[from_currency]

    # Step 2: convert from USD into the target currency
    converted_amount = amount_in_usd * rates[to_currency]

    print("=" * 30)
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    