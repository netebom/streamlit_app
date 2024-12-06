import joblib

# Load the pre-trained models
svm_model = joblib.load(r"C:\Users\Etebom\Documents\streamlit\churn_prediction_app\models\Churn_svm_model.pkl")
rf_model = joblib.load(r"C:\Users\Etebom\Documents\streamlit\churn_prediction_app\models\Churn_rf_model.pkl")
xgb_model = joblib.load(r"C:\Users\Etebom\Documents\streamlit\churn_prediction_app\models\Churn_xgb_model.pkl")
knn_model = joblib.load(r"C:\Users\Etebom\Documents\streamlit\churn_prediction_app\models\Churn_knn_model.pkl")

# Create a dictionary to hold the models
components = {
    'tuned_models': {
        'svm': svm_model,
        'random_forest': rf_model,
        'xgboost': xgb_model,
        'knn': knn_model,
    }
}

# Save the components as a pickle file
joblib.dump(components, 'models/churn_model_components.pkl')

print("churn_model_components.pkl has been created successfully!")
