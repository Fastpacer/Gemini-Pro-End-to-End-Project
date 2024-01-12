Exploring Google’s Gemini Pro API: Two Streamlit Applications
This project is a beginner-friendly guide to building web applications using Streamlit and Google’s Gemini Pro API. It consists of two distinct Streamlit applications that leverage the power of Language Model Learning (LLM).

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.6 or higher
pip (Python Package Installer)
Installation
Create a Virtual Environment: To avoid conflicts with other projects, it’s a good practice to create a virtual environment. Here’s how you can do it:
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

Install Required Packages: Once you’ve activated the virtual environment, you can install the required packages using pip:
pip install -r requirements.txt

Get Google Gemini Pro API Key: You’ll need a Google Gemini Pro API key to run the applications. Here’s how you can get it:
Go to the Google Gemini website
Follow the instructions to create a new project and enable the Gemini Pro API
Once the API is enabled, create credentials for the API and copy the API key
Set Up API Key: Create a config.py file in the project directory and add your API key:
Python

# config.py
API_KEY = 'your-api-key'
AI-generated code. Review and use carefully. More info on FAQ.
Remember to replace 'your-api-key' with your actual API key.

Running the Applications
You can run the applications using the following command:
streamlit run app.py

Open your web browser and you will be direxted to your localhost.

You can deploy this pre-eminent basic model on cloud accompanied with some further modifications if you deem it to be necessary.

