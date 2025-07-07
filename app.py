import streamlit as st
import pandas as pd

# Load emission factors
df = pd.read_csv("emission_factors.csv")

st.title("BETAM's Product Carbon Footprint Calculator")
st.caption("An internal sustainability tool developed by the Sustainability Department at BETAM ")
st.markdown("""
**Bin Dasmal Engineering Technologies & Management Co. LLC (BETAM)**  
This tool is designed to estimate carbon emissions associated with materials, energy, and transportation — aligned with GHG Protocol Scopes 1, 2, and 3.
""")

# Show data
if st.checkbox("Show Emission Factors"):
    st.dataframe(df)

# Select item
selected_item = st.selectbox("Select Material or Activity", df["Item"].unique())
quantity = st.number_input("Enter Quantity", min_value=0.0, step=0.1)

# Calculate emissions
if selected_item and quantity:
    row = df[df["Item"] == selected_item].iloc[0]
    factor = row["Emission Factor (kg CO₂e/unit)"]
    unit = row["Unit"]
    scope = row["Scope"]
    total_emissions = quantity * factor

    st.markdown(f"**Unit:** {unit}")
    st.markdown(f"**Scope:** {scope}")
    st.success(f"✅ Total Emissions: **{total_emissions:.2f} kg CO₂e**")
