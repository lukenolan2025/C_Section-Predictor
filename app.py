import streamlit as st

st.set_page_config(layout="centered")

st.set_page_config(layout="centered")

st.markdown("""
    <style>

        /* Zoom entire Streamlit app to 300% */
        body {
            zoom: 3.0;
        }

        /* Ensure scrolling still works after zooming */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            overflow: auto !important;
            height: 100% !important;
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 14px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }

        ::-webkit-scrollbar-thumb {
            background: #999;
            border-radius: 8px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #666;
        }

        /* Center the main content and limit width */
        .main {
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }

    </style>
""", unsafe_allow_html=True)


st.title("Maternal Health Input")

st.header("Mother Information")

# Grouping mother information fields into columns
col1, col2, col3 = st.columns(3)
with col1:
    mother_name = st.text_input("Mother Name:")
with col2:
    mother_weight = st.number_input("Mother Weight (lb):", min_value=0.0, format="%.2f")
with col3:
    mother_height = st.number_input("Mother Height (in):", min_value=0.0, format="%.2f")

# Calculate BMI
mother_bmi = (mother_weight * 703) / (mother_height**2) if mother_height > 0 else 0.0
st.write(f"Mother BMI: {mother_bmi:.2f}")

num_babies = st.selectbox("Number of babies:", options=list(range(0, 11)))

st.header("Demographic Information")

# Grouping demographic information fields into columns
col4, col5 = st.columns(2)
with col4:
    mother_age = st.selectbox("Mother Age:", options=list(range(15, 51)))
    State = st.selectbox("State:", options=[
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
        "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming", "Other"
    ])
    Education = st.selectbox("Education:", options=[
        "High School(No degree)", "High School (Degree)", "College (No degree)",
        "Associates", "Bachelors", "Masters", "Doctorate"
    ])
with col5:
    County = st.text_input("County:")
    Race = st.selectbox("Race:", options=[
        "Hispanic", "Black", "Asian", "White", "Pacific Islander", "Multiple", "Other"
    ])

st.header("Medical Payment Information")
Medical_Payment = st.selectbox("Medical Payment:", options=[
    "CHAMPUS/TRICARE", "INDIAN HEALTH SERVICE", "MEDICAID", "OTHER GOVERNMENT", "PRIVATE INSURANCE"
])

st.header("Health Conditions")

# Grouping health conditions fields into columns
cond_col1, cond_col2 = st.columns(2)
with cond_col1:
    full_term = st.radio("Full Term:", ("Yes", "No"))
    pre_pregnancy_diabetes = st.radio("Pre Pregnancy Diabetes:", ("Yes", "No"))
    gestational_diabetes = st.radio("Gestational Diabetes:", ("Yes", "No"))
    pre_pregnancy_hypertension = st.radio("Pre Pregnancy Hypertension:", ("Yes", "No"))
with cond_col2:
    gestational_hypertension = st.radio("Gestational Hypertension:", ("Yes", "No"))
    hypertension_eclampsia = st.radio("Hypertension Eclampsia:", ("Yes", "No"))
    prior_c_section = st.radio("Prior C-Section:", ("Yes", "No"))

st.header("Submit Data")
if st.button("Submit Data"):
    data = {
        "Mother Name": mother_name,
        "Mother Age": mother_age,
        "Mother Weight (lb)": mother_weight,
        "Mother Height (in)": mother_height,
        "Mother BMI": mother_bmi,
        "Number of babies": num_babies,
        "State": State,
        "County": County,
        "Race": Race,
        "Education": Education,
        "Medical Payment": Medical_Payment,
        "Full Term": full_term,
        "Pre Pregnancy Diabetes": pre_pregnancy_diabetes,
        "Gestational Diabetes": gestational_diabetes,
        "Pre Pregnancy Hypertension": pre_pregnancy_hypertension,
        "Gestational Hypertension": gestational_hypertension,
        "Hypertension Eclampsia": hypertension_eclampsia,
        "Prior C-Section": prior_c_section
    }

    numerical_sum = sum(v for v in data.values() if isinstance(v, (int, float)))
    st.write("Sum of Numerical Data:", numerical_sum)
