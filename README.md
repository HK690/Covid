# 🦠 COVID-19 India Data Analysis & Visualization

This project performs **Exploratory Data Analysis (EDA)** on COVID-19 cases and vaccination data in India using **Python**. It analyzes confirmed cases, recoveries, deaths, active cases, and vaccination statistics while creating visualizations to better understand the spread and impact of COVID-19 across different states.

---

# 📖 Project Overview

The objective of this project is to analyze publicly available COVID-19 datasets to gain insights into:

* Total confirmed COVID-19 cases
* Active cases across Indian states
* Recovery and mortality rates
* Most affected states
* Vaccination statistics
* Gender-wise vaccination distribution

The project uses Python data analysis and visualization libraries to clean, process, and visualize the data.

---

# ✨ Features

* 📊 Data Cleaning and Preprocessing
* 📅 Date Formatting and Time-Series Analysis
* 🦠 Active Case Calculation
* 📈 Recovery Rate Calculation
* ⚠️ Mortality Rate Calculation
* 📍 State-wise COVID Analysis
* 📉 Top 10 Most Affected States Visualization
* 📈 COVID Trend Analysis for Major States
* 💉 Vaccination Data Analysis
* 👨 Male vs 👩 Female Vaccination Distribution
* 📊 Interactive Pie Chart using Plotly

---

# 🛠️ Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

---

# 📂 Project Structure

```text
COVID-19-India-Analysis/
│
├── covid_analysis.ipynb (or main.py)
├── covid_data.csv
├── vaccination_data.csv
├── README.md
```

---

# 📥 Installation

Clone the repository:

```bash
git clone https://github.com/HK690/COVID.git
cd COVID-19-India-Analysis
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly
```

---

# 📁 Dataset

This project uses two datasets:

### COVID-19 Cases Dataset

Contains:

* Date
* State/Union Territory
* Confirmed Cases
* Deaths
* Recoveries

### Vaccination Dataset

Contains:

* Vaccination Date
* State
* Total Vaccinations
* Male Vaccinated
* Female Vaccinated
* Other Vaccination Statistics

Replace the file paths in the code:

```python
covid_df = pd.read_csv("path/to/covid_data.csv")
vaccine_df = pd.read_csv("path/to/vaccination_data.csv")
```

---

# ▶️ Running the Project

Run the Python script:

```bash
python main.py
```

or open the notebook:

```bash
jupyter notebook
```

---

# 📊 Data Processing

The project performs the following preprocessing steps:

* Removes unnecessary columns
* Converts dates into datetime format
* Calculates active COVID-19 cases
* Creates state-wise pivot tables
* Computes:

  * Recovery Rate
  * Mortality Rate
* Cleans vaccination data
* Removes unnecessary vaccination columns

---

# 📈 Visualizations

The project generates several visualizations, including:

### 📍 Top 10 States with Highest Active Cases

A Seaborn bar chart showing the states with the highest number of active COVID-19 cases.

---

### 📉 COVID-19 Trend of Top States

A line chart comparing active cases over time for major affected states.

---

### 💉 Gender-wise Vaccination Distribution

An interactive Plotly pie chart displaying the proportion of vaccinated males and females.

---

# 📊 Metrics Calculated

* Total Confirmed Cases
* Total Deaths
* Total Recoveries
* Active Cases
* Recovery Rate (%)
* Mortality Rate (%)
* Gender-wise Vaccination Count

---

# 📌 Learning Outcomes

This project demonstrates practical knowledge of:

* Exploratory Data Analysis (EDA)
* Data Cleaning
* Data Visualization
* Time-Series Analysis
* Statistical Analysis
* Pandas Data Manipulation
* Plotly Interactive Charts
* Seaborn & Matplotlib Visualization

---

# 🔮 Future Improvements

* Add a dashboard using Streamlit or Dash.
* Include district-level COVID analysis.
* Add forecasting using Machine Learning models.
* Create interactive filters for states and dates.
* Deploy the project as a web application.
* Integrate live COVID-19 APIs for real-time updates.

---

# 📄 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Developed by **Harshal Kapse**.
