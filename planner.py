# planner.py
import subprocess
import json

PROMPT_TEMPLATE = """
You are a helpful healthcare assistant. Based on the user's natural language input, generate a personalized DAILY CARE PLAN in JSON format. 

Ensure the plan includes relevant medications, meals, exercises, rest, and notes. Each section must be a structured list of JSON objects.

User Input:
"{user_input}"

Output format (JSON only):

{{
  "medications": [
    {{
      "name": "Metformin",
      "dose": "500mg twice a day",
      "time": ["morning", "evening"]
    }}
  ],
  "meals": [
    {{
      "meal": "breakfast",
      "suggestions": ["oatmeal with fruit and nuts", "scrambled eggs with whole-grain toast"]
    }},
    {{
      "meal": "lunch",
      "suggestions": ["grilled chicken salad", "quinoa with vegetables"]
    }},
    {{
      "meal": "dinner",
      "suggestions": ["baked salmon with brown rice", "vegetable stir-fry"]
    }}
  ],
  "exercise": [
    {{
      "activity": "short walk",
      "duration": "30 minutes",
      "frequency": "twice a day"
    }}
  ],
  "rest": [
    {{
      "amount": "7-8 hours",
      "time": ["night"]
    }}
  ],
  "notes": [
    "Monitor blood sugar levels regularly.",
    "Encourage physical activity to improve health.",
    "Consult a doctor before taking or changing medications."
  ]
}}
"""

def query_ollama(user_input: str, model="llama3") -> dict:
    prompt = PROMPT_TEMPLATE.format(user_input=user_input)
    try:
        result = subprocess.run(["ollama", "run", model], input=prompt, text=True, capture_output=True)
        response = result.stdout
        # Try to extract JSON from response
        start = response.find("{")
        end = response.rfind("}") + 1
        json_str = response[start:end]
        return json.loads(json_str)
    except Exception as e:
        return {"error": str(e)}

def query_empathy_bot(user_message: str, model="llama3") -> str:
    empathy_prompt = f"""
You are a compassionate mental health assistant. A caregiver says: "{user_message}". 
Respond with warmth, empathy, and emotional validation to help them feel heard and supported.  also give advice where appropriate.
Keep your response under 80 words. Do not include technical or clinical advice. No JSON, just natural language.
"""
    try:
        result = subprocess.run(["ollama", "run", model], input=empathy_prompt, text=True, capture_output=True)
        return result.stdout.strip()
    except Exception as e:
        return f"⚠️ Error generating response: {str(e)}"