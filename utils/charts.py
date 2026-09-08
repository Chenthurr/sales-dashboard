import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def sales_trend(df):
    """Monthly sales trend line chart."""
    monthly = df.groupby('Month Name')['Sales'].sum().reset_index()
    # Sort by actual date order
    monthly['Sort'] = pd.to_datetime(monthly['Month Name'], format='%b %Y')
    monthly = monthly.sort_values('Sort')

    fig = px.line(
        monthly, 
        x='Month Name', 
        y='Sales', 
        title='📈 Monthly Sales Trend',
        markers=True,
        line_shape='spline'
    )
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    fig.update_traces(line_color='#1f77b4', line_width=3)
    return fig

def profit_trend(df):
    """Monthly profit trend line chart."""
    monthly = df.groupby('Month Name')['Profit'].sum().reset_index()
    monthly['Sort'] = pd.to_datetime(monthly['Month Name'], format='%b %Y')
    monthly = monthly.sort_values('Sort')

    fig = px.line(
        monthly, 
        x='Month Name', 
        y='Profit', 
        title='💰 Monthly Profit Trend',
        markers=True,
        line_shape='spline'
    )
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title='Profit ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    fig.update_traces(line_color='#2ca02c', line_width=3)
    return fig

def category_breakdown(df):
    """Sales by category bar chart."""
    cat_sales = df.groupby('Category')['Sales'].sum().reset_index().sort_values('Sales', ascending=True)

    fig = px.bar(
        cat_sales, 
        x='Sales', 
        y='Category',
        orientation='h',
        title='📊 Sales by Category',
        color='Category',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        xaxis_title='Sales ($)',
        yaxis_title='',
        template='plotly_white',
        showlegend=False,
        height=350
    )
    return fig

def regional_sales(df):
    """Sales by region pie chart."""
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()

    fig = px.pie(
        region_sales, 
        values='Sales', 
        names='Region', 
        title='🌍 Sales by Region',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4
    )
    fig.update_layout(
        template='plotly_white',
        height=350
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def subcategory_breakdown(df):
    """Top 10 sub-categories by sales."""
    sub_sales = df.groupby('Sub-Category')['Sales'].sum().reset_index().sort_values('Sales', ascending=False).head(10)

    fig = px.bar(
        sub_sales, 
        x='Sub-Category', 
        y='Sales',
        title='🏆 Top 10 Sub-Categories by Sales',
        color='Sales',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        xaxis_title='',
        yaxis_title='Sales ($)',
        template='plotly_white',
        height=400
    )
    return fig

def sales_vs_profit_scatter(df):
    """Scatter plot of Sales vs Profit with discount color coding."""
    fig = px.scatter(
        df,
        x='Sales',
        y='Profit',
        color='Discount',
        size='Quantity',
        hover_data=['Category', 'Sub-Category', 'Region'],
        title='💡 Sales vs Profit (Color = Discount, Size = Quantity)',
        color_continuous_scale='RdYlBu_r'
    )
    fig.update_layout(
        template='plotly_white',
        height=450
    )
    # Add a horizontal line at y=0
    fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Break-even")
    return fig

def segment_performance(df):
    """Sales by customer segment."""
    seg_data = df.groupby('Segment').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'nunique'
    }).reset_index()
    seg_data.columns = ['Segment', 'Sales', 'Profit', 'Orders']
    seg_data['Avg Order Value'] = seg_data['Sales'] / seg_data['Orders']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=seg_data['Segment'],
        y=seg_data['Sales'],
        name='Sales',
        marker_color='#1f77b4'
    ))
    fig.add_trace(go.Bar(
        x=seg_data['Segment'],
        y=seg_data['Profit'],
        name='Profit',
        marker_color='#2ca02c'
    ))
    fig.update_layout(
        title='👥 Sales & Profit by Customer Segment',
        barmode='group',
        template='plotly_white',
        height=350,
        xaxis_title='',
        yaxis_title='Amount ($)'
    )
    return fig

def discount_impact(df):
    """Show how discount levels affect profit margins."""
    df['Discount Range'] = pd.cut(df['Discount'], 
                                   bins=[0, 0.01, 0.2, 0.4, 0.6, 1.0],
                                   labels=['No Discount', '1-20%', '21-40%', '41-60%', '60%+'],
                                   include_lowest=True)

    discount_data = df.groupby('Discount Range').agg({
        'Profit Margin': 'mean',
        'Sales': 'sum',
        'Order ID': 'count'
    }).reset_index()
    discount_data.columns = ['Discount Range', 'Avg Profit Margin', 'Total Sales', 'Order Count']

    fig = px.bar(
        discount_data,
        x='Discount Range',
        y='Avg Profit Margin',
        title='📉 Discount Impact on Profit Margin',
        color='Avg Profit Margin',
        color_continuous_scale='RdYlGn',
        text='Avg Profit Margin'
    )
    fig.update_layout(
        template='plotly_white',
        height=350,
        xaxis_title='Discount Range',
        yaxis_title='Avg Profit Margin (%)'
    )
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    return fig

def top_bottom_products(df, top_n=10):
    """Top and bottom performing products by profit."""
    product_profit = df.groupby('Sub-Category')['Profit'].sum().reset_index().sort_values('Profit', ascending=False)
    top = product_profit.head(top_n)
    bottom = product_profit.tail(top_n).sort_values('Profit')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=top['Sub-Category'],
        x=top['Profit'],
        orientation='h',
        name='Top Performers',
        marker_color='#2ca02c'
    ))
    fig.add_trace(go.Bar(
        y=bottom['Sub-Category'],
        x=bottom['Profit'],
        orientation='h',
        name='Bottom Performers',
        marker_color='#d62728'
    ))
    fig.update_layout(
        title=f'🏅 Top & Bottom {top_n} Sub-Categories by Profit',
        template='plotly_white',
        height=500,
        xaxis_title='Profit ($)',
        yaxis_title='',
        barmode='group'
    )
    return fig
