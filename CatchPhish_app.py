#buidling the catchphish app
import streamlit as st
import pandas as pd
import joblib
from feature_extraction import extract_features

# loading the model
model = joblib.load('Model/xgb_model.pkl')

#creating the main title
st.title("CatchPhish - Phishing URL Detector")

# asking for the user to  URL
url = st.text_input("Enter the URL to check")

if url:
    # extract features from URL
    extracted = extract_features(url)

    # ask to fill additional fields
    st.subheader("Please fill in the additional required fields")

    feature_order = [
        'DomainLength', 'TLDLegitimateProb', 'TLDLength', 'NoOfSubDomain',
        'NoOfLettersInURL', 'LetterRatioInURL', 'NoOfEqualsInURL', 'NoOfQMarkInURL',
        'LineOfCode', 'LargestLineLength', 'HasTitle', 'DomainTitleMatchScore',
        'HasFavicon', 'Robots', 'IsResponsive', 'NoOfURLRedirect', 'NoOfSelfRedirect',
        'NoOfPopup', 'NoOfiFrame', 'HasExternalFormSubmit', 'HasSubmitButton',
        'HasHiddenFields', 'HasPasswordField', 'Bank', 'Pay', 'Crypto', 'NoOfImage',
        'NoOfCSS', 'NoOfJS', 'NoOfEmptyRef', 'NoOfExternalRef'
    ]

    manual_fields = set(feature_order) - set(extracted.keys())

    for field in manual_fields:
        if field.startswith("NoOf"): #setting it so that if a field starts w/noof you can insert an integer greater than 0
            extracted[field] = st.number_input(field, min_value=0)
        elif field.startswith("Has") or field in ['Bank', 'Pay', 'Crypto', 'Robots', 'IsResponsive']: # if feature has 'has' in the beginning it will be a boolean
            extracted[field] = st.selectbox(f"{field} (0 = No, 1 = Yes)", [0, 1])
        elif field == 'DomainTitleMatchScore': #using the slider functionality
            extracted[field] = st.slider(field, 0.0, 1.0)
        elif field in ['LineOfCode', 'LargestLineLength']:#allowing these features to enter integer
            extracted[field] = st.number_input(field, min_value=0)
        elif field == 'TLDLegitimateProb': #using slider functionality
            extracted[field] = st.slider(field, 0.0, 1.0)

    if st.button("Predict"):
        df = pd.DataFrame([[extracted[col] for col in feature_order]], columns=feature_order)
        prediction = model.predict(df)[0]
        label = "Phishing - OPEN AT YOUR OWN DISCRETION" if prediction == 1 else "Legitimate URL, You Can Open this Link"
        st.subheader(f"Prediction: {label}")
