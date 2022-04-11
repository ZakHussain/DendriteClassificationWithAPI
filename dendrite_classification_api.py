"""
To run this app, in your terminal:
> python dendrite_classification_api.py
"""
import connexion
from sklearn.externals import joblib

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

# Load our pre-trained model
clf = joblib.load('./model/Rand_Forest_model.joblib')

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    try:
        predict(1, 1, 1)
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}

# Implement our predict function
def predict(upstroke_downstroke_ratio_short_square, peak_v_ramp, average_interspike_interval):
    # Accept the feature values provided as part of our POST
    # Use these as input to clf.predict()
    prediction = clf.predict([[upstroke_downstroke_ratio_short_square, peak_v_ramp, average_interspike_interval]])

    # Map the predicted value to an actual class
    if prediction[0] == 0:
        predicted_class = "spiny dendrite"
    else:
        predicted_class = "Aspiny dendrite"

    # Return the prediction as a json
    return {"prediction" : predicted_class}

# Read the API definition for our service from the yaml file
app.add_api("dendrite_classification_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()
