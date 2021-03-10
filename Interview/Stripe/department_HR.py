'''
employee_info
{
    "id": "10"
    "first_name":"Marie_inn"
    "last_name":""
    "email":""
    "gender":""
    "age":""
    "salary":""
    "job_title":""}
'''
import pandas as pd
from csv import DictReader
employee_info = []
with open("employee.csv", newline="") as f:
    reader = DictReader()
    for row in reader:
        row["age"] = int(row["age"])
        row("salary") =  float(row["salary"])
        employee_info.append(row)
'''Task1: Unique Number of Job Titles'''
columns = employee_info[0].keys()
employee_frame = pd.DataFrame.from_records(employee_info, columns=columns)
print(f"Number of Unique Job Titles: {employee_frame.job_title.value_counts().count()}")

'''
Use a Pivot Table to Determine the Salary Difference Depending on Gender
'''

#To determine the average pay difference between men and women with the same job title, we'll first need to determine which jobs have both men and women doing them:
job_title_unique_gender_count = employee_frame.groupby('job_title')['gender'].nunique()
job_titles_with_two_genders = job_title_unique_gender_count.where(job_title_unique_gender_count == 2).dropna().index
job_title_gender_frame = employee_frame[employee_frame.job_title.isin(job_titles_with_two_genders)]

'''The last bit of code we use creates a column for each gender in our table, and also adds a column to the table to hold the pay difference between female and male employees:
'''
gender_difference_table = pd.pivot_table(job_title_gender_frame, columns='gender', values=['salary'], index=['job_title'])
gender_difference_table[('salary', 'difference')] = gender_difference_table[('salary', 'Female')] - gender_difference_table[('salary', 'Male')]
print(gender_difference_table)

'''Task 3'''
employee_frame['age_range'] = pd.cut(employee_frame.age, [18, 41, 80], labels=['18 - 40', '41 - 80'])
employee_frame.age_range.cat.add_categories(['difference'], inplace=True)

'''Next, we need to determine while job titles have at least one employee from each of the age ranges:
'''

job_title_unique_age_range_count = employee_frame.groupby('job_title')['age_range'].nunique()
job_titles_with_two_age_ranges = job_title_unique_age_range_count.where(job_title_unique_age_range_count == 2).dropna().index
job_title_age_range_frame = employee_frame[employee_frame.job_title.isin(job_titles_with_two_age_ranges)]

'''Now that we have a new data frame, we're ready to create our pivot table and populate a new difference column:
'''

age_difference_table = pd.pivot_table(job_title_age_range_frame, columns='age_range', values=['salary'], index=['job_title'])
age_difference_table[('salary', 'difference')] = age_difference_table[('salary', '18 - 40')] - age_difference_table[('salary', '41 - 80')]
print(age_difference_table)