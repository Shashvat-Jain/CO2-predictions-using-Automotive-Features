# CO₂ Emissions Prediction from Vehicle Features

**Authors:** Shashvat Jain  
**Affiliation:** Integrated M.Tech. in Mathematics & Computing, IIT Dhanbad  
**GitHub:** https://github.com/Shashvat-Jain/CO2-predictions-using-Automotive-Features

---

## 📖 Project Overview

This repository presents an end-to-end machine-learning pipeline for **analyzing** and **predicting** on-road vehicle CO₂ emissions (g/km) using public datasets. We combine:

1. **Exploratory Data Analysis (EDA)** to understand feature distributions and relationships
2. **Preprocessing & Feature Engineering** (scaling, encoding, power transforms)
3. **Multiple Baseline Models** (linear, polynomial, regularized regressions; tree-based and boosting methods)
4. **Final Stacking Ensemble** (LightGBM, XGBoost, CatBoost base learners → MLP meta-learner → Ridge residual correction)
5. **Hyperparameter Optimization** via Optuna
6. **Comprehensive Diagnostics** (parity plots, residual analysis, learning curves, permutation importance, SHAP)

Key result:

> **Test set**: (R^2 = 0.9830), MAE ≈ 3.08 g/km, RMSE ≈ 8.64 g/km

---

## 📦 Repository Structure

.
├── README.md
├── LICENSE
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DATA_DICTIONARY.md
├── .gitignore
├── environment.yml
├── requirements.txt
├── setup.py
├── Dockerfile
│
├── data/
│ └── New Dataset.csv
│
├── notebooks/
│ └── co2-emissions-predict.ipynb
│
├── src/
│ ├── **init**.py
│ ├── preprocessing.py
│ ├── models.py
│ ├── evaluation.py
│ └── pipeline.py
│
├── tests/
│ └── test_pipeline.py
│
├── Figures/
│ ├── parity_plot.png
│ ├── residual_hist.png
│ ├── qq_plot.png
│ ├── residuals_vs_pred.png
│ ├── mae_decile.png
│ ├── learning_curve.png
│ ├── perm_importance.png
│ ├── shap_summary.png
│ ├── shap_dependence.png
│ └── pipeline_diagram.png
│
├── Slides/
│ └── End Evaluation.pdf
│
└── Reports/
├── Split Report
└── Final Report with plag report.pdf

---

## ⚙️ Installation

1. **Clone the repository**

```bash
   git clone https://github.com/Shashvat-Jain/CO2-predictions-using-Automotive-Features.git
```

2. **Create a virtual environment**

```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. **Install dependencies**

```bash
    pip install -r requirements.txt
```

## 🚀 Usage

1. **Prepare data**
   Place New Dataset.csv under data/.

2. **Run notebook**
   Open and execute notebooks/co2_emissions_predict.ipynb to reproduce EDA, model training, and evaluation.

3. **Diagnostics & plots**
   Generated in figures/:
   - Parity plot
   - Residual histogram & Q-Q plot
   - Learning curve
   - Permutation & SHAP importance charts

Note: The notebook co2_emissions_predict.ipynb contains the complete code for the thesis whereas the src folder only contains the code for the new pipeline presented in this research.

## 📊 Results Snapshot

Figure: ![Predicted vs. True CO₂ Emissions](Figures/Parity%20Plot.png)
Figure: ![Learning Curve](<Figures/Learning%20Curve%20(R2).png>)

## 📚 References

- Smith A., Jones B., Lee C. (2020). Random Forest–Based Prediction of Vehicle CO₂ Emissions. Int. J. Automotive Technol.

- Gupta R., Ramesh S. (2021). XGBoost Regression for Estimating Vehicle Emissions. IEEE Trans. Intelligent Vehicles.

- Tansini A., Pavlović I., Fontaras G. (2022). Forecasting CO₂ Emissions Using Ensemble, ML & DL. PeerJ.

- Zhao P., Zhang X., Li Y. (2023). Global Fuel- and Vehicle-Type-Specific CO₂ Emissions. Earth Syst. Sci. Data.

- Government of Canada (2024). Fuel Consumption Ratings. Open Gov. Portal.

- U.S. EPA (2022). 2022 EPA Automotive Trends Report. EPA-420-S-22-001.

- (See full bibliography in reports/.)

## 📄 License

This project is licensed under the MIT License. See LICENSE for details.
