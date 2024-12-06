import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Prediction History",
    page_icon="🕰️",
    layout="wide",
)

# Display header
st.header("Prediction History")

# Check if history exists in session state
if 'history' in st.session_state and not st.session_state.history.empty:
    # Display the prediction history as a table
    st.dataframe(st.session_state.history)

    # Option to download the history as a CSV file
    csv = st.session_state.history.to_csv(index=False)
    st.download_button(
        label="Download Prediction History as CSV",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
    )
else:
    # If there is no history available
    st.write("No predictions have been made yet.")

