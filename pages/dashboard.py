import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊", 
    layout="wide",
)

# Get the current working directory (where the script is running)
current_dir = os.getcwd()

# Define the relative path to 'datasets/dn.csv'
dataset_path = os.path.join(current_dir, 'datasets', 'dn.csv')

# Title and Introduction
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("""
    ## Welcome to the Customer Churn Prediction Dashboard

    This dashboard provides insightful visualizations and detailed metrics to help you understand and predict customer churn. 
    Here, you can explore key performance indicators, analyze the impact of various factors on churn, and gain actionable insights from the data.
    
    ### What You Can Do:
    - **View KPIs:** Get an overview of the key performance indicators related to churn.
    - **Explore Data:** Analyze the distribution of factors contributing to customer churn.
    - **Compare Metrics:** Assess model performance through precision, recall, and F1-score metrics.

    Use the tabs to navigate through the different sections of the dashboard.
""")

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["EDA Dashboard", "Analytics Dashboard"])

# EDA Dashboard
if options == "EDA Dashboard":
    st.header("🔍 EDA Dashboard")

    # Try to load the CSV file
    try:
        dn = pd.read_csv(dataset_path)
    except FileNotFoundError as e:
        st.error(f"Error: {e}. Please ensure the file exists at the specified path: {dataset_path}")
        dn = None  # Prevent the rest of the code from executing if the file isn't found
    
    # If the file is successfully loaded, continue with visualizations
    if dn is not None:
        # Visualization: Types of Contracts
        if 'Contract' in dn.columns:
            st.markdown("### Types of Contracts")
            value_counts = dn['Contract'].value_counts()
            fig, ax = plt.subplots(figsize=(6, 4))
            value_counts.plot(kind='barh', color='skyblue', ax=ax)
            ax.set_title('Types of Contracts')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure

        # Create histogram plot of Monthly Charges using seaborn
        if 'Monthly_Charges' in dn.columns:
            st.markdown("### Distribution of Monthly Charges")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(data=dn['Monthly_Charges'], kde=True, ax=ax)
            ax.set_title('Distribution of Monthly Charges')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure
        else:
            st.info("No 'Monthly_Charges' column in the dataset.")

        # Create histogram plot of Total Charges using seaborn
        if 'Total_Charges' in dn.columns:
            st.markdown("### Distribution of Total Charges")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(data=dn['Total_Charges'], kde=True, ax=ax)
            ax.set_title('Distribution of Total Charges')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure
        else:
            st.info("No 'Total_Charges' column in the dataset.")

        # Count and create pie chart of the 'SeniorCitizen' column
        if 'Senior_Citizen' in dn.columns:
            st.markdown("### Distribution of Senior Citizens")
            senior_citizen_counts = dn['Senior_Citizen'].value_counts()
            labels = ['Non-Senior Citizen', 'Senior Citizen']
            counts = [senior_citizen_counts.get(0, 0), senior_citizen_counts.get(1, 0)]
            colors = ['#009ACD', '#ADD8E6']
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.pie(counts, labels=labels, colors=colors, autopct='%1.0f%%', shadow=False)
            ax.axis('equal')
            ax.set_title('Distribution of Senior Citizens')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure
        else:
            st.info("No 'Senior_Citizen' column in the dataset.")

        # Visualization: Gender Distribution
        if 'Gender' in dn.columns:
            st.markdown("### Distribution of Gender")
            value_counts = dn['Gender'].value_counts()
            fig, ax = plt.subplots(figsize=(6, 4))
            value_counts.plot(kind='bar', color='red', ax=ax)
            ax.set_title('Distribution of Gender')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure
        else:
            st.info("No 'Gender' column in the dataset.")

        # Calculate churn rates by payment method
        if 'Churn' in dn.columns and 'Payment_Method' in dn.columns:
            st.markdown("### Churn Rate by Payment Method")
            churn_counts = dn.groupby('Payment_Method')['Churn'].value_counts(normalize=True).unstack()
            fig, ax = plt.subplots(figsize=(10, 6))
            churn_counts.plot(kind='bar', stacked=True, color=['green', 'red'], ax=ax)
            ax.set_title('Churn Rate by Payment Method')
            ax.set_xlabel('Payment Method')
            ax.set_ylabel('Churn Rate')
            ax.legend(title='Churn')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure
        else:
            st.info("No 'Churn' or 'Payment_Method' column in the dataset.")

        # Multivariate analysis of Partner, Tenure, Monthly Charges, and Churn
        if all(col in dn.columns for col in ['Partner', 'Churn', 'Tenure_Months', 'Monthly_Charges']):
            st.markdown("### Multivariate Analysis: Partner, Tenure, Monthly Charges and Churn")
            multivariate_df = dn.groupby(['Partner', 'Churn']).agg({'Tenure_Months': 'mean', 'Monthly_Charges': 'mean'}).reset_index()
            fig, ax = plt.subplots(figsize=(12, 8))

            # Tenure vs Churn
            plt.subplot(2, 1, 1)
            sns.barplot(data=multivariate_df, x='Partner', y='Tenure_Months', hue='Churn', palette='pastel')
            plt.title('Tenure vs Churn by Partner Status')
            plt.xlabel('Partner Status')
            plt.ylabel('Average Tenure')

            # Monthly Charges vs Churn
            plt.subplot(2, 1, 2)
            sns.barplot(data=multivariate_df, x='Partner', y='Monthly_Charges', hue='Churn', palette='pastel')
            plt.title('Monthly Charges vs Churn by Partner Status')
            plt.xlabel('Partner Status')
            plt.ylabel('Average Monthly Charges')

            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)  
        else:
            st.info("One or more columns for multivariate analysis are missing.")

        # Grouping by tenure and calculating the mean Total Charges
        if 'Tenure_Months' in dn.columns and 'Total_Charges' in dn.columns:
            st.markdown("### Mean Total Charges by Tenure")
            df_grp_tenure = dn.groupby('Tenure_Months')['Total_Charges'].mean().reset_index()
            df_grp_tenure_15 = df_grp_tenure.head(15)
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.pointplot(data=df_grp_tenure_15, x='Tenure_Months', y='Total_Charges', color='steelblue', ax=ax)
            ax.set_title('Mean Total Charges by Tenure')
            ax.set_xlabel('Tenure')
            ax.set_ylabel('Mean Total Charges')
            st.pyplot(fig)
            plt.close(fig)  # Close the figure
        else:
            st.info("No 'Tenure_Months' or 'Total_Charges' column in the dataset.")


# Analytics Dashboard
elif options == "Analytics Dashboard":
    st.header("📈 Comprehensive Analytics Dashboard")
    st.markdown("""
        ### Dive into the Analytics

        The Analytics Dashboard provides an in-depth view of customer churn predictions. Here, you'll find a comprehensive analysis of the model's performance, including key metrics and visualizations that highlight the effectiveness of the churn prediction model.

        #### What You'll Find:
        - **Key Performance Indicators:** Overview of accuracy, precision, recall, and F1-score.
        - **Detailed Metrics:** Breakdown of model performance across different classes.
        - **Visual Insights:** Graphical representations to help interpret the model's predictions and their implications.

        Use this dashboard to explore how well the model performs and to gain a deeper understanding of the factors influencing customer churn.
    """)

    # Metrics and confusion matrix defined as variables
    accuracy_score = 82.43
    precision_no = 0.87
    recall_no = 0.87
    f1_no = 0.87
    precision_yes = 0.74
    recall_yes = 0
