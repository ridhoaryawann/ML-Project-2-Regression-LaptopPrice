# 💻 Laptop Price Prediction - Regression - Machine Learning Project #2

> 🧪 **This is a mini-project designed to practice and demonstrate an end-to-end Data Science workflow** — from data analysis and model building to deployment using a simple web app.  

The goal is to estimate laptop prices based on their specifications using machine learning. The project is contextualized in a **financial services scenario**, where laptops may be used as **collateral for loans**. This tool helps provide **data-driven estimations** of collateral value.

---

## 🧠 Business Context

Financial institutions often receive laptops as collateral when issuing personal or micro loans. Estimating the device’s fair market value is crucial to minimize lending risk. This ML model helps by predicting the price of a laptop based on its core specs, ensuring **quick, objective, and reliable assessments**.

---

## 📁 Project Structure

```
├── 1-data-analytics.ipynb       # Exploratory Data Analysis (EDA)
├── 2-model-building.ipynb       # Model training with Random Forest & GridSearchCV
├── 3-app.py                     # Streamlit web app for prediction
├── laptop.csv                   # Raw dataset
└── rf_model.pkl                 # Trained model (Random Forest)
```

---

## 🔍 Step-by-Step Breakdown

### 📊 1. Exploratory Data Analysis (`1-data-analytics.ipynb`)

- **Checked** for duplicates, missing values, and descriptive stats
- **Tested for normality** using Shapiro-Wilk and Anderson-Darling
- **Visualized** distributions with boxplots, violin plots, and heatmaps
- **Analyzed relationships** using ANOVA and correlation to `Price`

📌 *Finding:* None of the numerical features followed a normal distribution.

---

### 🏗️ 2. Model Building (`2-model-building.ipynb`)

- Features used: `Processor_Speed`, `RAM_Size`, `Storage_Capacity`
- Trained a **Random Forest Regressor**
- Applied **GridSearchCV** to optimize hyperparameters
- Dropped `Brand` for simplicity in the deployed model

🧠 *Business Insight:* These features are aligned with real-world laptop pricing, making the model intuitive and defensible.

---

### 🌐 3. Deployment (`3-app.py`)

- Built a **Streamlit web application**
- User inputs specs; the app returns an estimated price
- Model loaded with `joblib` (`rf_model.pkl`)

🎯 *Target users:* loan officers or credit analysts estimating laptop value quickly during customer assessments.

---

## ✅ Model Evaluation

| Metric               | Result       |
|----------------------|--------------|
| **Model**            | Random Forest (with GridSearchCV) |
| **Best Parameters**  | Automatically selected |
| **Mean Absolute Error** | Low (as seen in notebook) |
| **Explainability**   | High – only core specs used |
| **Deployment Ready** | ✅ Yes – via Streamlit UI |

---

## 🔍 Feature Importance (Business-Friendly)

- 💾 **Storage Capacity**: Highest influence on price
- 🧠 **RAM Size**: Also a strong contributor
- ⚡ **Processor Speed**: Moderate influence

---

## 🏦 Financial Relevance

- ✅ Enables **automated price estimates**
- ✅ Helps ensure **fair and risk-aware lending**
- ✅ Supports **collateral-based decision making**
- ✅ Backed by **transparent, explainable features**

---

## 🚀 Learning Takeaways

✔️ Full ML pipeline: from raw data to deployed model  
✔️ Learned how to clean, analyze, model, and deploy  
✔️ Built experience with: `pandas`, `scikit-learn`, `seaborn`, `GridSearchCV`, `Streamlit`, `joblib`  

---

## 📌 Future Enhancements

- Reintroduce `Brand` using proper encoding
- Expand input features (GPU, screen size, etc.)
- Build a backend service or API for production use
