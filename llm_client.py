import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_trends(news_list):
    print("🧠 Engaging LLM for Trend Analysis...")
    
    context = "\n".join([f"- [{n['source']}] {n['title']}" for n in news_list])
    
    prompt = f"""
    Act as a Senior Tech Analyst. Summarize these signals:
    {context}
    
    Format as:
    - **SUMMARY**: (3 bullets)
    - **THE VIBE**: (One sentence)
    """
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    
    print("📊 Analysis complete.")
    return completion.choices[0].message.content