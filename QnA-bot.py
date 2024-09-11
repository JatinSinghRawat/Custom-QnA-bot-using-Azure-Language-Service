pip install streamlit requests
import streamlit as st
import requests

# Azure Language Service credentials
AZURE_ENDPOINT = "YOUR_AZURE_ENDPOINT_URL"  # Replace with your Azure endpoint URL
AZURE_API_KEY = "YOUR_AZURE_API_KEY"  # Replace with your Azure API key
AZURE_PROJECT_NAME = "YOUR_PROJECT_NAME"  # Replace with your project name
AZURE_DEPLOYMENT_NAME = "YOUR_DEPLOYMENT_NAME"  # Replace with your deployment name

# Function to query the Azure Custom QnA bot
def get_qna_response(question):
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_API_KEY,
        "Content-Type": "application/json"
    }
    url = f"{AZURE_ENDPOINT}/language/query-knowledgebases/projects/{AZURE_PROJECT_NAME}/deployments/{AZURE_DEPLOYMENT_NAME}/qna?api-version=2021-10-01"

    body = {
        "question": question,
        "top": 1
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        return data['answers'][0]['answer']
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
st.title("Azure Custom QnA Bot")
st.write("Ask a question to the bot:")

# Input text box
user_question = st.text_input("Your question:")

# Submit button
if st.button("Submit"):
    if user_question.strip() != "":
        answer = get_qna_response(user_question)
        st.write(f"**Bot's response:** {answer}")
    else:
        st.write("Please enter a question.")
