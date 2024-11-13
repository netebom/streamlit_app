import streamlit as st 
st.set_page_config(
    page_title="About App",
    page_icon="🏡",
    layout="wide"
)
# Main Content
def home():
    # Set the title with a larger font and center alignment
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Customer Churn Prediction App</h1>", unsafe_allow_html=True)
    
    # Add a subtitle
    st.markdown("<h3 style='text-align: center; color: #f39c12;'>Designed by Team Fiji</h3>", unsafe_allow_html=True)
    
    # Add a nice visual (banner image or illustration)
    st.image("Customer-churn-prediction.webp", use_column_width=True, caption="Predicting customer churn to retain valuable customers.")

    # Provide a brief introduction or description of the app
    st.write("""
    Welcome to the Customer Churn Prediction App! This application helps you analyze customer behavior and predict churn using advanced machine learning algorithms. 
    Navigate through the app using the sidebar to view data, explore the dashboard, or make predictions.
    """)

# Display the home page
home()

# Key Features
st.subheader("Key Features")
st.markdown("""
- **Data Integration**: Connect to SQL Server to fetch and analyze customer data.
- **Feature Selection**: Choose relevant features for classification.
- **Model Performance Report**: Access a detailed report on model performance.
- **Interactive Charts**: Visualize feature importance and churn probabilities with interactive charts.
""")

# App Features
st.subheader("App Navigation")
st.markdown("""
1. **About This App**: Overview of the application's purpose and functionality.
2. **View Data**: Explore the dataset and understand the customer attributes.
3. **Dashboard**: Visualize key metrics and insights from the data.
4. **Prediction**: Make individual predictions on customer churn.
5. **History Page**: Review past predictions and their outcomes.
""")

# How to Run the App
st.subheader("Running the App")
st.code(""" 
# Activate the virtual environment
venv/Scripts/activate

# Run the Streamlit app
streamlit run app.py
""", language='python')

# Machine Learning Integration
st.subheader("Machine Learning Integration")
st.markdown("""
- **Model Selection**: Choose from various machine learning models for prediction.
- **Prediction**: Generate predictions for individual customers based on their data.
- **Seamless Integration**: Easily incorporate predictions into your business workflow.
- **Insights and Visualization**: Gain valuable insights through interactive charts and graphs.
""")

# Contact and Github Repository
st.subheader("Need Help or Collaboration?")
st.markdown("""
For collaboration or support, please contact Team Fiji.
""")
if st.button("Visit Our GitHub Repository"):
    st.markdown("[GitHub Repository](https://github.com/your-repo-link)")
