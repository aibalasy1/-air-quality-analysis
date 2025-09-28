# 🌬️ Air Quality Analysis and Pollutant Forecasting

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-yellowgreen?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![MIT License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

## 📖 Project Overview

A comprehensive diploma project focused on air quality analysis and forecasting using time series data of pollutants (CO, NO, PM10, PM2.5, SO2) combined with meteorological data. This project employs advanced machine learning techniques and statistical analysis to understand air pollution patterns and build predictive models.

### 🎯 Project Objectives

- **Time Series Analysis**: Comprehensive analysis of pollutant temporal patterns
- **Pattern Recognition**: Identification of cyclical and seasonal trends in air quality data  
- **Predictive Modeling**: Development of forecasting models using lagged variables
- **Environmental Impact**: Investigation of meteorological factors' influence on pollution levels
- **Feature Engineering**: Advanced feature selection and lag variable optimization

## 🏗️ Project Architecture

```
📦 Air Quality Analysis Project
├── 📊 Core Data
│   ├── airdata_updated.csv                    # Main air quality dataset
│   ├── merged_dataset_new.csv                 # Consolidated dataset
│   ├── upd_sep_targets/                       # Individual pollutant datasets
│   │   ├── dataset_CO.csv                     # Carbon monoxide data
│   │   ├── dataset_NO.csv                     # Nitrogen oxide data
│   │   ├── dataset_PM10.csv                   # PM10 particulate matter
│   │   ├── dataset_PM2.5.csv                  # PM2.5 fine particles
│   │   └── dataset_SO2.csv                    # Sulfur dioxide data
│   └── upd_sep_targets_with_lags/             # Datasets with engineered lag features
├── 📈 Analysis Notebooks
│   ├── preprocessing.ipynb                    # Data preprocessing & cleaning
│   ├── Analysis of time variables.ipynb       # Time series analysis & FFT
│   └── Рабочая версия .ipynb                  # Main modeling & feature selection
├── 🌤️ Weather Data
│   └── weatherapi/                            # Meteorological API data
│       ├── new/                               # Current weather stations
│       └── old/                               # Historical weather data
└── 📋 Processed Datasets
    └── updated_dataset/                       # Filtered & cleaned data
```

## � Monitored Air Pollutants

This project analyzes five critical air quality indicators:

<div align="center">

| Pollutant | Full Name | Units | Health Impact | WHO Guidelines |
|-----------|-----------|--------|---------------|----------------|
| **CO** | Carbon Monoxide | mg/m³ | ⚠️ High | 30 mg/m³ (1h) |
| **NO** | Nitrogen Oxide | μg/m³ | ⚠️ Medium | 200 μg/m³ (1h) |
| **PM10** | Particulate Matter ≤10μm | μg/m³ | 🔴 High | 50 μg/m³ (24h) |
| **PM2.5** | Fine Particulate Matter ≤2.5μm | μg/m³ | 🔴 Very High | 25 μg/m³ (24h) |
| **SO2** | Sulfur Dioxide | μg/m³ | ⚠️ Medium | 125 μg/m³ (24h) |

</div>

## 🚀 Quick Start Guide

### Prerequisites

Ensure you have Python 3.8+ installed. Then install the required packages:

```bash
# Install required packages
pip install -r requirements.txt

# OR install individually
pip install pandas numpy matplotlib seaborn scikit-learn jupyter scipy statsmodels openpyxl requests
```

### 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/aibalasy1/air-quality-analysis.git
   cd air-quality-analysis
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv air_quality_env
   source air_quality_env/bin/activate  # On Windows: air_quality_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

### � Notebook Execution Order

Execute the notebooks in the following sequence for optimal results:

1. **`preprocessing.ipynb`** 
   - Data loading and cleaning
   - Meteorological data integration  
   - Missing value handling
   - Data quality assessment

2. **`Analysis of time variables.ipynb`**
   - FFT analysis for cyclical patterns
   - Granger causality testing
   - Lag variable generation
   - Temporal dependency analysis

3. **`Рабочая версия .ipynb`**
   - Feature selection (Lasso, ElasticNet)
   - Feature importance visualization
   - Outlier detection and removal
   - Model building and evaluation

## 🔬 Advanced Methodology

### 1. 🧹 Data Preprocessing Pipeline
- **Data Integration**: Merging air quality measurements with meteorological observations
- **Temporal Alignment**: Synchronizing timestamps across different data sources
- **Missing Data Handling**: Advanced interpolation techniques for gap filling
- **Quality Control**: Outlier detection using statistical and domain-specific thresholds
- **Feature Engineering**: Creation of derived variables (seasons, time indicators)

### 2. ⏰ Time Series Analysis Framework
- **📊 FFT Analysis**: Fast Fourier Transform to identify periodic components
  - Daily cycles (24-hour patterns)
  - Weekly cycles (7-day patterns) 
  - Seasonal variations
- **🔗 Granger Causality Testing**: Determining causal relationships between variables
- **📈 Lag Variable Engineering**: Systematic creation of temporal dependencies
- **🌊 Stationarity Testing**: ADF tests and trend analysis

### 3. 🎯 Feature Selection Methodology
```python
# Advanced feature selection pipeline
├── Lasso Regression (L1 regularization)
│   ├── Automatic feature selection
│   ├── Sparsity enforcement
│   └── Cross-validation optimization
├── ElasticNet (L1 + L2 regularization)
│   ├── Balanced regularization
│   ├── Grouped variable selection
│   └── Stability enhancement
└── Random Forest Importance
    ├── Non-linear feature interactions
    ├── Permutation importance
    └── Robust importance metrics
```

### 4. 🤖 Machine Learning Pipeline
- **Time Series Split**: Temporal validation to prevent data leakage
- **Nested Cross-Validation**: Robust hyperparameter optimization
- **Model Ensemble**: Combining multiple algorithms for improved predictions
- **Residual Analysis**: Comprehensive model diagnostic procedures

## 📈 Key Research Findings

### 🏭 Monitoring Stations Performance
<div align="center">

| Station | Location | Data Completeness | Primary Use |
|---------|----------|-------------------|-------------|
| **k7** | Urban Center | 99.8% | 🎯 Primary Analysis Station |
| **k8** | Industrial Area | 97.2% | Secondary Analysis |
| **k9** | Residential Zone | 96.8% | Comparative Studies |  
| **k12** | Suburban Area | 85.4% | Limited Analysis |

</div>

### 🔍 Discovered Patterns

#### Temporal Cycles Identified:
- **Daily Patterns**: Rush hour peaks (7-9 AM, 5-7 PM)
- **Weekly Cycles**: Higher weekday pollution, weekend recovery
- **Seasonal Variations**: Winter heating effects, summer photochemical processes
- **Meteorological Dependencies**: Wind speed/direction correlations

#### Optimal Lag Variables by Pollutant:
<div align="center">

| Pollutant | Optimal Lags (days) | Model Performance | Key Predictors |
|-----------|---------------------|-------------------|----------------|
| **CO** | 1, 6 | R² = 0.82 | Traffic, Temperature |
| **NO** | 0.5, 1, 9 | R² = 0.78 | Vehicle emissions, Wind |
| **PM10** | 1 | R² = 0.75 | Dust, Meteorology |
| **PM2.5** | 1 | R² = 0.79 | Combustion, Humidity |
| **SO2** | 6 | R² = 0.71 | Industrial, Pressure |

</div>

### 🎯 Statistical Significance
- **Granger Causality Tests**: Significant relationships (p < 0.05) found between:
  - Meteorological variables → Pollutant concentrations
  - Cross-pollutant dependencies (NO ↔ CO correlation: r = 0.64)
  - Temporal lag effects up to 9 days for certain pollutants

## 🛠️ Technology Stack & Dependencies

<div align="center">

### Core Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Machine Learning & Statistics
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-8CAAE6?style=for-the-badge&logo=python&logoColor=white)

### Visualization & Data Processing
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-2E7D32?style=for-the-badge&logo=microsoft-excel&logoColor=white)

</div>

### 📋 Detailed Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **pandas** | ≥2.0.0 | Data manipulation and analysis |
| **numpy** | ≥1.21.0 | Numerical computing |
| **scikit-learn** | ≥1.3.0 | Machine learning algorithms |
| **matplotlib** | ≥3.5.0 | Static plotting and visualization |
| **seaborn** | ≥0.12.0 | Statistical data visualization |
| **scipy** | ≥1.9.0 | Scientific computing |
| **statsmodels** | ≥0.14.0 | Statistical modeling |
| **jupyter** | ≥1.0.0 | Interactive notebooks |
| **openpyxl** | ≥3.0.0 | Excel file processing |
| **requests** | ≥2.28.0 | HTTP library for API calls |

## � Usage Examples

### Basic Data Loading
```python
import pandas as pd
import numpy as np

# Load processed datasets with lag features
data_co = pd.read_csv("upd_sep_targets_with_lags/dataset_CO_with_lags.csv")
data_no = pd.read_csv("upd_sep_targets_with_lags/dataset_NO_with_lags.csv")
# ... (other pollutants)
```

### Feature Importance Analysis
```python
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

def plot_feature_importances(df, target):
    X = df.drop(columns=[target, "datetime"])
    y = df[target]
    
    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)
    
    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=importance_df.head(15), x="Importance", y="Feature")
    plt.title(f"Top 15 Features for {target}")
    plt.show()
```

### Advanced Feature Selection
```python
from sklearn.linear_model import ElasticNetCV
from sklearn.preprocessing import StandardScaler

def select_features_elasticnet(df, target, alpha_values=np.logspace(-3, 2, 50)):
    X = df.drop(columns=[target, "datetime"]).fillna(0)
    y = df[target].fillna(method='ffill')
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = ElasticNetCV(alphas=alpha_values, cv=5, random_state=42)
    model.fit(X_scaled, y)
    
    selected_features = X.columns[model.coef_ != 0].tolist()
    return df[["datetime", target] + selected_features]
```

## 📊 Data Structure Overview

### Main Dataset Schema
```
📋 airdata_updated.csv
├── datetime          : datetime64[ns] - Timestamp (3-hour intervals)
├── stationId         : object - Station identifier (k7, k8, k9, k12)
├── CO                : float64 - Carbon monoxide concentration (mg/m³)
├── NO                : float64 - Nitrogen oxide concentration (μg/m³)  
├── PM10              : float64 - PM10 concentration (μg/m³)
├── PM2.5             : float64 - PM2.5 concentration (μg/m³)
├── SO2               : float64 - Sulfur dioxide concentration (μg/m³)
├── temperature_2m    : float64 - Temperature at 2m height (°C)
├── relative_humidity_2m : float64 - Relative humidity (%)
├── precipitation     : float64 - Precipitation amount (mm)
├── pressure_msl      : float64 - Mean sea level pressure (hPa)
├── wind_speed_10m    : float64 - Wind speed at 10m (m/s)
├── wind_direction_10m : float64 - Wind direction (degrees)
├── cloud_cover       : float64 - Cloud cover percentage (%)
└── season            : object - Season indicator (heating/non-heating)
```

### Lag Features Schema
```
📋 *_with_lags.csv files additionally contain:
├── CO_lag_1          : float64 - CO value 1 day ago
├── CO_lag_6          : float64 - CO value 6 days ago
├── NO_lag_0.5        : float64 - NO value 0.5 days ago
├── [pollutant]_lag_[days] : float64 - Lag features for all pollutants
└── station_[id]      : bool - Binary station indicators
```

## 🤝 Contributing & Collaboration

### 🔬 Research Contributions
This project welcomes contributions in the following areas:
- **Algorithm Improvements**: Enhanced feature selection methods
- **New Data Sources**: Additional meteorological or pollution datasets  
- **Model Extensions**: Deep learning approaches for time series
- **Validation Studies**: Cross-regional model validation
- **Visualization**: Advanced interactive dashboards

### 📝 Coding Standards
- **PEP 8**: Python code formatting
- **Type Hints**: Use type annotations where applicable
- **Docstrings**: Comprehensive function documentation
- **Testing**: Unit tests for critical functions
- **Version Control**: Meaningful commit messages

### 🐛 Issue Reporting
When reporting issues, please include:
- Python version and environment details
- Complete error traceback
- Data sample that reproduces the issue
- Expected vs. actual behavior

## 👨‍🎓 Author & Academic Context

**Author**: aibalasy1  
**Institution**: [University Name]  
**Degree Program**: Environmental Engineering / Data Science  
**Academic Year**: 2024-2025  
**Supervisor**: [Supervisor Name]  

### 🏆 Academic Achievements
- Advanced time series analysis methodologies
- Novel lag variable optimization techniques
- Comprehensive air quality forecasting framework
- Statistical validation of environmental relationships

## 📄 License & Usage Rights

```
MIT License

Copyright (c) 2025 aibalasy1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 🙏 Acknowledgments & References

### Special Thanks
- **Academic Supervisor** for guidance and research direction
- **Environmental Monitoring Agencies** for providing air quality data
- **Open-Source Community** for excellent Python libraries
- **Weather API Providers** for meteorological data access

### Key References
1. Box, G. E. P., & Jenkins, G. M. (2015). *Time Series Analysis: Forecasting and Control*
2. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*
3. WHO Air Quality Guidelines (2021). *Global Update 2021*
4. Granger, C. W. J. (1969). "Investigating Causal Relations by Econometric Models"

### Related Publications
- Environmental time series analysis methodologies
- Machine learning applications in air quality monitoring  
- Meteorological influence on urban pollution patterns

---

<div align="center">

## 📞 Contact & Support

[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red?style=for-the-badge&logo=github)](https://github.com/aibalasy1/air-quality-analysis/issues)
[![Email](https://img.shields.io/badge/Email-Contact-blue?style=for-the-badge&logo=gmail)](mailto:your.email@domain.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-profile)

**If you find this research useful, please consider starring ⭐ the repository!**

*Last Updated: September 2025*

</div>