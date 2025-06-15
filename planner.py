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
    # Simulated static response (mocked care plan)
    return {
        "medications": [
            {"name": "Metformin", "dose": "500mg twice a day", "time": ["morning", "evening"]}
        ],
        "meals": [
            {"meal": "breakfast", "suggestions": ["Oatmeal with fruit", "Boiled eggs and toast"]},
            {"meal": "lunch", "suggestions": ["Grilled chicken salad", "Quinoa with vegetables"]},
            {"meal": "dinner", "suggestions": ["Baked salmon with rice", "Veggie stir fry"]}
        ],
        "exercise": [
            {"activity": "Stretching and short walk", "duration": "20 minutes", "frequency": "twice a day"}
        ],
        "rest": [
            {"amount": "8 hours", "time": ["night"]}
        ],
        "notes": [
            "Monitor blood sugar levels regularly.",
            "Avoid high-sugar snacks.",
            "Encourage regular physical activity."
        ]
    }


def get_emotional_response(user_msg):
    return "I'm here for you. It’s okay to feel overwhelmed — you're doing an amazing job. 💖"
