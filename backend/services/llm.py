import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_recommendation(disease):

    prompt = f"""
 You are an agricultural expert.

 Disease:
  {disease}

 Provide:

 🌿 Disease Description

 ⚠️ Causes

 💊 Treatment

  🛡️ Prevention

 Keep response under 200 words.
 Use bullet points.
     """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content