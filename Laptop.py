import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

df = pd.read_csv(r'C:\Users\PC-User\CSS145\LaptopPrice.csv')
st.title("Laptop Prices Data Analysis")

st.write("Group 2")
st.write("Tyrell John C. Del Carmen")
st.write("Claraence Paragoso")
st.write("Markus Antwone Nadora")
st.write("Monti Kilayco")



st.caption("The Dataset")
df 
df.shape
st.caption("Columns of Dataset.")
df.columns
st.caption("Table to Detect NaN Values in the Dataset.")
st.write(df.isna().sum())
st.caption("Duplicated Sum.")
st.write(df.duplicated().sum())
st.caption("Description of Dataset.")
st.write(df.describe())
st.caption("Information of Dataset.")
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)
st.caption("Unique Values for Each Columns.")
st.write(df.nunique())


st.write(df.Product.value_counts())

plt.figure(figsize=(10, 10))
plt.pie(df['TypeName'].value_counts(), labels=df['TypeName'].value_counts().index, autopct='%1.1f%%')
plt.title('TypeName Pie Chart')
st.pyplot(plt)
plt.clf()
st.markdown("TypeName Pie Chart Distribution")

st.write("This is a pie chart that represents the TypeNames of the laptops. Typename basically describes what type of laptop the device is. There are laptops that specialize in Gaming, another type is ultrabook where they specialize in their lightweight, very thin and has an extended battery life. Which makes it very convenient to bring anywhere.")
st.write("In this Graph, it shows that majority of the Laptops that are being sold are notbook laptops. Which has a 55.5% population in the dataset. While the other typenames are closely on par with numbers such as Gaming (16.1%), Ultrabook (15.2%) 2 in 1 Convertible (9.2%). And the lowest population of typenames in the dataset are Workstation (2.3%) and Netbook (1.8%)")

company_avg_price = df.groupby('Company')['Price (Euro)'].mean()
plt.figure(figsize=(15, 5))
plt.bar(company_avg_price.index, company_avg_price.values)
plt.title('Average Laptop Price by Company')
plt.xlabel('Company')
plt.ylabel('Average Price (euros)')
plt.xticks(rotation=90)
st.pyplot(plt)
plt.clf()
st.markdown("Average Laptop Price Per Company Bar Chart")

st.write("This Bar Graph shows the Average Laptop Price per company. In this graph it shows that Razer has the highest average laptop price out of all the companies. With an average price of 3346.14 Euros. While the other companies usually play arounud the 1000-2000 Euro Range. While the lowest average price came from the Vero Company with an average price of 217.43 Euros.")
company_avg_price

