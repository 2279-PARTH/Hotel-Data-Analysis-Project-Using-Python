#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("C:\\Users\\Administrator\\Downloads\\hotel_booking.csv\\hotel_booking (Autosaved).csv")


# In[4]:


df


# In[5]:


df.isnull().sum()


# In[6]:


df.nunique()


# In[7]:


df.dropna()


# In[8]:


df.isnull().sum()


# In[9]:


df.info()


# In[10]:


df.dropna(inplace=True)


# In[11]:


df.info()


# In[12]:


df.isnull().sum()


# In[13]:


df.shape


# In[14]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[206]:


total_booking=df['is_canceled'].sum


# # Total_booking

# In[ ]:


We can see that there are total 118898 booking in 3 years which is 2015,2016,2017


# In[201]:


Total_cancellation=df['is_canceled'].sum()


# # Total_cancellation

# In[ ]:


From above we can see that in last 3 years there have 44153 cancellation


# # Types of Hotel

# In[67]:


a= sns.countplot(x='hotel',data=df)
sns.set(rc={'figure.figsize':(15,5)})
for bars in a.containers:
    a.bar_label(bars)

This are types of hotel we have by looking we can see that city hotel are higher in number compare to resort hotel 
# # Cancellation on Basis of hotel

# In[68]:


hotel_cancellation=df.groupby(['hotel'],as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=True)


# In[86]:


a5=sns.barplot(x='hotel',y='is_canceled',data=hotel_cancellation)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a5.containers:
    a5.bar_label(bars)

So that's why there are more cancellation in city hotel than resort hotel
Cancellation rate of Resort Hotel=28%
Cancellation rate of City Hotel=41%
# # Cancellation on basis of room status

# In[98]:


a1= sns.countplot(x='roomt_status',data=df)
sns.set(rc={'figure.figsize':(15,5)})
for bars in a1.containers:
    a1.bar_label(bars)

Above graph is about desired and undesired room if customer is assigned the same what he ask for it is included in category
of desired room or else it is included in category of undesired room
# In[89]:


df.groupby(['roomt_status'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=False)


# In[92]:


preferance_cancellation=df.groupby(['roomt_status'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=False)
a2=sns.barplot(x='roomt_status',y='is_canceled',data=preferance_cancellation)
sns.set(rc={'figure.figsize':(10,5)})
for bars in a2.containers:
    a2.bar_label(bars)

We can see there is very little effect on basic of roomt_status(room type status) on cancellation of our hotels
cancellation rate of desired room is around 41%
cancellation rate of undesired room is around 5%
but as we need to decrease our cancellation rate even though undesired 5% is less but 
we can try to give best customer service to our customers if we are giving them undesired room atleast 
we can give them some benifits to improve their satisfaction rate which will help us grow and we need make sure there is no 
overbooking which creates this problem a few times

# # Cancellation on Basis of guest type

# In[50]:


total_guest=df['guest_type'].value_counts()


# In[53]:


total_guest


# In[218]:


a6=sns.countplot(x='guest_type',data=df)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a6.containers:
    a6.bar_label(bars)

Most of our guest are couples then singles and lastly family 
From this data we can try to increase guest by seeking feedback of scope of improve which helps us
# In[18]:


df.groupby(['guest_type'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=False)


# In[219]:


cancellation_by= df.groupby(['guest_type'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=False)
a2=sns.barplot(x='guest_type',y='is_canceled',data=cancellation_by)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a2.containers:
    a2.bar_label(bars)

Cancellation of Couples 39%
Cancellation of single 29%
Cancellation of Family 34%
More booking which means more cancellation 
# In[ ]:





# # Cancellation on basis of month

# In[115]:


guest_per_month=df['arrival_date_month'].value_counts().sort_values(ascending=True)


# In[104]:


guest_per_month


# In[307]:


a7= sns.countplot(x='arrival_date_month',data=df)
sns.set(rc={'figure.figsize':(13,5)})
for bars in a7.containers:
    a7.bar_label(bars)

From above data we can see that top 3 booking are on the month 
1)August
2)July 
3)May
On a average 9,900 bookings are done per month
# In[ ]:


df


# In[111]:


df.groupby(['arrival_date_month'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=True)


# In[235]:


cancel_month=df.groupby(['arrival_date_month'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=True)


# In[304]:


a5=sns.barplot(x='arrival_date_month',y='is_canceled',data=cancel_month)
sns.set(rc={'figure.figsize':(10,5)})
for bars in a5.containers:
    a5.bar_label(bars)

Jan 30%
Feb 33%
mar 32%
april 40%
may 39
june 41
july 37%
aug 37%
sept 39%
oct 38
nov 31
dec 35
From above data we can see that top 3 booking cancellation rate in the month
1)June -41%
2)April -40%
3)May -39%
On an average there are 3,679 cancellation per month
# In[183]:


a1= sns.countplot(x='customer_type',data=df)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a1.containers:
    a1.bar_label(bars)


# # On basis of years

# In[212]:


df['arrival_date_year'].value_counts()


# In[220]:


a9= sns.countplot(x='arrival_date_year',data=df)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a9.containers:
    a9.bar_label(bars)


# In[208]:


cancellation_by_year=df.groupby(['arrival_date_year'], as_index=False)['is_canceled'].sum().sort_values(by='is_canceled',ascending=True)


# In[209]:


cancellation_by_year


# In[221]:


a8=sns.barplot(x='arrival_date_year',y='is_canceled',data=cancellation_by_year)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a8.containers:
    a8.bar_label(bars)

From 2015 to 2016 there was increase in booking but there is also increase in cancellation rate
34% to 36% but more concerning thing is that booking were decreased from 2016 to 2017 but there was increase in the cancellation rate 36% to 39%
39,632 bookings per year
14,404 cancellation per year
To improve this thing we can 
(*)Flexible Booking Policies
1)Flexible Rates: Offer different rates for flexible and non-refundable bookings. This allows customers to choose based on their preference for flexibility.
2)Cancellation Windows: Implement and clearly communicate cancellation windows, such as free cancellation until a certain date before arrival.
# # Retention Rate

# In[310]:


a6=sns.countplot(x='is_repeated_guest',data=df)
sns.set(rc={'figure.figsize':(15,5)})
for bars in a6.containers:
    a6.bar_label(bars)

Retention rate is 3.2% which is very less over past three years
Customer retention is very less we can try to implement loyalty Programs
Incentives: Encourage repeat bookings by offering loyalty programs that provide benefits for non-cancellable bookings.
Rewards: Offer points, discounts, or exclusive benefits to loyal customers who book non-refundable rates.
# In[328]:


retention_rate=df.groupby(['arrival_date_year'], as_index=False)['is_repeated_guest'].sum().sort_values(by='is_repeated_guest',ascending=True)


# In[329]:


retention_rate


# # Retention on basis of year

# In[331]:


a10=sns.barplot(x='arrival_date_year',y='is_repeated_guest',data=retention_rate)
sns.set(rc={'figure.figsize':(15,5)})
for bars in a10.containers:
    a10.bar_label(bars)

2015 2.93%
2016 3.14%
2017 3.42%
There is progess in retention rate
# # Retention on basis of guest_type

# In[334]:


retentionf_rate=df.groupby(['guest_type'], as_index=False)['is_repeated_guest'].sum().sort_values(by='is_repeated_guest',ascending=True)


# In[335]:


retentionf_rate 


# In[338]:


a11=sns.barplot(x='guest_type',y='is_repeated_guest',data=retentionf_rate)
sns.set(rc={'figure.figsize':(5,5)})
for bars in a11.containers:
    a11.bar_label(bars)

Singles 10%
Couples 1.7%
Family 1.3%
# In[ ]:




