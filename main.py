import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime

# Load COVID dataset
covid_df = pd.read_csv('filepath/filename.csv')

# Explore dataset
covid_df.head()
covid_df.info()
covid_df.describe()

# Load Vaccination dataset
vaccine_df = pd.read_csv('filepath/filename.csv')

vaccine_df.head()
vaccine_df.info()

# Drop unnecessary columns
covid_df.drop(
    ["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"],
    inplace=True,
    axis=1
)

# Convert Date column to datetime format
covid_df['Date'] = pd.to_datetime(
    covid_df['Date'],
    format="%Y-%m-%d"
)

covid_df.head(7)

# Calculate Active Cases
covid_df['Active_cases'] = (
    covid_df['Confirmed']
    - (covid_df['Cured'] + covid_df['Deaths'])
)

covid_df.tail()

# State-wise analysis
statewise = pd.pivot_table(
    covid_df,
    values=["Confirmed", "Deaths", "Cured"],
    index="State/UnionTerritory",
    aggfunc=max
)

statewise

# Recovery and Mortality Rate
statewise["Recovery_rate"] = (
    statewise["Cured"] * 100 / statewise["Confirmed"]
)

statewise["Mortality_rate"] = (
    statewise["Deaths"] * 100 / statewise["Confirmed"]
)

statewise.sort_values(by="Confirmed", ascending=False)

# Gradient styling
statewise.style.background_gradient(cmap="cubehelix")

# Top 10 Active Cases
top_10_active_cases = (
    covid_df.groupby(by='State/UnionTerritory')
    .max()[['Active_cases', 'Date']]
    .sort_values(by=['Active_cases'], ascending=False)
    .reset_index()
)

top_10_active_cases

# Bar Plot
ax = sns.barplot(
    data=top_10_active_cases.iloc[:10],
    y="Active_cases",
    x="State/UnionTerritory",
    linewidth=2,
    edgecolor='red'
)

# Recalculate Top 10
top_10_active_cases = (
    covid_df.groupby(by='State/UnionTerritory')
    .max()[['Active_cases', 'Date']]
    .sort_values(by=['Active_cases'], ascending=False)
    .reset_index()
)

# Plot Figure
fig = plt.figure(figsize=(10, 5))
plt.title("Top 10 States with most no. of Cases", size=15)

ax = sns.barplot(
    data=top_10_active_cases.iloc[:10],
    y="Active_cases",
    x="State/UnionTerritory",
    linewidth=2,
    edgecolor='red'
)

# Line Plot for Top 5 States
fig = plt.figure(figsize=(10, 5))

ax = sns.lineplot(
    data=covid_df[
        covid_df['State/UnionTerritory'].isin([
            'Maharasthra',
            'Karnataka',
            'Kerala',
            'Tamil Nadu',
            'Uttar Pradesh'
        ])
    ],
    x='Date',
    y='Active_cases',
    hue='State/UnionTerritory'
)

ax.set_title('Top 5 most affected States', size=10)

# Vaccination Dataset
vaccine_df.head()

# Rename Column
vaccine_df.rename(
    columns={'Updated On': 'Vaccine_Date'},
    inplace=True
)

vaccine_df.head()
vaccine_df.info()

# Check Missing Values
vaccine_df.isnull().sum()

# Remove unnecessary columns
vaccination = vaccine_df.drop(
    columns=[
        'Sputnik V (Doses Administered)',
        'AEFI',
        '18-44 Years (Doses Administered)',
        '45-60 Years (Doses Administered)',
        '60+ Years (Doses Administered)'
    ],
    axis=1
)

vaccination.head()

# Total Vaccinated by Gender
male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()

# Pie Chart
px.pie(
    names=["Male", "Female"],
    values=[male, female],
    title="Males and Females Vaccination"
)
