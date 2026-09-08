import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data, filter_data, get_summary_stats
from utils.charts import (
    sales_trend, profit_trend, category_breakdown, regional_sales,
    subcategory_breakdown, sales_vs_profit_scatter, segment_performance,
    discount_impact, top_bottom_products
)

# Page configuration
st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .stMetric {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">📊 Sales Performance Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Interactive analytics for sales, profit, and regional performance insights</p>', unsafe_allow_html=True)

# Load data
@st.cache_data
def get_data():
    return load_data("data/SampleSuperstore.csv")

try:
    df = get_data()
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.info("Please ensure the dataset file 'data/SampleSuperstore.csv' exists.")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filters")
st.sidebar.markdown("---")

# Date range filter
min_date = df['Order Date'].min().date()
max_date = df['Order Date'].max().date()

col_date1, col_date2 = st.sidebar.columns(2)
with col_date1:
    start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
with col_date2:
    end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

if start_date > end_date:
    st.sidebar.error("⚠️ Start date must be before end date!")
    st.stop()

# Region filter
regions = st.sidebar.multiselect(
    "🌍 Region",
    options=sorted(df['Region'].unique()),
    default=sorted(df['Region'].unique())
)

# Category filter
categories = st.sidebar.multiselect(
    "📦 Category",
    options=sorted(df['Category'].unique()),
    default=sorted(df['Category'].unique())
)

# Segment filter
segments = st.sidebar.multiselect(
    "👤 Customer Segment",
    options=sorted(df['Segment'].unique()),
    default=sorted(df['Segment'].unique())
)

st.sidebar.markdown("---")
date_range_text = f"{min_date.strftime('%b %Y')} - {max_date.strftime('%b %Y')}"
date_range_text = f"{min_date.strftime('%b %Y')} - {max_date.strftime('%b %Y')}"
st.sidebar.info(f"📅 Data Range: {date_range_text}  |  📊 Total Records: {len(df):,}")
# Apply filters
filtered_df = filter_data(df, start_date, end_date, regions, categories, segments)

if len(filtered_df) == 0:
    st.warning("⚠️ No data matches your selected filters. Please adjust your selection.")
    st.stop()

# Calculate KPIs
stats = get_summary_stats(filtered_df)

# KPI Cards Row
st.subheader("📈 Key Performance Indicators")
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.metric(
        label="💵 Total Sales",
        value=f"${stats['total_sales']:,.0f}",
        delta=f"{len(filtered_df):,} orders"
    )

with kpi_col2:
    st.metric(
        label="💰 Total Profit",
        value=f"${stats['total_profit']:,.0f}",
        delta=f"{stats['profit_margin']:.1f}% margin"
    )

with kpi_col3:
    st.metric(
        label="🛒 Avg Order Value",
        value=f"${stats['avg_order_value']:,.0f}",
        delta=f"{stats['total_quantity']:,} items sold"
    )

with kpi_col4:
    st.metric(
        label="🏷️ Avg Discount",
        value=f"{stats['avg_discount']:.1f}%",
        delta=f"{stats['total_orders']:,} unique orders"
    )

st.markdown("---")

# Charts Section 1: Trends
st.subheader("📊 Sales & Profit Trends")
trend_col1, trend_col2 = st.columns(2)

with trend_col1:
    st.plotly_chart(sales_trend(filtered_df), use_container_width=True, key="sales_trend")

with trend_col2:
    st.plotly_chart(profit_trend(filtered_df), use_container_width=True, key="profit_trend")

st.markdown("---")

# Charts Section 2: Breakdowns
st.subheader("🔍 Category & Regional Breakdown")
break_col1, break_col2 = st.columns(2)

with break_col1:
    st.plotly_chart(category_breakdown(filtered_df), use_container_width=True, key="category")

with break_col2:
    st.plotly_chart(regional_sales(filtered_df), use_container_width=True, key="region")

st.markdown("---")

# Charts Section 3: Advanced Analytics
st.subheader("🧠 Advanced Analytics")
adv_col1, adv_col2 = st.columns(2)

with adv_col1:
    st.plotly_chart(sales_vs_profit_scatter(filtered_df), use_container_width=True, key="scatter")

with adv_col2:
    st.plotly_chart(discount_impact(filtered_df), use_container_width=True, key="discount")

st.markdown("---")

# Charts Section 4: Segment & Subcategory
st.subheader("👥 Customer & Product Insights")
insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.plotly_chart(segment_performance(filtered_df), use_container_width=True, key="segment")

with insight_col2:
    st.plotly_chart(subcategory_breakdown(filtered_df), use_container_width=True, key="subcategory")

st.markdown("---")

# Top/Bottom Performers
st.subheader("🏆 Performance Rankings")
st.plotly_chart(top_bottom_products(filtered_df), use_container_width=True, key="rankings")

st.markdown("---")

# Data Table Section
st.subheader("📋 Raw Data Explorer")

# Show data stats
st.caption(f"Showing {len(filtered_df):,} of {len(df):,} total records")

# Display dataframe with options
st.dataframe(
    filtered_df[[
        'Order Date', 'Region', 'State', 'Category', 'Sub-Category',
        'Segment', 'Sales', 'Profit', 'Quantity', 'Discount', 'Profit Margin'
    ]].sort_values('Order Date', ascending=False),
    use_container_width=True,
    hide_index=True
)

# Download button
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(filtered_df)
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name=f"sales_data_{start_date}_to_{end_date}.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Python, Pandas, Plotly & Streamlit | Data: Superstore Sales Dataset")
