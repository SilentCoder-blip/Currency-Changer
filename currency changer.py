import streamlit as st
import requests
import pandas as pd

# API endpoint and your API key (Get it from ExchangeRate-API)
API_URL = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"

# Function to get exchange rates
@st.cache_data
def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data["conversion_rates"]

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        # Convert from the original currency to USD first
        amount_in_usd = amount / rates[from_currency]
    else:
        amount_in_usd = amount

    # Convert from USD to the target currency
    return amount_in_usd * rates[to_currency]

# Main Streamlit app
def main():
    st.title("Currency Changer App")

    # Fetch the latest exchange rates
    rates = get_exchange_rates()

    # Display the available currencies
    currency_options = list(rates.keys())

    # Input fields
    amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
    from_currency = st.selectbox("From Currency:", options=currency_options)
    to_currency = st.selectbox("To Currency:", options=currency_options)

    # Convert button
    if st.button("Convert"):
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        st.write(f"Converted Amount: {converted_amount:.2f} {to_currency}")

    # Displaying current rates in a table
    st.write("### Current Exchange Rates (Base: USD)")
    rates_df = pd.DataFrame(rates.items(), columns=["Currency", "Rate"])
    st.dataframe(rates_df)

if __name__ == "__main__":
    main()
