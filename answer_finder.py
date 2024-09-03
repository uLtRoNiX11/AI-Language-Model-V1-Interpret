import google.generativeai as genai

# Replace with your Gemini API key (if required)
gemini_api_key = "ENTER YOUR GEMINI API KEY HERE" 

def get_answer(question):

  # Configure the Gemini API client (if necessary)
  if gemini_api_key:
      genai.configure(api_key=gemini_api_key)

  # Send the question to the Gemini model
  response = genai.GenerativeModel(model_name="gemini-1.5-flash").generate_content(question)
  return response.text
