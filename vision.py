from dotenv import load_dotenv

load_dotenv() # Loading all the environment variables

import streamlit as st

import os

import google.generativeai as genai

from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load gemini pro  model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


# Function to load gemini pro  model and get responses
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input !="":

     response=model.generate_content([input,image])
    elif input=="" :
     response=model.generate_content(image)
    else:
     print("Both input and image are empty. Please provide at least one.")

    return response.text




# Initialize the streamlit app
st.set_page_config(page_title="Q/A Demonstration")

st.header("Basic Gemini Pro LLM Application")

input=st.text_input("INPUT:  ",key="input")

submit=st.button("Ask the question")
  
uploaded_file=st.file_uploader("Chose an image....",type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
   image=Image.open(uploaded_file)
   st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell me about the image")

#  If submit is clicked

if submit:
  
 response=get_gemini_response(input,image)


 st.subheader("The response is")
 st.write(response)


