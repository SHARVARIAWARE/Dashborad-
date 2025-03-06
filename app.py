import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
import numpy as np

st.set_page_config(page_title="PMBFY Claim Analysis",layout="wide")
df=pd.read_excel("merged_data.xlsx")
st.title("📊 PMFBY Claim Analysis 2018 - 2023")
st.sidebar.header("Select the District:")
district=st.sidebar.multiselect("Select the District:",options=df['District Name'].unique(),default=df['District Name'].unique())
df_selection = df[(df['District Name'].isin(district)) ]

xyz=df_selection[['Year',"Total Applications"]]
fig1=px.bar(xyz,x='Year',y='Total Applications',title="<b>Total Applications per Year<b>",text_auto=True)
st.plotly_chart(fig1)


x_farmers=df_selection[['Year','Farmers']]
fig2=px.bar(x_farmers,x='Year',y='Farmers',title="<b>Total Farmers per Year<b>",text_auto=True,color_discrete_sequence=["#ff7f0e"])
st.plotly_chart(fig2)


cluster_bar = df_selection[['Year', 'Total Applications', 'Farmers']]

# Reshape data (Convert Wide to Long Format)
xyz_melted = cluster_bar.melt(id_vars=['Year'], value_vars=['Total Applications', 'Farmers'], 
                              var_name='Category', value_name='Count')

# Create a Clustered Bar Chart
fig3 = px.bar(
    xyz_melted, 
    x='Year', 
    y='Count', 
    color='Category',  # Groups by 'Total Applications' and 'Farmers'
    barmode='group',  # Enables clustered bars
    title="<b>Total Applications & Farmers per Year</b>", 
    text_auto=True,
    color_discrete_map={"Total Applications": "#1f77b4", "Farmers": "#ff7f0e"} 
)

# Display in Streamlit
st.plotly_chart(fig3)



#4
area_insured=df_selection[['Year','Area Insured (in thousand ha)']]
fig4=px.bar(area_insured,x='Area Insured (in thousand ha)',y='Year',title="<b>Area Insured(in thousand ha) per Year<b>",text_auto=True,color_discrete_sequence=["#6a0dad"],orientation='h')  
st.plotly_chart(fig4)


#5
gross_premium=df_selection[['Year','Gross Premium (in lakhs)']]
fig5=px.bar(gross_premium,x='Year',y='Gross Premium (in lakhs)',title="<b>Gross Premium(in lakhs) per Year<b>",text_auto=True,color_discrete_sequence=["#e63946"])  
st.plotly_chart(fig5)

#6
Line_chart = df_selection[['Year', 'Premium\Sum insured']]
fig6 = px.line(Line_chart, x='Year', y='Premium\Sum insured', 
               title="<b>Gross Premium / Sum Insured per Year</b>", 
               markers=True,  # Adds points to the line
               color_discrete_sequence=["#2ca02c"])  # Green color
fig6.update_traces(text=Line_chart['Premium\Sum insured'], textposition="top center")
st.plotly_chart(fig6)


#7
sum_insured=df_selection[['Year','Sum Insured (In Lac.)']]
fig7=px.bar(sum_insured,x='Sum Insured (In Lac.)',y='Year',title="<b>Sum Insured (In Lac.) per Year<b>",text_auto=True,color_discrete_sequence=["#ff006e"],orientation='h')  
st.plotly_chart(fig7)



#8
cluster_bar1 = df_selection[['Year', 'Farmers', 'Total Farmer Benefit(Actual)']]
xyz_melted1 = cluster_bar1.melt(id_vars=['Year'], value_vars=['Total Farmer Benefit(Actual)', 'Farmers'], 
                              var_name='Category', value_name='Count')
fig8 = px.bar(
    xyz_melted1, 
    x='Year', 
    y='Count', 
    color='Category',  # Groups by 'Total Applications' and 'Farmers'
    barmode='group',  # Enables clustered bars
    title="<b>Farmers And Farmers Benefit per Year</b>", 
    text_auto=True,
    color_discrete_map={"Total Farmer Benefit(Actual)": "#2ca02c", "Farmers": "#ff7f0e"}  # Blue & Orange
)
st.plotly_chart(fig8)



#9
Line_chart1 = df_selection[['Year', 'Claim\Premium']]
fig9 = px.line(Line_chart1, x='Year', y='Claim\Premium', 
               title="<b>Claim/ Gross Premium</b>", 
               markers=True,  # Adds points to the line
               color_discrete_sequence=["#adb5bd"])  # Green color
fig9.update_traces(text=Line_chart1['Claim\Premium'], textposition="top center")

st.plotly_chart(fig9)





#10
cluster_bar2 = df_selection[['Year', 'Total Claim Paid (in lakhs)', 'MSA and ILA andPost Harvest']]
xyz_melted2 = cluster_bar2.melt(id_vars=['Year'], value_vars=['MSA and ILA andPost Harvest', 'Total Claim Paid (in lakhs)'], 
                              var_name='Category', value_name='Count')
fig10 = px.bar(
    xyz_melted2, 
    x='Year', 
    y='Count', 
    color='Category',  # Groups by 'Total Applications' and 'Farmers'
    barmode='group',  # Enables clustered bars
    title="<b>Total Claim against MSA,ILA,Post Harvest per Year</b>", 
    text_auto=True,
    color_discrete_map={"Total Claim Paid (in lakhs)": "#2ca02c", "MSA and ILA andPost Harvest": "#4b5563 "}  # Blue & Orange
)
st.plotly_chart(fig10)




#11
loss = df_selection[['Year', 'Loss in Cr']].copy()

# Add a new column to define colors dynamically
loss['Color'] = np.where(loss['Loss in Cr'] >= 0, 'green', 'red')

# Create a bar chart with conditional colors
fig11 = px.bar(
    loss,
    x='Year',
    y='Loss in Cr',
    title="<b>Loss (in Cr) per Year</b>",
    text_auto=True,
    color='Color',  # Use the dynamically assigned color column
    color_discrete_map={"green": "#2ca02c", "red": "#d62728"}  # Green for +ve, Red for -ve
)

# Hide legend (since we are only using color for visual effect)
fig11.update_layout(showlegend=False)

# Display in Streamlit
st.plotly_chart(fig11)


#12
cluster_bar3 = df_selection[['Year', 'Total Claim Paid (in lakhs)', 'Yield Based (in lakhs)']]
xyz_melted3 = cluster_bar3.melt(id_vars=['Year'], value_vars=['Yield Based (in lakhs)', 'Total Claim Paid (in lakhs)'], 
                              var_name='Category', value_name='Count')
fig12 = px.bar(
    xyz_melted3, 
    x='Year', 
    y='Count', 
    color='Category',  # Groups by 'Total Applications' and 'Farmers'
    barmode='group',  # Enables clustered bars
    title="<b>Total Claim Paid (in lakhs) and Yield Based (in lakhs) per Year</b>", 
    text_auto=True,
    color_discrete_map={"Yield Based (in lakhs)": "#ffc107", "Total Claim Paid (in lakhs)": "#dc3545"}  # Blue & Orange
)
st.plotly_chart(fig12)



