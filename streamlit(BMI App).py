import streamlit as st
import pandas as pd
import time as t
from datetime import date
st.markdown("<h3 style = 'color:rgb(190,168,120);'># BMI Calculator By Prasanth 😉</h3>",unsafe_allow_html=True)

if "user_text" not in st.session_state:
    st.session_state.user_text = ""

if "clear_text" not in st.session_state:
    st.session_state.clear_text = False

if st.session_state.clear_text:
    st.session_state.user_text = ""
    st.session_state.clear_text = False 
with st.sidebar:
    st.date_input("Today Date:")
    st.time_input("Current Time:")
    st.title("Contents:")
    st.caption("1.Track your Health with quick BMI check")

    st.text_area("Feedback: ",placeholder="Type here....",key ="user_text")
    if st.button("Submit"):
        st.session_state.clear_text = True
        st.write("Your feedback has been recorded")
    def level1():
        st.sidebar.warning("⚠️Low BMI") 
    def level2():
           st.sidebar.success("✅️Normal BMI")
    def level3():
           st.sidebar.error("🚨High BMI")
    with st.expander("ℹ️ Health Tips"):
        st.write("- Stay hydrated")
        st.write("- Maintain balanced diet")
        st.write("- Exercise regularly")
    def format_stars(x):
        return "★" * x + "☆" * (5 - x)
    st.header("🌟 Rate This App")
    rating = st.selectbox(
        "Your Rating:",
        options=list(range(1, 6)),
        format_func=format_stars
    )
    if st.button("submit"):
        if rating == 4 or rating == 5:
            st.balloons()
        st.success("Thanks for rating! 🙏")
    st.page_link(
        page="https://www.healthline.com/nutrition/27-health-and-nutrition-tips#meditation",
        label="➡️ Go to this healthline Page",
        icon=":material/navigate_next:"
    )
    
name = st.text_input("Enter Your Name:")
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f",step=0.1)

height_unit = st.selectbox("Select your height unit:", ['Centimeters', 'Meters', 'Feet'])
st.caption(f"You Preferred {height_unit}")

height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f",step=1.0)

if st.button("Calculate BMI"):
    with st.spinner("Please Wait"):
        t.sleep(2)
    try:
        if height_unit == 'Centimeters':
            height_m = height / 100
        elif height_unit == 'Feet':
            height_m = height / 3.28
        else:
            height_m = height

        if height_m <= 0:
            st.error("Height must be greater than zero.")
        if weight <= 0:
            st.error("Weight must be greater than zero.")
        else:
            bmi = weight / (height_m ** 2)
            st.session_state.bmi = bmi
            st.success(f"Your BMI is {bmi:.2f}")

    except:
        st.error("Please enter valid numeric values.")

if "bmi" in st.session_state:
    bmi = st.session_state.bmi
    if  bmi < 18.5:
        st.warning(f"{name},You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success(f"{name},You are normal weight")
    elif 25 <= bmi < 40:
        st.error(f"{name},You are Overweight")
    bmi_slider = st.slider("Weight Category :",min_value=5.0,max_value=40.0,value=bmi)    
    
    if bmi_slider < 18.5:
        st.caption("Underweight")
        level1()

    elif bmi_slider >= 18.5 and bmi_slider < 25:
        st.caption("Normal")
        level2()
          
    elif bmi_slider >= 25 and bmi_slider < 40:
        st.caption("Overweight")
        level3()

workout_data = [
    {"Day":"Monday","Focus Area":"Chest & Triceps","Exercises":"Bench Press; Tricep Dips","Sets × Reps":"4×8; 3×12","Duration (min)":60,"Est. Calories":400},
    {"Day":"Tuesday","Focus Area":"Back & Biceps","Exercises":"Pull-ups; Barbell Row; Bicep Curls","Sets × Reps":"4×6; 4×8; 3×10","Duration (min)":60,"Est. Calories":380},
    {"Day":"Wednesday","Focus Area":"Cardio","Exercises":"Treadmill Run (steady)","Sets × Reps":"","Duration (min)":30,"Est. Calories":300},
    {"Day":"Thursday","Focus Area":"Legs","Exercises":"Squats; Lunges; Leg Press","Sets × Reps":"4×8; 3×12; 3×10","Duration (min)":60,"Est. Calories":420},
    {"Day":"Friday","Focus Area":"Shoulders","Exercises":"Overhead Press; Lateral Raises","Sets × Reps":"4×8; 3×12","Duration (min)":60,"Est. Calories":350},
    {"Day":"Saturday","Focus Area":"Full Body HIIT","Exercises":"Burpees; Jump Squats; Mountain Climbers","Sets × Reps":"5 rounds","Duration (min)":45,"Est. Calories":500},
    {"Day":"Sunday","Focus Area":"Rest & Stretch","Exercises":"Yoga; Foam Rolling","Sets × Reps":"","Duration (min)":30,"Est. Calories":150},
]

Workout_Plan = pd.DataFrame(workout_data)
csv_str = Workout_Plan.to_csv(index=False)
          
st.download_button(
    "🗂️Download Weekly Routine",
    data=csv_str.encode("utf-8"),
    file_name="Workout_Plan.csv",
    mime="text/csv"
)
default_date = date.today()
BMI_Check = st.date_input("Update Your Next Bmi Check:",value = default_date,min_value=date(2025,9,2),max_value=date(2030,12,31))

st.warning(f"⚠️ Your Next Remainder For BMI Check is '{BMI_Check}'")

