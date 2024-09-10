# Load the required libraries
from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

# Load the API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the function to get the response from the Gemini API
def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

# Define the function to convert the PDF to image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())
        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="ATS Resume Checker")
st.header("ATS Resume Checking Tool")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your Resume (PDF)",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Analyse the Resume")
submit3 = st.button("Match the Resume with Job Description")

# Define the input prompts
input_prompt1 = """
 You are an experienced Technical Human Resource Manager for Technology recruitments. Your task is to review the provided resume against the job description. 
 Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. Also, provide drafts for changes that should be made as seen in the resume.
"""
input_prompt3 = """
You are a sophisticated ATS (Applicant Tracking System) scanner with a deep understanding of data science, analytics and data engineering and ATS functionality.
You are able to evaluate resumes and job descriptions to determine the percentage match between the two. You are also well versed in recruiting for big techs like Microsoft, Google, Amazon, Facebook, Apple, Netflix, and LinkedIn.
Your task is to evaluate the resume against the provided job description. After evaluating, you will provide an accurate percentage of match based on your evaluation. Your response should always be in the following format:
Percentage Match: % \n
Job Title Match: Yes/No \n
Education Match: Yes/No \n
Hard Skills Match: \n
    Found Skills: list out skills as bullet points\n
    Missing Skills: list out skills as bullet points\n
Tips to Improve: 
"""

# Run logic based on the button click
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("Here is the Evaluation of your Resume:")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   





