# 📊 Startup Funding in India Explorer — Documentation

---

## 1. Problem Statement

Startups in India have been receiving increasing amounts of funding across various sectors.  
The goal of this project is to explore and analyze startup funding trends based on sectors and visualize which industries are getting the highest investments.

---

## 2. Solution Workflow

- Load the startup funding dataset using Pandas  
- Clean the dataset by converting the `amount` column into numeric format  
- Group the data based on `vertical` (startup category)  
- Calculate the total funding received in each sector  
- Display the top 10 sectors with the highest total funding  
- Visualize the result using a bar chart in Matplotlib  

---

## 3. Detailed Input of Each Part

**Dataset Used**: `startup_cleaned.csv`  
(Contains columns like `startup name`, `vertical`, `investors`, `city`, `amount`, etc.)

### Cleaning Steps:
- Remove commas in the `amount` column  
- Convert the `amount` column from text to float  
- Remove missing data (if any) in key columns  

### Grouping:
- Grouped by the `vertical` column using Pandas’ `groupby()`  
- Aggregated using `sum()` to get total funding per sector  

---

## 4. Tech Stack Used

- **Language**: Python 3  
- **Libraries**:
  - `Pandas`: For data reading, cleaning, and analysis  
  - `Matplotlib`: For data visualization (bar plots)  
- **Environment**: Jupyter Notebook / Google Colab  

---

## 5. Output Intent

To visually and numerically present:
- The top sectors receiving startup funding in India  
- The total amount of funding per sector in USD  

This output gives a clear picture of investment trends across industries.

---

## 6. Achieved Accuracy

- Handled all missing and malformed funding values  
- All numeric values were successfully cleaned and converted  
- Grouping and totals correctly reflect real trends based on the dataset  

---

## 7. Use Case, Relevance, and Learning

**Use Case**: Investors and startup founders can see which sectors are attracting the most capital  

**Relevance**: Helps in identifying hot sectors, market confidence, and opportunities for growth  

**Learning**:
- Clean and prepare real-world data  
- Group and summarize using Pandas  
- Create basic visualizations  
- Understand how data analytics supports business insights  

## To run:
- git clone https://github.com/devananda6200/Startup-funding
- pip install streamlit matplotlib pandas
- streamlit run startup.py
