
# PyAcademy - VChu

Observed Trend 1: School spending per student has a negative impact on overall performance - more analysis should be considered
Observed Trend 2: When assessing how school size contributes to overall math and reading performance, Small(>1000 students) and Medium (1000-2000 students) schools tend to perform the same, however larger schools of 2000-5000 students have on average poorer performance than their Small and Medium School counterparts.
Observed Trend 3: Charter schools generally perform better overall in reading and math than district schools


```python
import os
import pandas as pd
```


```python
schools_csv = 'schools_complete.csv'
students_csv = 'students_complete.csv'
schools_df = pd.read_csv(schools_csv)
students_df = pd.read_csv(students_csv)
```


```python
schools_df = schools_df.rename(columns = {
    "name" : "School Name",
    "type" : "School Type"
})
students_df = students_df.rename(columns = {
    "name" : "Student Name",
    "school": "School Name"
})
pyschool_df = pd.merge(schools_df, students_df, on = "School Name")
```

# District Summary


```python
print ("District Summary")
pyschool_df["reading_score"] = pyschool_df["reading_score"].astype(float)
pyschool_df["math_score"] = pyschool_df["math_score"].astype(float)
pyschool_df["size"] = pyschool_df["size"].astype(float)
pyschool_df["budget"] = pyschool_df["budget"].astype(float)
pyschool_df.dtypes
```

    District Summary
    




    School ID          int64
    School Name       object
    School Type       object
    size             float64
    budget           float64
    Student ID         int64
    Student Name      object
    gender            object
    grade             object
    reading_score    float64
    math_score       float64
    dtype: object




```python
#Calculate Overall Summary totals
#Total Schools
totalschool = len(schools_df["School Name"].unique())
totalstudent = len(students_df["Student Name"].unique())
totalbudget = schools_df["budget"].sum()
avgmath = students_df["math_score"].mean()
avgread = students_df["reading_score"].mean()
mathpass = students_df.loc[(students_df["math_score"] >=60)]
mathpct = totalstudent / (len(mathpass)) *100
readpass = students_df.loc[(students_df["reading_score"]>=60)]
readpct = totalstudent / (len(readpass)) *100
overallpass = (readpct + mathpct)/2
```


```python
districtsummary_df = pd.DataFrame({"Total Schools": [totalschool],
                                  "Total students": [totalstudent],
                                  "Total budget": [totalbudget],
                                  "Average Math Score": [avgmath],
                                  "Average Read Score": [avgread],
                                  "% Passing Math": [mathpct],
                                  "% Passing Reading":[readpct],
                                  "Overall Passing Rate": [overallpass]
                                  })
districtsummary_df = districtsummary_df.round(2)
districtsummary_df =[["Total Schools", "Total students", "Total budget", "Average Math Score", "% Passing Math", "Average Read Score", "% Passing Reading", "Overall Passing Rate"]]
districtsummary_df
```




    [['Total Schools',
      'Total students',
      'Total budget',
      'Average Math Score',
      '% Passing Math',
      'Average Read Score',
      '% Passing Reading',
      'Overall Passing Rate']]



# School Summary


```python
school_totalstud = pyschool_df.groupby("School Name")["Student Name"].count()
school_type = pyschool_df.groupby("School Name")["School Type"].unique().str.get(0)
school_budgetsum = pyschool_df.groupby("School Name")["budget"].unique().str.get(0)
school_budgetperstud = (school_budgetsum/school_totalstud)
school_avgmath = pyschool_df.groupby("School Name")["math_score"].mean()
school_avgread = pyschool_df.groupby("School Name")["reading_score"].mean()
school_mathpass = pyschool_df.loc[(students_df["math_score"]>=70)].groupby("School Name").count()
school_pctmathpass = ((school_mathpass["math_score"]/school_totalstud)*100)
school_readpass = pyschool_df.loc[(students_df["reading_score"]>=70)].groupby("School Name").count()
school_pctreadpass = ((school_readpass["reading_score"]/school_totalstud)*100)
school_overallpass = (school_pctreadpass+school_pctmathpass)/2
```


```python
schoolsummary_df =pd.DataFrame({"Total students": school_totalstud,
                               "School Type":school_type,
                               "Total Budget": school_budgetsum,
                                "Total Budget/Student" : school_budgetperstud,
                                "Average Math Score": school_avgmath,
                                "% Passing Math": school_pctmathpass,
                                "Average Reading Score" : school_avgread,
                                "% Passing Reading": school_pctreadpass,
                                "Overall Passing Score": school_overallpass
                               })
schoolsummary_df = schoolsummary_df.round(0)
schoolsummary_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Score</th>
      <th>School Type</th>
      <th>Total Budget</th>
      <th>Total Budget/Student</th>
      <th>Total students</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>67.0</td>
      <td>82.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
      <td>District</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>94.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>96.0</td>
      <td>Charter</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>66.0</td>
      <td>81.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>73.0</td>
      <td>District</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>68.0</td>
      <td>79.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
      <td>District</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>93.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
      <td>Charter</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>1468</td>
    </tr>
  </tbody>
</table>
</div>



# Top Performing School (by Passing Rate)


```python
#Top Performing Schools (By Passing Rate)
topschools_df = schoolsummary_df.sort_values(by="Overall Passing Score", ascending=False)
topschools_df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Score</th>
      <th>School Type</th>
      <th>Total Budget</th>
      <th>Total Budget/Student</th>
      <th>Total students</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>94.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>96.0</td>
      <td>Charter</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>93.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
      <td>Charter</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>95.0</td>
      <td>96.0</td>
      <td>84.0</td>
      <td>84.0</td>
      <td>95.0</td>
      <td>Charter</td>
      <td>585858.0</td>
      <td>609.0</td>
      <td>962</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>94.0</td>
      <td>96.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
      <td>Charter</td>
      <td>1056600.0</td>
      <td>600.0</td>
      <td>1761</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>93.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
      <td>Charter</td>
      <td>1043130.0</td>
      <td>638.0</td>
      <td>1635</td>
    </tr>
  </tbody>
</table>
</div>



# Bottom Performing School (By Passing Rate)


```python
#Bottom performing School by passing rate
bottomschool_df = schoolsummary_df.sort_values(by="Overall Passing Score")
bottomschool_df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Score</th>
      <th>School Type</th>
      <th>Total Budget</th>
      <th>Total Budget/Student</th>
      <th>Total students</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Figueroa High School</th>
      <td>66.0</td>
      <td>81.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>73.0</td>
      <td>District</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>66.0</td>
      <td>80.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>73.0</td>
      <td>District</td>
      <td>2547363.0</td>
      <td>637.0</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>67.0</td>
      <td>82.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
      <td>District</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>68.0</td>
      <td>79.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
      <td>District</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>67.0</td>
      <td>81.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
      <td>District</td>
      <td>3022020.0</td>
      <td>652.0</td>
      <td>4635</td>
    </tr>
  </tbody>
</table>
</div>



# Math Scores by Grade


```python
#Math Scores by Grade
math_grade_df=pyschool_df[["School Name", "grade","math_score"]]
mathbygrade=math_grade_df.groupby(["School Name","grade"])["math_score"].mean()
mathbygrade = mathbygrade.round()
mathbygrade.unstack().head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.0</td>
      <td>78.0</td>
      <td>76.0</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.0</td>
      <td>83.0</td>
      <td>83.0</td>
      <td>83.0</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>77.0</td>
      <td>77.0</td>
      <td>77.0</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>78.0</td>
      <td>77.0</td>
      <td>76.0</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.0</td>
      <td>84.0</td>
      <td>83.0</td>
      <td>82.0</td>
    </tr>
  </tbody>
</table>
</div>



# Reading Score by Grade


```python
#Reading Score by Grade
read_grade_df=pyschool_df[["School Name", "grade","reading_score"]]
readbygrade=read_grade_df.groupby(["School Name","grade"])["reading_score"].mean()
readbygrade=readbygrade.round()
readbygrade.unstack().head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.0</td>
      <td>81.0</td>
      <td>81.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.0</td>
      <td>84.0</td>
      <td>84.0</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.0</td>
      <td>81.0</td>
      <td>81.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.0</td>
      <td>80.0</td>
      <td>81.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.0</td>
      <td>84.0</td>
      <td>84.0</td>
      <td>83.0</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Spending


```python
#scorbyspend_df=schoolsummary_df[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", 
                                # "Overall Passing Score"]]
#scorbyspend_df["Total Budget/Student"]= pd.cut(schoolsummary_df["Total Budget/Student"], bins, labels=groupname)
bins = [550,600,650,700]
groupname = ["\$550-\$600", "\$600-\$650", "\$650-\$700"]
```


```python
scorespend=pd.cut(schoolsummary_df["Total Budget/Student"], bins, labels=groupname)
scorespend_df = pd.DataFrame({ "Average Math Score": school_avgmath,
                                "% Passing Math": school_pctmathpass,
                                "Average Reading Score" : school_avgread,
                                "% Passing Reading": school_pctreadpass,
                                "Overall Passing Score": school_overallpass,
                                "Spending": scorespend})
scorespend_df.reset_index().drop("School Name",1)
spendingbins_df=scorespend_df.groupby("Spending").mean()
spendingbins_df.round()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Score</th>
    </tr>
    <tr>
      <th>Spending</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>\$550-\$600</th>
      <td>94.0</td>
      <td>96.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>\$600-\$650</th>
      <td>77.0</td>
      <td>87.0</td>
      <td>79.0</td>
      <td>82.0</td>
      <td>82.0</td>
    </tr>
    <tr>
      <th>\$650-\$700</th>
      <td>66.0</td>
      <td>81.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Size


```python
bins = [0, 1000, 2000, 5000]
sizegroup =["Small (<1000)", "Medium (1000-2000)", "Large(2000-5000)"]
```


```python
scores = pd.cut(schoolsummary_df["Total students"], bins, labels = sizegroup)
scores_df =pd.DataFrame({"Average Math Score": school_avgmath,
                                "% Passing Math": school_pctmathpass,
                                "Average Reading Score" : school_avgread,
                                "% Passing Reading": school_pctreadpass,
                                "Overall Passing Score": school_overallpass,
                                "School Size": scores
                             })
scores_df.reset_index().drop("School Name", 1)
scorebysize_df=scores_df.groupby("School Size").mean()
scorebysize_df.round()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Score</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1000)</th>
      <td>94.0</td>
      <td>96.0</td>
      <td>84.0</td>
      <td>84.0</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>Medium (1000-2000)</th>
      <td>94.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>Large(2000-5000)</th>
      <td>70.0</td>
      <td>83.0</td>
      <td>78.0</td>
      <td>81.0</td>
      <td>76.0</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Type


```python
types_df = pd.DataFrame({"Average Math Score": school_avgmath,
                                "% Passing Math": school_pctmathpass,
                                "Average Reading Score" : school_avgread,
                                "% Passing Reading": school_pctreadpass,
                                "Overall Passing Score": school_overallpass,
                                 "School Type" : school_type
                             })
types_df.reset_index().drop("School Name",1)
scorebytype_df=types_df.groupby("School Type").mean()
scorebytype_df.round()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Score</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>94.0</td>
      <td>97.0</td>
      <td>83.0</td>
      <td>84.0</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>District</th>
      <td>67.0</td>
      <td>81.0</td>
      <td>77.0</td>
      <td>81.0</td>
      <td>74.0</td>
    </tr>
  </tbody>
</table>
</div>


