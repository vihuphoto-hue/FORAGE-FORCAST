from config import GROQ_API_KEY, GROQ_MODEL, REQUEST_TIMEOUT_SECONDS
import requests

def explain_plan(prompt: str, language: str) -> str:
    """Optional Groq integration. If no key is configured, return a transparent fallback."""
    if not GROQ_API_KEY:
        return (
            "AI advisor is not configured because GROQ_API_KEY is blank in your .env file. "
            "The rule-based recommendations above are still available. Add a Groq API key "
            "only if you choose to enable AI-generated explanations."
        )
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    body = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": (
                "You are a cautious rangeland planning assistant for a student prototype. "
                "Reply in the requested language. Do not invent measurements, local laws, "
                "water availability, forage biomass, or certainty. Explain uncertainty. "
                "Never override the calculated forage budget or ecological safety warnings. "
                "Give practical, sustainable options and recommend local expert validation."
            )},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 900
    }
    r = requests.post(url, headers=headers, json=body, timeout=REQUEST_TIMEOUT_SECONDS + 10)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
