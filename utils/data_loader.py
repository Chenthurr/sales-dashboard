import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(path):
    """
    Load and preprocess the Superstore sales data.

    Args:
        path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Cleaned and processed dataframe
    """
    df = pd.read_csv(path, encoding='latin1')

    # Convert date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')

    # Extract time components for filtering
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Month Name'] = df['Order Date'].dt.strftime('%b %Y')
    df['Quarter'] = df['Order Date'].dt.quarter
    df['Day of Week'] = df['Order Date'].dt.day_name()

    # Calculate derived metrics
    df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
    df['Profit Margin'] = df['Profit Margin'].fillna(0)
    df['Discounted'] = df['Discount'] > 0

    # Handle edge cases
    df['Profit Margin'] = df['Profit Margin'].replace([np.inf, -np.inf], 0)

    return df

def filter_data(df, start_date, end_date, regions, categories, segments=None):
    """
    Filter dataframe based on user selections.

    Args:
        df (pd.DataFrame): Source dataframe
        start_date: Start date filter
        end_date: End date filter
        regions (list): Selected regions
        categories (list): Selected categories
        segments (list, optional): Selected segments

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    mask = (
        (df['Order Date'] >= pd.Timestamp(start_date)) &
        (df['Order Date'] <= pd.Timestamp(end_date)) &
        (df['Region'].isin(regions)) &
        (df['Category'].isin(categories))
    )

    if segments and len(segments) > 0:
        mask = mask & (df['Segment'].isin(segments))

    return df[mask].copy()

def get_summary_stats(df):
    """
    Calculate key performance indicators.

    Args:
        df (pd.DataFrame): Filtered dataframe

    Returns:
        dict: Dictionary of KPI values
    """
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['Order ID'].nunique()
    avg_order_value = total_sales / total_orders if total_orders > 0 else 0
    profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    total_quantity = df['Quantity'].sum()
    avg_discount = df['Discount'].mean() * 100

    return {
        'total_sales': total_sales,
        'total_profit': total_profit,
        'total_orders': total_orders,
        'avg_order_value': avg_order_value,
        'profit_margin': profit_margin,
        'total_quantity': total_quantity,
        'avg_discount': avg_discount
    }
