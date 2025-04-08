import streamlit as st
import requests
import pandas as pd
import smtplib

# Streamlit UI components
st.title("UST Rollover & Fed QT Alert System")
st.markdown("### Monitor High-Risk Treasury Events")

# Scrape data (replace with actual URL and logic)
def fetch_treasury_data():
    url = 'https://www.treasurydirect.gov/govt/reports/pd/mspd/mspd.htm'  # Update this URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        st.error(f"An error occurred while fetching data: {e}")
        return pd.DataFrame(columns=["Maturity Date", "Amount ($)"])
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all("table")

    # Process data here (simplified example)
    maturity_data = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 1:
                try:
                    date = cols[0].text.strip()
                    amount = cols[1].text.strip().replace('$', '').replace(',', '')
                    maturity_data.append([date, float(amount)])
                except ValueError:
                    continue  # Skip rows with invalid data
    
    return pd.DataFrame(maturity_data, columns=["Maturity Date", "Amount ($)"])

# Example usage
df = fetch_treasury_data()
if not df.empty:
    st.dataframe(df)
