🚢 Titanic Dataset – Data Cleaning & Exploratory Data Analysis (EDA)
This project demonstrates data cleaning and exploratory data analysis (EDA) on the Titanic dataset from Kaggle. The goal is to explore relationships between variables and identify patterns and trends that influence passenger survival.

📌 Objectives
Load and inspect the Titanic dataset

Clean missing, irrelevant, or inconsistent data

Perform univariate and bivariate analysis

Visualize relationships using plots

Identify meaningful insights and survival patterns

📊 Dataset Overview
The dataset contains information about passengers aboard the RMS Titanic, including:

Demographics (e.g., Age, Sex)

Class and Fare (e.g., Pclass, Fare)

Travel details (e.g., Embarked, SibSp)

Survival status (0 = did not survive, 1 = survived)

🧹 Data Cleaning Steps
Dropped irrelevant columns: PassengerId, Name, Ticket, Cabin

Filled missing values in Age (median) and Embarked (mode)

Converted Pclass, Sex, and Embarked to categorical types for analysis

📈 EDA Highlights
Univariate analysis: Distribution of Age, Fare, Survived, etc.

Bivariate analysis: Survival rates by Sex, Pclass, Embarked, etc.

Boxplots & heatmaps: Identify outliers and variable correlations

Crosstab summaries: Survival percentages by category

📷 Sample Visualizations
Count plot of survival status

Histogram of age distribution

Survival rate comparison by gender and class

Correlation heatmap of numerical features

💡 Key Insights
Women and children had higher survival rates than men.

First-class passengers were more likely to survive.

Embarked location showed a slight variation in survival trends.

Fare showed a weak positive correlation with survival.

🛠 Requirements
bash
Copy
Edit
pip install pandas matplotlib seaborn
🚀 How to Run
bash
Copy
Edit
python titanic_eda.py
Or use a Jupyter Notebook for interactive exploration.

📁 Dataset Source
🔗 Kaggle Titanic Competition

📄 License
This project is open-source and available under the MIT License.











Ask ChatGPT

