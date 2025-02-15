import streamlit as st

st.title("🎈 My new app")
import streamlit_app as st
import pandas as pd 
import plotly.express as pd
import os
print(os.path.exists("style.css"))  # Should print True if the file exists

st.set_page_config(layout= 'wide', initial_sidebar_state= 'expanded') 
#Expands the app layout to use the full width of the screen
#Expands the sidebar by default when the app loads.
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html= True)
st.sidebar.header('Menu')
st.sidebar.subheader('Money income')

st.title("♉ My fianace dashboard ☻")
st.write()
#input income
income = st.number_input("Income (thousand): ", min_value = 0, value = 7000, step = 1)

# Expense Goods
goods = ["Rent", "Merch", "Debt", "Foods", "Drinks", "Petrol", "Shopping", "Others"]
expense_data = {}
for good in goods:
    expense_data[good] = st.number_input(f"{goods} expense (thousand)", min_value = 0, value = 0, step = 10)
    
#Convert to DataFrame
df = pd.DataFrame(expense_data.items(), columns= ["good", "Amount"]) # a data structure that organizes data into rows and columns

# Calculate Total Expenses & Savings
total_expense = df["Amount"].sum()
saving = income - total_expense

#show
st.subheader("Fianace State")
st.write(f"**Total Income:** {income}K")
st.write(f"**Total Expense:** {total_expense}K")
st.write(f"**Saving:** {saving}K")

