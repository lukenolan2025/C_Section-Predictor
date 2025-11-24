import math
import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
    <style>

        /* -------------------------------------- */
        /* FORCE VERTICAL SCROLL BAR ON RIGHT SIDE */
        /* -------------------------------------- */
        html, body, [data-testid="stAppViewContainer"] {
            overflow-y: scroll !important;   /* Always show vertical scroll */
        }

        /* Prevent horizontal scrolling */
        html, body {
            overflow-x: hidden !important;
        }

        /* Optional: keep app centered and tidy */
        .main {
            max-width: 900px;
            margin: auto;
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
    married = st.selectbox("Married:", options=["Yes", "No", "Unknown"]) # New widget

st.header("Medical Payment Information")
Medical_Payment = st.selectbox("Medical Payment:", options=[
    "CHAMPUS/TRICARE", "INDIAN HEALTH SERVICE", "MEDICAID", "OTHER GOVERNMENT", "PRIVATE INSURANCE"
])

st.header("Health Conditions")

# Grouping health conditions radio buttons into columns
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

# New columns for additional health conditions (STIs and infertility) - all radio buttons
cond_col3, cond_col4 = st.columns(2)
with cond_col3:
    syphilis = st.radio("Syphilis:", ("Yes", "No"))
    chlamydia = st.radio("Chlamydia:", ("Yes", "No"))
with cond_col4:
    gonorrhea = st.radio("Gonorrhea:", ("Yes", "No"))
    hepatitis_b = st.radio("Hepatitis B:", ("Yes", "No"))
    hepatitis_c = st.radio("Hepatitis C:", ("Yes", "No"))
    infertility_treatment_used = st.radio("Infertility Treatment Used:", ("Yes", "No"))

st.subheader("Additional Health Metrics") # Adding a subheader for clarity
num_cond_col1, num_cond_col2 = st.columns(2)
with num_cond_col1:
    weight_gained = st.number_input("Weight Gained (lb):", min_value=0.0, format="%.2f")
    cigarettes_trimester1 = st.number_input("Cigarettes in Trimester 1:", min_value=0, format="%d")
with num_cond_col2:
    cigarettes_trimester2 = st.number_input("Cigarettes in Trimester 2:", min_value=0, format="%d")
    cigarettes_trimester3 = st.number_input("Cigarettes in Trimester 3:", min_value=0, format="%d")

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
        "Married": married, # Added to data dictionary
        "Education": Education,
        "Medical Payment": Medical_Payment,
        "Full Term": full_term,
        "Pre Pregnancy Diabetes": pre_pregnancy_diabetes,
        "Gestational Diabetes": gestational_diabetes,
        "Pre Pregnancy Hypertension": pre_pregnancy_hypertension,
        "Gestational Hypertension": gestational_hypertension,
        "Hypertension Eclampsia": hypertension_eclampsia,
        "Prior C-Section": prior_c_section,
        "Syphilis": syphilis, # Added to data dictionary
        "Chlamydia": chlamydia, # Added to data dictionary
        "Gonorrhea": gonorrhea, # Added to data dictionary
        "Hepatitis B": hepatitis_b, # Added to data dictionary
        "Hepatitis C": hepatitis_c, # Added to data dictionary
        "Infertility Treatment Used": infertility_treatment_used, # Added to data dictionary
        "Weight Gained (lb)": weight_gained, # Added to data dictionary
        "Cigarettes in Trimester 1": cigarettes_trimester1, # Added to data dictionary
        "Cigarettes in Trimester 2": cigarettes_trimester2, # Added to data dictionary
        "Cigarettes in Trimester 3": cigarettes_trimester3 # Added to data dictionary
    }

    # Convert categorical inputs to dummy variables (0 or 1)
    mbraceship_Hispanic = 1 if data["Race"] == "Hispanic" else 0
    mbraceship_Non_Hispanic_AIAN_only = 0 # Not directly available, defaulting to 0
    mbraceship_Non_Hispanic_Black_only = 1 if data["Race"] == "Black" else 0
    mbraceship_Non_Hispanic_NHOPI_only = 1 if data["Race"] == "Pacific Islander" else 0
    mbraceship_Non_Hispanic_White_only = 1 if data["Race"] == "White" else 0
    mbraceship_Non_Hispanic_more_than_one_race = 1 if data["Race"] == "Multiple" else 0

    has_college_degree = 1 if data["Education"] in ["Associates", "Bachelors", "Masters", "Doctorate"] else 0

    pay_CHAMPUS_TRICARE = 1 if data["Medical Payment"] == "CHAMPUS/TRICARE" else 0
    pay_Indian_Health_Service = 1 if data["Medical Payment"] == "INDIAN HEALTH SERVICE" else 0
    pay_Medicaid = 1 if data["Medical Payment"] == "MEDICAID" else 0
    pay_Other_Government = 1 if data["Medical Payment"] == "OTHER GOVERNMENT" else 0
    pay_Private_Insurance = 1 if data["Medical Payment"] == "PRIVATE INSURANCE" else 0

    # Region mapping - define a simple mapping for demonstration
    NORTHEAST_STATES = ["Connecticut", "Delaware", "Maine", "Maryland", "Massachusetts", "New Hampshire", "New Jersey", "New York", "Pennsylvania", "Rhode Island", "Vermont"]
    MIDWEST_STATES = ["Illinois", "Indiana", "Iowa", "Kansas", "Michigan", "Minnesota", "Missouri", "Nebraska", "North Dakota", "Ohio", "South Dakota", "Wisconsin"]
    WEST_STATES = ["Alaska", "Arizona", "California", "Colorado", "Hawaii", "Idaho", "Montana", "Nevada", "New Mexico", "Oregon", "Utah", "Washington", "Wyoming"]

    region_Midwest = 1 if data["State"] in MIDWEST_STATES else 0
    region_Northeast = 1 if data["State"] in NORTHEAST_STATES else 0
    region_West = 1 if data["State"] in WEST_STATES else 0

    dmar_Married = 1 if data["Married"] == "Yes" else 0

    # Health conditions (dummy variables)
    breech_dummy = 0 # Not available in form, defaulting to 0
    rf_pdiab_dummy = 1 if data["Pre Pregnancy Diabetes"] == "Yes" else 0
    rf_gdiab_dummy = 1 if data["Gestational Diabetes"] == "Yes" else 0
    rf_phype_dummy = 1 if data["Pre Pregnancy Hypertension"] == "Yes" else 0
    rf_ghype_dummy = 1 if data["Gestational Hypertension"] == "Yes" else 0
    rf_ehype_dummy = 1 if data["Hypertension Eclampsia"] == "Yes" else 0
    rf_inftr_dummy = 1 if data["Infertility Treatment Used"] == "Yes" else 0
    rf_cesar_dummy = 1 if data["Prior C-Section"] == "Yes" else 0
    ip_gono_dummy = 1 if data["Gonorrhea"] == "Yes" else 0
    ip_syph_dummy = 1 if data["Syphilis"] == "Yes" else 0
    ip_chlam_dummy = 1 if data["Chlamydia"] == "Yes" else 0
    ip_hepb_dummy = 1 if data["Hepatitis B"] == "Yes" else 0
    ip_hepc_dummy = 1 if data["Hepatitis C"] == "Yes" else 0

    previs = 0 # Not available in form, defaulting to 0
    wtgain = data["Weight Gained (lb)"]
    mager = data["Mother Age"]
    bmi = data["Mother BMI"]
    cig_1 = data["Cigarettes in Trimester 1"]
    cig_2 = data["Cigarettes in Trimester 2"]
    cig_3 = data["Cigarettes in Trimester 3"]

    # --- your LP calculation block ---
    LP = -2.5358 \
         -0.1213 * mbraceship_Hispanic \
         -0.2574 * mbraceship_Non_Hispanic_AIAN_only \
         -0.0165 * mbraceship_Non_Hispanic_Black_only \
         -0.0280 * mbraceship_Non_Hispanic_NHOPI_only \
         -0.1509 * mbraceship_Non_Hispanic_White_only \
         -0.0143 * mbraceship_Non_Hispanic_more_than_one_race \
         +0.0668 * has_college_degree \
         +0.0258 * pay_CHAMPUS_TRICARE \
         -0.0274 * pay_Indian_Health_Service \
         +0.1127 * pay_Medicaid \
         +0.2044 * pay_Other_Government \
         +0.2990 * pay_Private_Insurance \
         -0.3351 * region_Midwest \
         -0.2456 * region_Northeast \
         -0.3391 * region_West \
         -0.1760 * dmar_Married \
         +3.6798 * breech_dummy \
         +0.7183 * rf_pdiab_dummy \
         +0.1473 * rf_gdiab_dummy \
         +0.3259 * rf_phype_dummy \
         +0.3500 * rf_ghype_dummy \
         +0.7827 * rf_ehype_dummy \
         +0.9229 * rf_inftr_dummy \
         +3.1173 * rf_cesar_dummy \
         +0.1689 * ip_gono_dummy \
         +0.0531 * ip_syph_dummy \
         -0.0915 * ip_chlam_dummy \
         -0.1116 * ip_hepb_dummy \
         +0.0391 * ip_hepc_dummy \
         +0.0103 * previs \
         +0.0132 * wtgain \
         +0.0106 * mager \
         +0.0222 * bmi \
         +0.0095 * cig_1 \
         -0.0015 * cig_2 \
         -0.0017 * cig_3

    # Output LP
    st.write(f"Calculated LP (Log-Odds): {LP:.4f}")

    # --- Convert LP to probability ---
    probability = 1 / (1 + math.exp(-LP))

    # Display probability 0–1
    st.write(f"Predicted Probability of C-Section: {probability:.4f}")
