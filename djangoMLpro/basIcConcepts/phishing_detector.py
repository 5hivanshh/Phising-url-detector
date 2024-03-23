# phishing_detector.py

import pickle

def load_model():
    with open('C:\\Users\\5h1vansh\\Documents\\djangoMLpro\\basIcConcepts\\ML_model\\rf_model.pkl', 'rb') as f:

        model = pickle.load(f)
    return model

# Example usage
def predict_phishing(url):
    model = load_model()
    # Use the model for prediction
