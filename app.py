import streamlit as st

st.title('Medical Insurance Demo')

st.markdown('Please input your data and we\'ll give you a prediction of your medical insurance charge.')

with st.form("form"):
	# age (18, 64)
	age = st.slider('Age', 18, 64)
	# sex (m, f)
	sex = st.selectbox('Sex',('m', 'f'))
	# bmi (16, 53.1)
	bmi = st.slider('BMI', 16, 54)
	# children (0, 5)
	children = st.slider('Children number', 0, 5)
	# smoker (y, n)
	smoker = st.selectbox('Are you a smoker?',('yea', 'nah'))
	# region (southeast, southwest, other)
	region = st.selectbox('Select a region',('southeast', 'southwest', 'other'))
	# charges

	submitted = st.form_submit_button("Submit")

