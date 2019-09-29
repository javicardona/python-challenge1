#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# In[18]:


school_df = pd.read_csv(school_data_to_load, dtype={'School ID' : int,
                                                    'name' : object,
                                                    'type' : object,
                                                    'size' : int,
                                                    'budget' : int})


# In[20]:


school_df.head()


# In[69]:


student_df = pd.read_csv(student_data_to_load, dtype={'School_ID' : int,
                                                      'name' : object,
                                                      'gender' : object,
                                                      'grade' : object,
                                                      'school' : object,
                                                      'reading_score' : int,
                                                      'math_score' : int})
                                                 


# In[70]:


student_df.head()


# In[71]:


total_students = student_data["student_name"].count()
total_students


# In[72]:


school_data["school_name"].count()


# In[73]:


student_data["student_name"].count()


# In[74]:


school_data["budget"].sum()


# In[75]:


student_data["math_score"].mean()


# In[76]:


student_passing_reading = student_df.loc[student_df["reading_score"] > 70, :].count()
student_passing_reading["Student ID"]


# In[77]:


student_passing_reading["Student ID"] / total_students


# In[44]:


student_passing_reading


# In[90]:


percent_passing_reading = student_passing_reading["Student ID"] / total_students * 100
percent_passing_reading


# In[91]:


student_passing_math = student_df.loc[student_df["math_score"] > 70, :].count()
student_passing_math["Student ID"]


# In[92]:


percent_passing_math = student_passing_math["Student ID"] / total_students *100
percent_passing_math


# In[95]:


overall_passing_rate = (percent_passing_math + percent_passing_reading)/ 2
overall_passing_rate


# In[180]:


total_schools = student_data["school_name"]
total_students


# In[179]:


total_budget = school_data["budget"]
total_budget


# In[177]:





# In[178]:


school_summary_df = pd.DataFrame(
     {'total schools' : total_schools,
      'Total students' : total_students,
      'total budget' : total_budget,
      'per_student-budget' :per_student_budget
      '%passing math' : percent_passing_math,
      '%passing reading' : percent_passing_reading,
      'over all passing rate' : overall_passing_rate
        
    },
)
school_summary_df.head()


# In[159]:


school_summary_df.shape


# In[170]:


top_five = school_summary_df.sort_values("over all passing rate", ascending=False)
top_five.head()


# In[172]:


bottom_five = school_summary_df.sort_values("over all passing rate").iloc[0:5]
top_five.tail()


# In[123]:


grade_9 = student_df.loc[student_df['grade']=='9th']
grade_10 = student_df.loc[student_df['grade']=='10th']
grade_11 = student_df.loc[student_df['grade']=='11th']
grade_12 = student_df.loc[student_df['grade']=='12th']


# In[124]:


grade_9_scount = grade_9.groupby('school_name')['grade'].count()
grade_10_scount = grade_10.groupby('school_name')['grade'].count()
grade_11_scount = grade_11.groupby('school_name')['grade'].count()
grade_12_scount = grade_12.groupby('school_name')['grade'].count()


# In[127]:


grade_9_math = grade_9.groupby('school_name')['math_score'].sum()/ grade_9_scount
grade_10_math = grade_10.groupby('school_name')['math_score'].sum()/ grade_10_scount
grade_11_math = grade_11.groupby('school_name')['math_score'].sum()/ grade_11_scount
grade_12_math = grade_12.groupby('school_name')['math_score'].sum()/ grade_12_scount


# In[129]:


math_by_grade = pd.concat([grade_9_math,
                           grade_10_math,
                           grade_11_math,
                           grade_12_math],
                          axis =1)


# In[130]:


math_by_grade = math_by_grade.rename(columns={0:'9th', 1:'10th', 2:'11th', 3:'12th'})
math_by_grade


# In[154]:


grade_9_reading = grade_9.groupby('school_name')['reading_score'].sum()/ grade_9_scount
grade_10_reading = grade_10.groupby('school_name')['reading_score'].sum()/ grade_10_scount
grade_11_reading = grade_11.groupby('school_name')['reading_score'].sum()/ grade_11_scount
grade_12_reading = grade_12.groupby('school_name')['reading_score'].sum()/ grade_12_scount


# In[155]:


reading_by_grade = pd.concat([grade_9_reading,
                           grade_10_reading,
                           grade_11_reading,
                           grade_12_reading],
                          axis =1)


# In[156]:


reading_by_grade = reading_by_grade.rename(columns={0:'9th', 1:'10th', 2:'11th', 3:'12th'})
reading_by_grade


# In[186]:


schoolby_spending_df = school_df
studentsby_spending_df = student_df


# In[196]:


schoolby_spending_df["per student budget"] = schoolby_spending_df ["budget"]/ schoolby_spending_df["size"]
schoolby_spending_df.head()


# In[193]:


bin_list = [0,585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]

schoolby_spending_df["spending ranges (per student)"] = pd.cut(schoolby_spending_df["per student budget"],bin_list,)


# In[198]:


studentsby_spending_df = studentsby_spending_df.merge(schoolby_spending_df)


# In[203]:





# In[ ]:




