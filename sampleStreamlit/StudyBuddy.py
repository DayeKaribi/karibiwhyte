import streamlit as st
from PIL import Image
import google.generativeai as genai

#Gemini Set up
genai.configure(api_key='AIzaSyC_w0m3syV9Yno8jqYQ5GOIxJnTUpV7Wvk')

model = genai.GenerativeModel('gemini-pro-vision')

st.title("Welcome to your personal study buddy!")
st.text("")
st.write("Having trouble with studying? We got you covered! Study buddy is a personalized web app that will aid you in all your academic endeavors!")
st.text("")
st.write("Steps: ")
st.text("")

st.write("1. Select the subjects you want study buddy to help you with.\n")
st.write("2. Once selected, describe the issues you have per subject.")
st.write("3. Upload any files or images that Study buddy needs to further aid your studying.")
st.write("4. Click “Generate response” and watch your Study Buddy go!")
st.write("5. If you are unsatisfied with the response, explain your concerns in the “Additional information” textbox for the buddy to reevaluate their answer")
st.text("")
subjects = st.multiselect("What subject do you need help studying for?", ["Mathematics", "Science", "English", "History", "Health", "Engineering", "Computer Science", "Other"], help="This is a dropdown for all your classes")
st.text("")
if subjects:
    st.write("Great! What are you struggling with in these subjects?")
else:
    st.write("Please select a subject")
userInput = ""
if "Mathematics" in subjects:
  userInput += " Mathematics: " +  st.text_input("Mathematics", help= "Ex: Can’t figure out how to do an equation; need practice problems for derivatives")
if "Science" in subjects:
   userInput += " Science: " + st.text_input("Science", help= "Ex: Breakdown the rock cycle")
if "English" in subjects:
  userInput += " English " + st.text_input("English", help= "Ex: How to write a better essay")
if "History" in subjects:
   userInput += " History " + st.text_input("History", help= "Ex: What was the main cause of the American Revolution?")
if "Health" in subjects:
  userInput += " Health " +  st.text_input("Health", help= "Ex: How to lose weight")
if "Engineering" in subjects:
  userInput += " Engineering " +st.text_input("Engineering", help= "Ex: How to design a bridge")
if "Computer Science" in subjects:
   userInput += " Computer Science: " + st.text_input("Computer Science", help= "Ex: How to code a website")
if "Other" in subjects:
  userInput += " Other " + st.text_input("Other", help= "First describe the course then describe your issues")

st.write("Upload any files that we might need to better help your understanding:")
homework_file = st.file_uploader("Upload here",accept_multiple_files=False)
response_click = st.button("Generate Response")
if homework_file is not None:
  img = Image.open(homework_file)
  st.header("here is the picture you submitted: ")
  st.image(img)
  if response_click:
    response = model.generate_content(['Help the person with their subjects based off this input: ' + userInput, img])
    response.resolve()
    st.write("Study Buddy's Response: ")
    st.write(response.text)
if response_click:
    response = model.generate_content('Help the person with their subjects based off this input: ' + userInput)
    response.resolve()
    st.write("Study Buddy's Response: ")
    st.write(response.text)