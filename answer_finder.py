import google.generativeai as genai

# Replace with your Gemini API key (if required)
gemini_api_key = "AIzaSyDJ2qZy3w4YIw9_SOw6xpSfKBB-6mJIAcY" 

def get_answer(question):

  # Configure the Gemini API client (if necessary)
  if gemini_api_key:
      genai.configure(api_key=gemini_api_key)

  # Send the question to the Gemini model
  response = genai.GenerativeModel(model_name="gemini-1.5-flash").generate_content(question)
  return response.text
