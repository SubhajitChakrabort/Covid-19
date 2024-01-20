#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[3]:


covid = pd.read_csv("C:\\Users\\SUBHAJIT\\Desktop\\My Document\\Study Document\\Projects\\Covid Data Analysis\\worldometer_data.csv")


# In[4]:


covid.head()


# In[5]:


covid = covid [['Country/Region', 'Population' , 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical']]


# In[6]:


covid.head()


# In[7]:


covid = covid.rename(columns = {'Country/Region':'Country', 'TotalCases':'Cases', 'TotalDeaths':'Deaths','TotalRecovered':'Recovered', 'ActiveCases':'Active', 'Serious,Critical':'RedZone' })


# In[8]:


covid.head()


# In[9]:


covid.tail()


# In[10]:


covid.shape


# In[20]:


latest_cases = covid.loc[covid['Country'] == 'India', 'Cases']


# In[21]:


latest_cases


# In[23]:


covid.columns


# In[40]:


covid.sort_values(by ='Cases', ascending = False)


# In[42]:


top5 = covid.sort_values(by ='Cases', ascending = False).head()


# In[43]:


top5


# In[48]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Cases", data = top5)
plt.show()


# In[49]:


covid.sort_values(by ='Cases', ascending = True)


# In[51]:


covid.sort_values(by ='Cases', ascending = True).head()


# In[52]:


bot5 = covid.sort_values(by ='Cases', ascending = True).head()


# In[53]:


bot5


# In[56]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Cases", data = bot5)
plt.show()


# In[57]:


covid.head()


# In[63]:


covid[['Country', 'Cases']].value_counts()


# In[64]:


covid[['Country', 'Cases']].value_counts().head()


# In[86]:


selected_countries = covid[covid['Country'].isin(['India', 'USA', 'Brazil', 'Russia', 'South Africa'])]


# In[87]:


cases_counts = selected_country['Deaths'].value_counts()


# In[89]:


cases_counts


# In[98]:


India = covid[covid['Country'] == 'India']


# In[99]:


India


# In[107]:


sns.barplot(x = "Country", y = "Cases", data = India)
plt.show()


# In[102]:


USA = covid[covid['Country'] == 'USA']


# In[103]:


USA


# In[110]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Cases", data = India)
sns.barplot(x = "Country", y = "Cases", data = USA)
plt.show()


# In[111]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Deaths", data = top5)
plt.show()


# In[112]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Deaths", data = bot5)
plt.show()


# In[114]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Recovered", data = top5)
plt.show()


# In[115]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Active", data = top5)
plt.show()


# In[116]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "RedZone", data = top5)
plt.show()


# In[122]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Deaths", y = "Recovered", data = top5)
plt.show()


# In[124]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Cases", y = "RedZone", data = top5)
plt.show()


# In[126]:


plt.figure(figsize=(10, 5))
sns.scatterplot(x="Active", y="Cases", data=top5)
plt.show()


# In[128]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5, hue="Cases")
plt.show()


# In[129]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5, hue="RedZone")
plt.show()


# In[130]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5, hue="Population")
plt.show()


# In[131]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5, hue="Recovered")
plt.show()


# In[137]:


plt.figure(figsize=(10, 5))
plt.pie(top5['Cases'], labels=top5['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Cases by Country')
plt.show()


# In[167]:


plt.figure(figsize=(10, 8))
plt.pie(top5['Active'], labels=top5['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Active by Country')
plt.show()


# In[141]:


plt.figure(figsize=(10, 15))
plt.pie(top5['Deaths'], labels=top5['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Deaths by Country')
plt.show()


# In[143]:


plt.figure(figsize=(10, 15))
plt.pie(top5['Deaths'], labels=top5['Recovered'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Deaths & recovered')
plt.show()


# In[148]:


plt.figure(figsize=(10, 15))
plt.pie(top5['Population'], labels=top5['Deaths'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Population by Deaths')
plt.show()


# In[149]:


covid.columns


# In[150]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Active", y = "RedZone", data = top5)
plt.show()


# In[151]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Active", y = "Recovered", data = top5)
plt.show()


# In[152]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5, hue="Deaths")
plt.show()


# In[153]:


covid1 = pd.read_csv("C:\\Users\\SUBHAJIT\\Desktop\\My Document\\Study Document\\Projects\\Covid Data Analysis\\country_wise_latest.csv")


# In[154]:


covid1


# In[155]:


covid1.head()


# In[156]:


covid1.tail()


# In[157]:


covid1.columns


# In[158]:


covid1 = covid1 [['Country/Region','Confirmed', 'New cases', 'Deaths', 'New recovered', 'Recovered', 'Active', 'Recovered / 100 Cases', 'Deaths / 100 Cases', 'Deaths / 100 Recovered', 'Confirmed last week','1 week change', '1 week % increase'  ]]


# In[159]:


covid1 = covid1.rename(columns = {'Country/Region':'Country',  })


# In[160]:


covid1.head()


# In[161]:


covid1.tail()


# In[162]:


covid1.shape


# In[163]:


covid1.columns


# In[169]:


covid1.sort_values(by ='New cases', ascending = False)


# In[170]:


covid1.sort_values(by ='New cases', ascending = True)


# In[205]:


top5_1 = covid1.sort_values(by ='New cases', ascending = False).head()
top5_1


# In[206]:


bot5_1 = covid1.sort_values(by ='New cases', ascending = False).tail()
bot5_1


# In[207]:


top5_1 = covid1.sort_values(by ='New cases', ascending = True).head()
top5_1


# In[208]:


bot5_1 = covid1.sort_values(by ='New cases', ascending = True).tail()
bot5_1


# In[209]:


top5_1 = covid1.sort_values(by ='Deaths', ascending = True).head()
top5_1


# In[210]:


top5_1 = covid1.sort_values(by ='Recovered', ascending = True).head()
top5_1


# In[211]:


top5_1 = covid1.sort_values(by ='Confirmed', ascending = True).head()
top5_1


# In[212]:


top5_1 = covid1.sort_values(by ='Active', ascending = True).head()
top5_1


# In[213]:


top5_1 = covid1.sort_values(by ='Recovered / 100 Cases', ascending = True).head()
top5_1


# In[214]:


top5_1 = covid1.sort_values(by ='Deaths / 100 Cases', ascending = True).head()
top5_1


# In[215]:


top5_1 = covid1.sort_values(by ='Deaths / 100 Recovered', ascending = True).head()
top5_1


# In[216]:


top5_1 = covid1.sort_values(by ='1 week % increase', ascending = True).head()
top5_1


# In[218]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Deaths", data = top5_1)
plt.show()


# In[219]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Country", y = "Deaths", data = bot5_1)
plt.show()


# In[221]:


covid1[['Country', 'New cases']].value_counts()


# In[222]:


covid1[['Country', 'New cases']].value_counts().head()


# In[223]:


covid1[['Country', 'Deaths']].value_counts()


# In[224]:


covid1[['Country', 'Deaths']].max()


# In[225]:


covid1[['Country', 'Deaths']].min()


# In[226]:


covid1[['Country', 'Deaths']].sum()


# In[229]:


overall_average_deaths = covid1['Deaths'].mean()


# In[230]:


overall_average_deaths


# In[235]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5_1, hue="Recovered")
plt.show()


# In[234]:


covid1.columns


# In[236]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5_1, hue="Recovered")
plt.show()


# In[237]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5_1, hue="New cases")
plt.show()


# In[238]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5_1, hue="Deaths")
plt.show()


# In[242]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Recovered / 100 Cases", data=top5_1, hue="Deaths / 100 Cases")
plt.show()


# In[243]:


plt.figure(figsize = (10, 5))
sns.barplot(x = "Deaths / 100 Recovered", y = "Deaths / 100 Cases", data = top5_1)
plt.show()


# In[248]:


plt.figure(figsize=(10, 5))
sns.countplot(x="Country", data=top5_1, hue="1 week % increase")
plt.show()


# In[246]:


covid1.columns


# In[251]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Country", y = "1 week % increase", data = bot5_1)
plt.show()


# In[252]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Country", y = "Recovered / 100 Cases", data = bot5_1)
plt.show()


# In[253]:


plt.figure(figsize = (10, 5))
sns.lineplot(x = "Deaths / 100 Recovered", y = "Recovered / 100 Cases", data = bot5_1)
plt.show()


# In[259]:


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Deaths / 100 Recovered'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Deaths / 100 Recovered')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['Recovered / 100 Cases'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Recovered / 100 Cases')
plt.show()


# In[265]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['1 week change'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('1 week change')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['1 week % increase'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('1 week % increase')
plt.show()


# In[266]:


covid1.columns


# In[267]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['New cases'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('New cases')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['New recovered'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('New recovered')
plt.show()


# In[269]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Country'].value_counts(), labels=bot5_1['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Countries')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['New recovered'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('New Recovered Distribution')
plt.show()


# In[277]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Country'].value_counts(), labels=bot5_1['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Countries')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['Recovered / 100 Cases'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Recovered / 100 Cases')
plt.show()


# In[276]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Country'].value_counts(), labels=bot5_1['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Countries')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['Deaths / 100 Cases'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Deaths / 100 Cases')
plt.show()


# In[282]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Country'].value_counts(), labels=bot5_1['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Countries')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['Deaths / 100 Recovered'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Deaths / 100 Recovered')
plt.show()


# In[283]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Country'].value_counts(), labels=bot5_1['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Countries')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['1 week % increase'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('1 week % increase')
plt.show()


# In[284]:


plt.figure(figsize=(10, 15))
plt.subplot(1, 2, 1)
plt.pie(bot5_1['Country'].value_counts(), labels=bot5_1['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Countries')
plt.subplot(1, 2, 2)
plt.pie(bot5_1['Confirmed'], labels=bot5_1['Country'], autopct='%1.1f%%', startangle=90)
plt.title('Confirmed')
plt.show()


# In[ ]:




