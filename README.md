# 📊 Sales Performance Analytics Dashboard

An interactive, web-based sales analytics dashboard built with **Python**, **Streamlit**, and **Plotly**. Explore sales trends, regional performance, product profitability, and discount impact through dynamic filters and real-time visualizations.

🔗 **Live Demo:** (http://localhost:8501/)

!(assets/dashboard-preview.png)

---

## 🎯 Problem Statement

Sales teams often spend hours manually compiling reports in Excel to answer questions like:
- *"Which region is underperforming this quarter?"*
- *"How do discounts affect our profit margins?"*
- *"What are our top-selling product categories?"*

This dashboard eliminates manual reporting by providing an **interactive, self-service analytics tool** that updates in real-time as filters are applied.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Dynamic Filters** | Filter by date range, region, category, and customer segment |
| **KPI Cards** | Total Sales, Total Profit, Profit Margin, Avg Order Value, Avg Discount |
| **Sales Trend** | Monthly revenue trajectory with spline smoothing |
| **Profit Trend** | Monthly profit tracking |
| **Category Breakdown** | Horizontal bar chart ranking product categories |
| **Regional Distribution** | Donut chart showing sales share by region |
| **Sales vs Profit Scatter** | Identify outliers with discount color-coding and quantity sizing |
| **Discount Impact** | How different discount ranges affect profit margins |
| **Segment Performance** | Sales & profit comparison across customer segments |
| **Top/Bottom Performers** | Best and worst sub-categories by profit |
| **Raw Data Explorer** | Sortable, downloadable data table |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **App Framework** | Streamlit |
| **Deployment** | Streamlit Cloud |
| **Version Control** | Git + GitHub |

---

## 📁 Project Structure

```
sales-dashboard/
├── app.py                    # Main Streamlit application
├── data/
│   └── SampleSuperstore.csv  # Sales dataset (~10,000 records)
├── utils/
│   ├── __init__.py
│   ├── data_loader.py        # Data cleaning & filtering logic
│   └── charts.py             # Reusable Plotly chart functions
├── assets/
│   └── dashboard-preview.png # Screenshot for README
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sales-dashboard.git
   cd sales-dashboard
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv

   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally**
   ```bash
   streamlit run app.py
   ```
   The app will open at `http://localhost:8501`

---

## 🌐 Deployment

This app is deployed on **Streamlit Cloud** (free tier).

To deploy your own fork:
1. Push your code to a **public** GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account and select this repo
4. Set the main file path to `app.py`
5. Click **Deploy** — your app goes live in ~2 minutes

**Pro tip:** Add the live URL to your resume and LinkedIn. Recruiters *will* click it.

---

## 📊 Key Insights from the Data

> *Findings you can discover and mention in interviews:*

- **Technology** is the highest revenue category, but profit margins vary significantly by sub-category
- The **West** region consistently outperforms others in both sales volume and profitability
- Orders with **discounts > 40%** frequently result in negative profit — a clear pricing optimization opportunity
- **Consumer** segment drives the most volume, while **Corporate** has higher average order values
- Certain sub-categories (like Tables and Bookcases in Furniture) show negative profit margins despite high sales

---


## 🧪 Future Enhancements

- [ ] Connect to **SQLite/PostgreSQL** database instead of CSV
- [ ] Add **user authentication** with Streamlit-Authenticator
- [ ] Export reports as **PDF/Excel** with `xlsxwriter` or `reportlab`
- [ ] Integrate **Prophet** for 3-month sales forecasting
- [ ] Add **A/B testing framework** for discount strategy simulation
- [ ] Dockerize the application for consistent deployment

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋 About the Author

**Chenthurr C K** — Aspiring Data Analyst passionate about turning raw data into actionable business insights.

- LinkedIn: (https://www.linkedin.com/in/chenthurr-c-k-901ab0289/)
- Email: pchenthurr@gmail.com
- Portfolio: chenthurrck-portfolio.netilify.app

---

> *Built with ❤️ using Python, Pandas, Plotly, and Streamlit.*
