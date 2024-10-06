import joblib

def load_model(model_path):
    """Load the pre-trained model from the specified path."""
    model = joblib.load(model_path)
    return model

def predict_price(model, features):
    """Predict the house price using the model and input features."""
    return model.predict(features)
