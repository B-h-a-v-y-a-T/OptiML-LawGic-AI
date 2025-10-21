import os
import numpy as np

try:
    import google.generativeai as genai
except ImportError:
    genai = None  # type: ignore


GEMINI_API_KEY = (os.getenv("GEMINI_API_KEY") or os.getenv("AI_API_KEY") or "").strip()
GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL") or "models/text-embedding-004"

if genai is not None and GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as exc:
        print(f"⚠️ Gemini embedding client failed to initialize: {exc}")
elif genai is None:
    print("⚠️ google-generativeai not installed. Using dummy embeddings.")
else:
    print("ℹ️ Set GEMINI_API_KEY or AI_API_KEY to enable live embeddings")

async def get_embedding(text: str) -> list:
    """
    Returns vector embedding for a given text.
    Falls back to dummy embeddings if OpenAI is not available.
    """
    if genai is None or not GEMINI_API_KEY:
        # Return a dummy embedding vector for demo purposes
        # In a real scenario, you might use a different embedding model
        np.random.seed(hash(text) % (2**32))  # Consistent random seed based on text
        return np.random.random(1536).tolist()  # OpenAI embedding size
    
    try:
        embedding = genai.embed_content(
            model=GEMINI_EMBED_MODEL,
            content=text,
        )
        data = embedding.get("embedding")
        if data:
            return data
        raise ValueError("Embedding payload missing 'embedding' field")
    except Exception as exc:
        print(f"⚠️ Embedding generation failed: {exc}")
        # Fallback to dummy embedding
        np.random.seed(hash(text) % (2**32))
        return np.random.random(1536).tolist()
