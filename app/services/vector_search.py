import math
from typing import List, Tuple

def mock_text_embedding(text: str) -> List[float]:
    """Generate deterministic pseudo-embedding vector for text similarity matching."""
    words = text.lower().split()
    vector = [0.0] * 16
    for idx, word in enumerate(words):
        for char_idx, char in enumerate(word):
            vector[(ord(char) + idx) % 16] += 1.0
    
    # Normalize vector
    magnitude = math.sqrt(sum(v * v for v in vector)) or 1.0
    return [v / magnitude for v in vector]

def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    dot_product = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1)) or 1.0
    mag2 = math.sqrt(sum(b * b for b in v2)) or 1.0
    return round(dot_product / (mag1 * mag2), 4)
