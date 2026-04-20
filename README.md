# SPACEX-Labs

# SpaceX Falcon 9 Landing Prediction 🚀

## Overview
This project predicts whether the **SpaceX Falcon 9 first stage** will land successfully.

SpaceX launches cost about **$62 million**, while competitors may charge over **$165 million**. The cost advantage comes from **reusing the first stage booster**.  
Predicting landing success helps estimate launch costs and supports competitive bidding decisions in the aerospace industry.

---

## Project Goal
- Collect launch data from the SpaceX API
- Clean and format the dataset
- Analyze launch characteristics
- Predict first-stage landing success

---

## Data Source
Data is obtained from the public **SpaceX REST API**:

https://api.spacexdata.com

The dataset includes:
- Launch date
- Rocket version
- Payload mass
- Orbit
- Launch site
- Booster landing outcome

---

## Project Workflow
1. **Data Collection**
   - Retrieve launch data using API requests

2. **Data Wrangling**
   - Handle missing values
   - Convert JSON data into tabular format

3. **Exploratory Data Analysis**
   - Visualize launch trends
   - Study factors affecting landing success

4. **Prediction**
   - Build models to predict landing outcome


---

## Technologies Used
- Python
- Pandas
- NumPy
- Requests
- Matplotlib / Seaborn
- Jupyter Notebook

---

## How to Run
Clone the repository:

```bash
git clone https://github.com/DilbarMammadli/SPACEX-Labs.git
cd SPACEX-Labs
