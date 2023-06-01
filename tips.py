import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


primaryColor="#0F1116"
backgroundColor="#0F1116"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"


path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)
st.write("""
# Анализ чаевых ресторана 💸
""")



st.write(""" 
Взаимосвязь между общим счетом, чаевыми и размером
""")
fig,ax = plt.subplots()
ax=sns.scatterplot(data=tips, x='total_bill', y='tip', hue="size", size='size', legend="full", palette='flare')
plt.xlabel('Total bill')
st.pyplot(fig)



st.write("""
Зависимость объема чаевых от общей суммы
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size', palette="flare")
plt.xlabel('Общий счет')
plt.legend(title='Размер заказа', loc='upper left')
plt.ylabel('Чаевые')
st.pyplot(fig)


st.write("""
Зависимость объема чаевых от дня недели и пола посетителей
""")


fig,ax=plt.subplots()
sns.scatterplot(x='tip', y='day', size='tip', hue='sex', data=tips, palette={'Male': '#693A66', 'Female': '#CC8C78'})
plt.xlabel('Чаевые')
plt.ylabel('День недели')
st.pyplot(fig)



st.write("""
Распределение суммы счета с учетом времени обслуживания
""")

fig,ax=plt.subplots()
sns.boxplot(data=tips, x='day', y='total_bill', hue='time', palette='flare')
plt.xlabel('День недели')
plt.ylabel('Общий счет')
st.pyplot(fig)

st.write("""
Зависимость суммы счета от дня недели
""")
fig, ax = plt.subplots()
mean_bill=tips.groupby('day')['total_bill'].mean().astype(int).sort_values().reset_index()
ax=sns.barplot(data=mean_bill,x='day',y='total_bill',palette='flare')
plt.title('Average bill per day')
plt.ylabel('Total bill')
for i in ax.containers:
    ax.bar_label(i,fontsize=9)
st.pyplot(fig)

st.write("""
Общая выручка ресторана
""")

fig,ax=plt.subplots()
sns.histplot(tips['total_bill'], color='#914d6e')
plt.xlabel('Общий счет')
plt.ylabel('Сумма')
st.pyplot(fig)

