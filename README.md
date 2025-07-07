# Product Carbon Footprint (PCF) Calculator

This is a web-based **Product Carbon Footprint (PCF) Calculator** developed using **Python** and **Streamlit**. It estimates carbon emissions associated with a product or activity based on preloaded emission factors — aligned with **Scope 1, 2, and 3** categories of the Greenhouse Gas (GHG) Protocol.

---

## Live Demo

🔗 [Click here to try the app](https://your-username.streamlit.app)  
_(Replace with your actual deployed Streamlit app link)_

---

## Features

- Real-time carbon footprint calculation
- Dropdown selection of common materials and energy sources
- Scope 1, 2, and 3 classification for each activity
- Based on standard emission factor data (editable via CSV)
- Clean, minimal UI for fast use and testing

---

## Emission Factors Included

| Item                        | Emission Factor (kg CO₂e/unit) | Unit     | Scope   |
|-----------------------------|-------------------------------|----------|---------|
| Electricity (UAE Grid)      | 0.423                         | kWh      | Scope 2 |
| Diesel                      | 2.68                          | Litre    | Scope 1 |
| Plastic (LDPE)              | 1.75                          | kg       | Scope 3 |
| Steel                       | 1.85                          | kg       | Scope 3 |
| Cardboard Box               | 0.15                          | unit     | Scope 3 |
| Transportation (truck)      | 0.12                          | ton-km   | Scope 3 |

---

## File Structure
product-carbon-footprint/
├── app.py # Main application logic
├── emission_factors.csv # Dataset of GHG emission factors
├── requirements.txt # Streamlit + pandas dependencies
└── README.md # Project documentation
## Tech Stack

- Python
- Streamlit
- Pandas
- GitHub + Streamlit Cloud

---

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
