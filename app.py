from dotenv import load_dotenv

load_dotenv() # Loading all the environment variables

import streamlit as st

import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load gemini pro  model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text



# Initialize the streamlit app
st.set_page_config(page_title="Q/A Demonstration")

st.header("Basic Gemini Pro LLM Application")

input=st.text_input("INPUT:  ",key="input")

submit=st.button("Ask the question")
  
# When Submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response Is:  ")
    st.write(response)
