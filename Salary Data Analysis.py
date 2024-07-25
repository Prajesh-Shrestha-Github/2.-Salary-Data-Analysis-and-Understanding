#!/usr/bin/env python
# coding: utf-8

# # Data Preparation

# # ●	Write a python program to load data into pandas DataFrame 		

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('DataScienceSalaries.csv')
df


# # ●	Write a python program to remove unnecessary columns i.e., salary and salary currency.

# In[12]:


df.drop(columns=['salary','salary_currency'],inplace = True)

df


# # ●	Write a python program to remove the NaN missing values from updated dataframe. 	

# In[13]:


df.isnull().sum()


# ## if there was a null value:

# In[14]:


df.dropna()


# # ●	Write a python program to check duplicates value in the dataframe. 

# In[15]:


df[df.duplicated()]


# # ●	Write a python program to see the unique values from all the columns in the dataframe.

# In[16]:


for a in df.columns:
    print(df[a].unique())


# # ●	Rename the experience level columns as below.		
# SE – Senior Level/Expert, 
# MI – Medium Level/Intermediate, 
# EN – Entry Level, 
# EX – Executive Level	

# In[49]:


df['experience_level'].replace({'SE': 'Senior Level/Expert', 
                               'MI':'Medium Level/Intermediate',
                               'EN': 'Entry Level',
                               'EX': 'Executive Level'},inplace= True)
df


# # Data Cleaning

# In[19]:


job_title_consistency = {
    'Principal Data Scientist': 'Data Scientist',
    'ML Engineer': 'Machine Learning Engineer',
    'Applied Scientist': 'Research Scientist',
    'Data Modeler': 'Data Engineer',
    'Research Engineer': 'Research Scientist',
    'Analytics Engineer': 'Data Engineer',
    'Business Intelligence Engineer': 'BI Engineer',
    'Data Strategist': 'Data Analyst',
    'Computer Vision Engineer': 'Computer Vision Specialist',
    'Compliance Data Analyst': 'Data Analyst',
    'Applied Machine Learning Engineer': 'Machine Learning Engineer',
    'AI Developer': 'AI Engineer',
    'Data Analytics Manager': 'Analytics Manager',
    'Business Data Analyst': 'Data Analyst',
    'Applied Data Scientist': 'Data Scientist',
    'Staff Data Analyst': 'Data Analyst',
    'ETL Engineer': 'Data Engineer',
    'Data DevOps Engineer': 'DevOps Engineer',
    'Head of Data': 'Chief Data Officer',
    'Data Science Manager': 'Data Science Manager',
    'Data Manager': 'Data Manager',
    'Machine Learning Researcher': 'Research Scientist',
    'Big Data Engineer': 'Big Data Engineer',
    'Data Specialist': 'Data Analyst',
    'Lead Data Analyst': 'Senior Data Analyst',
    'BI Data Engineer': 'BI Engineer',
    'Director of Data Science': 'Director of Data Science',
    'Machine Learning Scientist': 'Research Scientist',
    'MLOps Engineer': 'DevOps Engineer',
    'AI Scientist': 'Research Scientist',
    'Autonomous Vehicle Technician': 'Vehicle Technician',
    'Applied Machine Learning Scientist': 'Research Scientist',
    'Lead Data Scientist': 'Senior Data Scientist',
    'Cloud Database Engineer': 'Cloud Engineer',
    'Financial Data Analyst': 'Data Analyst',
    'Data Infrastructure Engineer': 'Infrastructure Engineer',
    'Software Data Engineer': 'Software Engineer',
    'AI Programmer': 'AI Engineer',
    'Data Operations Engineer': 'Operations Engineer',
    'BI Developer': 'BI Engineer',
    'Data Science Lead': 'Data Science Manager',
    'Deep Learning Researcher': 'Research Scientist',
    'BI Analyst': 'BI Analyst',
    'Data Science Consultant': 'Data Scientist',
    'Data Analytics Specialist': 'Data Analyst',
    'Machine Learning Infrastructure Engineer': 'Infrastructure Engineer',
    'Head of Data Science': 'Chief Data Science Officer',
    'Insight Analyst': 'Data Analyst',
    'Deep Learning Engineer': 'Machine Learning Engineer',
    'Machine Learning Software Engineer': 'Software Engineer',
    'Big Data Architect': 'Big Data Architect',
    'Product Data Analyst': 'Data Analyst',
    'Computer Vision Software Engineer': 'Computer Vision Specialist',
    'Azure Data Engineer': 'Cloud Engineer',
    'Marketing Data Engineer': 'Marketing Analyst',
    'Data Analytics Lead': 'Senior Data Analyst',
    'Data Lead': 'Data Manager',
    'Data Science Engineer': 'Data Engineer',
    'Machine Learning Research Engineer': 'Research Engineer',
    'NLP Engineer': 'NLP Specialist',
    'Manager Data Management': 'Data Manager',
    'Machine Learning Developer': 'Machine Learning Engineer',
    '3D Computer Vision Researcher': 'Computer Vision Specialist',
    'Principal Machine Learning Engineer': 'Senior Machine Learning Engineer',
    'Data Analytics Engineer': 'Data Analyst',
    'Data Analytics Consultant': 'Data Analyst',
    'Data Management Specialist': 'Data Manager',
    'Data Science Tech Lead': 'Senior Data Scientist',
    'Data Scientist Lead': 'Senior Data Scientist',
    'Cloud Data Engineer': 'Cloud Engineer',
    'Data Operations Analyst': 'Operations Analyst',
    'Marketing Data Analyst': 'Marketing Analyst',
    'Power BI Developer': 'BI Engineer',
    'Product Data Scientist': 'Data Scientist',
    'Principal Data Architect': 'Senior Data Architect',
    'Machine Learning Manager': 'Machine Learning Manager',
    'Lead Machine Learning Engineer': 'Senior Machine Learning Engineer',
    'ETL Developer': 'Data Engineer',
    'Cloud Data Architect': 'Cloud Architect',
    'Lead Data Engineer': 'Senior Data Engineer',
    'Head of Machine Learning': 'Chief Machine Learning Officer',
    'Principal Data Analyst': 'Senior Data Analyst',
    'Principal Data Engineer': 'Senior Data Engineer',
    'Staff Data Scientist': 'Data Scientist',
    'Finance Data Analyst': 'Data Analyst'
}

df['job_title'] = df['job_title'].replace(job_title_consistency)

df


# In[69]:


df['job_title'].nunique()


# # Data Analysis

# # ●	Write a Python program to show summary statistics of sum, mean, standard deviation, skewness, and kurtosis of any chosen variable. 

# In[24]:


salary_sum = df.salary_in_usd.sum()

print(f"The sum of salary in USD is {salary_sum}")


# In[26]:


salary_mean = df.salary_in_usd.mean()

print(f"The mean of salary in USD is {salary_mean}")


# In[27]:


salary_std = df.salary_in_usd.std()

print(f"The standard deviation of salary in USD is {salary_std}")


# In[29]:


salary_skew = df.salary_in_usd.skew()

print(f"The skewness of salary in USD is {salary_skew}")


# In[30]:


salary_kurtosis = df.salary_in_usd.kurtosis()

print(f"The kurtosis of salary in USD is {salary_kurtosis}")


# # ●	Write a Python program to calculate and show correlation of all variables. 

# In[31]:


df.corr(numeric_only=True)


# # Data Exploration

# # ●	Write a python program to find out top 15 jobs. Make a bar graph of sales as well.         

# In[32]:


top_jobs = df['job_title'].value_counts().head(15)
print(top_jobs)


# In[38]:


top_jobs.plot(kind='bar', title= 'Top 15 Jobs on Value Count')
plt.xlabel('Jobs')
plt.ylabel('No. of Jobs')
plt.legend()


# # ●	Which job has the highest salaries? Illustrate with bar graph.	

# In[67]:


highest_salaries = df.groupby('job_title')['salary_in_usd'].max().sort_values(ascending=False)
a = highest_salaries.head(10)
print(f"The job titles with the highest salaries in USD are:")
print(a)


# In[68]:


a.plot(kind='bar', title='Job Titles with the Highest Salary')
plt.xlabel('Job Titles')
plt.ylabel('Salaries')
plt.legend()


# # ●	Write a python program to find out salaries based on experience level. Illustrate it through bar graph.	

# In[46]:


b = df.groupby('experience_level')['salary_in_usd'].max()

b


# In[48]:


b.plot(kind='bar', title = 'Salary based on Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Salaries')
plt.legend()


# # ●	Write a Python program to show histogram and box plot of any chosen different variables. Use proper labels in the graph.

# In[64]:


plt.hist(df['salary_in_usd'], label="")
plt.title("Histogram of Salary")


# In[66]:


plt.boxplot(df['work_year'])


# In[ ]:




