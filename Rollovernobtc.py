import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit UI components
st.title("UST Rollover & Fed QT Alert System")
st.markdown("### Monitor High-Risk Treasury Events")

# Scrape data (replace with actual URL and logic)
def fetch_treasury_data():
    url = 'https://www.treasurydirect.gov/govt/reports/pd/mspd/mspd.htm'  # Update this URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all("table")
    
    # Process data here (simplified example)
    maturity_data = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 1:
                date = cols[0].text.strip()
                amount = cols[1].text.strip().replace('$', '').replace(',', '')
                maturity_data.append([date, float(amount)])
                
    return pd.DataFrame(maturity_data, columns=["Maturity Date", "Amount ($)"])


