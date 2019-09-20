#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os 
import csv


# In[17]:


pybank = os.path.join ("Resources/budget_data.csv")


# In[18]:


month_c = 0
total_r = 0
this_month_r = 0
last_month_r = 0
revenue_c = []
months = []
revenue_changes = []


# In[19]:


with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        month_c = month_c + 1
        months.append(row[0])
        this_month_r = int(row[1])
        total_r = total_r + this_month_r
        if month_c > 1:
            revenue_c = this_month_r - last_month_r
            revenue_changes.append(revenue_c)
            last_month_r = this_month_r


# In[22]:


sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_c - 1)
max_change = min(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(max_change)
max_month = months[max_month_index]
min_month = months[min_month_index]


# In[23]:


print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {month_c}")
print(f"Total : ${total_r}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase In Profits: {max_month} (${max_month})")
print(f"Greatest Decrease In Profits: {min_month} (${min_month})")
      
      


# In[ ]:




