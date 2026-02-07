# pulsecheck-ai
⚡ PulseCheck AI: Real-Time Tech Intelligence
A high-speed RAG (Retrieval-Augmented Generation) pipeline for live tech news analysis.

📖 Project Overview
PulseCheck AI is a lightweight intelligence tool designed to solve "information overload" for tech professionals. Instead of manually scrolling through multiple RSS feeds, this tool fetches live signals, processes them through a Stateless RAG pipeline, and generates a high-level executive summary in seconds.

Why this exists:
Context over Noise: Uses LLMs to distinguish between "Hype" and "Reality" in tech news.

Speed-First Architecture: Built on Groq's LPU Inference Engine to achieve 300+ tokens/second.

Production Ready: Fully containerized with Docker for consistent deployment.

🛠️ Technical Stack
LLM: Llama 3.3 70B (via Groq Cloud API)

Backend: Python 3.10

Frontend: Streamlit (Custom Slate-Mint Theme)

Data Sources: Real-time RSS Feeds (TechCrunch, HackerNews, The Verge)

DevOps: Docker & Docker Compose

🏗️ Architecture & Logic
PulseCheck uses a Stateless RAG approach. Unlike traditional RAG that requires a persistent Vector Database, this project performs "In-Memory Retrieval":

Fetch: Parallelized parsing of multiple XML RSS streams.

Context Injection: Live headlines are sanitized and injected directly into the LLM system prompt.

Reasoning: The LLM acts as a "Cyberpunk Intelligence Officer" to synthesize the data packets.

Live Monitoring: Implemented a custom LogCapture class to stream container internal logs directly to the UI for transparent debugging.

🚀 Getting Started
Prerequisites
Groq API Key (Free Tier)

Docker & Docker Compose installed

🧠 Key Challenges & Learning
Circular Dependencies: Resolved a major architectural bottleneck where the UI and LLM client were tightly coupled, leading to circular import errors.

Docker Pathing: Overcame Streamlit component pathing issues within Linux containers by implementing a native HTML/JS Lottie player rather than relying on standard Python wrappers.