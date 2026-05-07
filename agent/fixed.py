import json
import os

from openai import OpenAI
from dotenv import load_dotenv

from agent.prompts import SYSTEM_PROMPT, FIX_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class FixGenerator:
    def generate_fix(self, error: str, category: str):
        prompt = FIX_PROMPT.format(
            category=category,
            error=error,
        )

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except Exception:
            return {
                "issue": error,
                "category": category,
                "recommended_fix": content,
                "confidence": 0.75,
            }