import streamlit as st
import requests

# Function to get exchange rates
def get_exchange_rates(base_currency='USD'):
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data['rates']
    else:
        st.error("Error fetching data")
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == 'USD':
        converted_amount = amount * rates[to_currency]
    else:
        # Convert from another currency to USD first
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]
    
    return converted_amount

# Streamlit App
def main():
    st.title("Currency Converter")
    
    # Get the exchange rates
    rates = get_exchange_rates()

    if rates is None:
        return

    # Currency options
    currencies = {
        'USD': 'United States Dollar',
        'EUR': 'Euro',
        'JPY': 'Japanese Yen',
        'GBP': 'British Pound Sterling',
        'AUD': 'Australian Dollar',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'CNY': 'Chinese Yuan Renminbi',
        'SEK': 'Swedish Krona',
        'NZD': 'New Zealand Dollar',
        'SGD': 'Singapore Dollar',
        'HKD': 'Hong Kong Dollar',
        'NOK': 'Norwegian Krone',
        'KRW': 'South Korean Won',
        'INR': 'Indian Rupee',
        'BRL': 'Brazilian Real',
        'MXN': 'Mexican Peso',
        'ZAR': 'South African Rand',
        'TRY': 'Turkish Lira',
        'RUB': 'Russian Ruble',
        'PLN': 'Polish Zloty',
        'DKK': 'Danish Krone',
        'THB': 'Thai Baht',
        'IDR': 'Indonesian Rupiah',
        'PHP': 'Philippine Peso',
        'MYR': 'Malaysian Ringgit',
        'HUF': 'Hungarian Forint',
        'CZK': 'Czech Koruna',
        'CLP': 'Chilean Peso',
        'PKR': 'Pakistani Rupee',
        'BDT': 'Bangladeshi Taka'
    }

    # User inputs
    from_currency = st.selectbox("Select currency to convert from", list(currencies.keys()))
    to_currency = st.selectbox("Select currency to convert to", list(currencies.keys()))
    amount = st.number_input("Enter the amount to convert", min_value=0.0, step=0.01)

    if st.button("Convert"):
        if from_currency in rates and to_currency in rates:
            converted_amount = convert_currency(amount, from_currency, to_currency, rates)
            st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            st.error("Invalid currency code entered.")

if _name_ == "_main_":
    main()
