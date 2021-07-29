import streamlit as st

from modelExecutor import getCost

st.title("Medical Insurance Demo")

st.markdown(
    "Please input your data and we'll give you a prediction of your medical insurance charge."
)

with st.form("form"):
    # age (18, 64)
    age = st.slider("How old are you?", 18, 64)
    # sex (m, f)
    sex = st.selectbox("What is your Sex?", ("m", "f"))
    # bmi (16, 53.1)

    height = st.slider("What is your height? (cm)", 100, 210)
    weight = st.slider("How much do you weight? (Kg)", 20, 160)

    # bmi = st.slider("BMI", 16, 54)
    # children (0, 5)
    children = st.slider("How many children do you have?", 0, 5)
    # smoker (y, n)
    smoker = st.selectbox("Are you a smoker?", ("yes", "no"))
    # region (southeast, southwest, other)
    region = st.selectbox(
        "Select a region", ("northeast", "northwest", "southeast", "southwest")
    )
    # charges

    submitted = st.form_submit_button("Calculate price")

    if submitted:
        bmi = weight / (height / 100) ** 2
        cost = getCost(age, sex, bmi, children, smoker, region)
        st.write(
            "You would have to pay ", f"${round(cost,2)}", "dollars for your insurance."
        )
