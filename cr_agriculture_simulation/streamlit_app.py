import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cognitive Radio Agricultural Model Simulator", layout="wide")

# ----- Data Loading -----
df = pd.read_csv("data/simulated_agriculture.csv")

# ----- Realistic Hybrid Algorithm -----
def cso_fba_optimization(df):
    df['selected_spider_group'] = ((df['temperature'] > 30) & (df['soil_moisture'] < 400)).astype(int)
    df['optimal_cluster'] = df.get('cluster_id', pd.Series(['A']*len(df)))
    df['action'] = ['Irrigate' if sm < 400 else 'Skip' for sm in df['soil_moisture']]
    df['optimized_cluster'] = (df['soil_moisture'] + df['temperature']) / 2
    return df

df_opt = cso_fba_optimization(df)

# ----- Main Title -----
st.markdown("# Cognitive Radio Agricultural Model Simulator")

# ----- Raw Data Table -----
st.markdown("### Raw Sensor Data")
st.dataframe(df.head(10))

# ----- Optimized Output Table -----
st.markdown("### Optimized Cluster Output (CSO + FBA)")
st.dataframe(df_opt.head(10))

# ----- CSV Download Button -----
st.download_button(
    label='Download Optimized Data as CSV',
    data=df_opt.to_csv(index=False),
    file_name='results.csv',
    mime='text/csv'
)

# ----- Custom Chart (matplotlib with labels, colors) -----
st.markdown("### Sensor Measurements Overview")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['temperature'], label='Temperature (°C)', color='red')
ax.plot(df['soil_moisture'], label='Soil Moisture', color='blue')
ax.plot(df['co2'], label='CO₂ (ppm)', color='green')
ax.set_xlabel("Sample Index") 
ax.set_ylabel("Sensor Values")
ax.set_title("Key Sensor Parameters Over Time")
ax.legend()
st.pyplot(fig)

# ----- Bar Chart (optimized cluster) -----
st.markdown("### Optimized Cluster Values")
st.bar_chart(df_opt['optimized_cluster'])

# ----- More Features: Add-on Experimental Columns -----
if 'energy_consumption' not in df.columns:
    df_opt['energy_consumption'] = np.random.uniform(200, 700, len(df_opt))
    st.markdown("### Randomly Simulated Energy Consumption")
    st.line_chart(df_opt['energy_consumption'])

# ----- (Optional) Theme Switch in Sidebar -----
theme = st.sidebar.radio("Select theme:", ["light", "dark"])
if theme == "dark":
    st.markdown(
        """
        <style>
        body { background-color: #222; color: #e6e6e6; }
        .stDataFrame { background-color: #333; }
        </style>
        """, unsafe_allow_html=True
    )

# ----- Multi-page Navigation Example -----
st.sidebar.markdown("## Navigation")
page = st.sidebar.selectbox("Go to:", ["Main Dashboard", "Sensor Analysis", "Cluster Decisions"])

if page == "Sensor Analysis":
    st.markdown("### Sensor Analysis Page (Demo)")
    st.line_chart(df[['temperature', 'humidity', 'light']])
elif page == "Cluster Decisions":
    st.markdown("### Cluster Decision Simulation (Demo)")
    st.write(df_opt[['optimal_cluster', 'action', 'selected_spider_group']])

# ----- End of App -----
st.markdown("#### Powered by Streamlit (research demo)")

