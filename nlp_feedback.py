# File: src/nlp_feedback.py

from transformers import pipeline

# load a grammar‑correction pipeline from Hugging Face
grammar_check = pipeline(
    "text2text-generation",
    model="vennify/t5-base-grammar-correction"
)

def correct_grammar(sentence: str) -> str:
    """
    Takes a sentence and returns the corrected version.
    """
    result = grammar_check(sentence, max_length=256)
    return result[0]["generated_text"]
