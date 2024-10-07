import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

url = 'https://raw.githubusercontent.com/Lixir81/CSS145/refs/heads/main/LaptopPrice.csv'
df = pd.read_csv(url)
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

average_weight = df.groupby('TypeName')['Weight (kg)'].mean().reset_index()
average_weight.index = range(1, len(average_weight) + 1)
plt.figure(figsize=(12, 6))
sns.barplot(x='TypeName', y='Weight (kg)', data=average_weight)
plt.title('Average Weight of Laptops by TypeName')
plt.xlabel('TypeName')
plt.ylabel('Average Weight (kg)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(plt)
plt.clf()
st.markdown("Average Weight of Laptops by TypeName Bar Chart")

st.write("The bar chart illustrates the average weight of laptops categorized by their type. From the results, Gaming laptops are the heaviest on average at approximately 2.95 kg, while Netbooks are the lightest at about 1.32 kg. Quite similar to Netbooks,Ultrabooks has a relatively low average weight of 1.34 kg. In contrast, Notebooks weigh around 2.06 kg, and Workstations are slightly heavier at 2.47 kg. Lastly,the 2 in 1 Convertible laptops average about 1.55 kg.")
average_weight

company_model_count = df['Company'].value_counts()
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Company', order=company_model_count.index)
plt.title('Count of Laptop Models by Company')
plt.xticks(rotation=45)
plt.ylabel('Number of Models')
plt.xlabel('Company')
st.pyplot(plt)
plt.clf()
st.markdown("Count of Laptop Models by Company Bar Chart")

st.write("The bar graph shows the number of laptop models offered by each company. The result reveals that Dell has the highest number with 291 models, closely followed by Lenovo with 289 models. HP offers 268 models, while Asus and Acer have 152 and 101 models, respectively. On the other hand, several companies have significantly fewer models, with Apple at 21, Samsung at 9, and brands like Razer and Mediacom having 7 models. Notably, companies like Chuwi, Google, Fujitsu, LG each have only 3 models with Huawei being the company with the lowest laptop model count at 2.")
company_model_count

plt.figure(figsize = (10, 10))
plt.title('GPU Brand Chart')
plt.pie(df['GPU_Company'].value_counts(), labels = df['GPU_Company'].value_counts().index, autopct = '%1.2f%%')
plt.show()
st.markdown("GPU Brand Percentage Chart")

st.write("The chart shows various GPUs that are utilised by the laptops. As it shows, most of them use Intel - most likely CPU-integrated graphics - with a share of 55.22%. When it comes to dedicated graphics cards, Nvidia takes the lead at 31%, with AMD coming in at second (third overall) with 13.65%. ARM comes in at last with 0.8%.")

ram_per_laptop = df.groupby('TypeName')['RAM (GB)'].mean()

plt.figure(figsize = (15, 15))
plt.title('RAM Size by Laptop Type Chart')
plt.bar(ram_per_laptop.index, ram_per_laptop.values)
plt.xlabel('Laptop Type')
plt.ylabel('RAM Size')
plt.show()
st.markdown("Average RAM Size per Laptop Type Chart")

st.write("The bar graph shows the average RAM size per type of Laptop. Gaming laptops have the most; Workstations come in at second; Ultrabooks at third; 2-in-1 Convertibles at fourth; Notebooks at fifth; and Netbooks at sixth. This shows the peformance and the workload these types of laptops typically and can do.")
