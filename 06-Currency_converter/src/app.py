import streamlit as st
from main import get_exchange_rate, convert_currency
import requests

st.title("🌍 Full Currency Converter")

st.markdown("""
Convert any currency to any other currency using real-time exchange rates.
Select the currencies and enter the amount to see the result.
""")

# Get full list of currencies from the API
def get_currency_list():
    url = "https://v6.exchangerate-api.com/v6/0d41627ff1429995d6eb9583/latest/USD"
    response = requests.get(url)
    data = response.json()
    if 'conversion_rates' in data:
        return list(data['conversion_rates'].keys())
    else:
        st.error("Error fetching currency list")
        return []

currency_list = get_currency_list()

# Select currencies
base_currency = st.selectbox("From Currency (Base):", currency_list, index=currency_list.index("USD"))
target_currency = st.selectbox("To Currency (Target):", currency_list, index=currency_list.index("EUR"))

# Input amount
amount = st.number_input("Amount to Convert:", min_value=0.0, value=1.0)

# Conversion
if amount > 0:
    try:
        rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        st.success(f"✅ {amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        st.info(f"Exchange Rate: 1 {base_currency} = {rate:.4f} {target_currency}")
    except Exception as e:
        st.error(f"Error fetching exchange rate: {e}")
