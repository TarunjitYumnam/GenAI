#Text Generation from Gemini API
import google.generativeai as genai
genai.configure(api_key = "AP_KEY")
model = genai.GenerativeModel("gemini-pro")

import re
def responses(question):
  response = model.generate_content(question)
  response = re.sub(r'[\n\-\_\*]',' ',response.text)
  response = re.sub(r'\s+',' ',response).strip()
  return response
  
usr_qsn = input("Enter your Doubt: ")
responses(usr_qsn)
#Image Info genegartion from gemini-1.5-flash
img_model = genai.GenerativeModel("gemini-1.5-flash")
from PIL import Image
def image_details():
  res = Image.open('IMG_8607.JPG')
  res = img_model.generate_content(res)
  return res.text
image_details()
