from transformers import pipeline
from transformers.pipelines import PipelineException
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# Load a publicly available grammar correction model
model_name = "vennify/t5-base-grammar-correction"
try:
    corrector = pipeline("text2text-generation", model=model_name, tokenizer=model_name)
except Exception as e:
    logging.error(f"Error loading model: {e}")
    print("❌ Failed to load the grammar correction model. Please check your setup.")
    exit(1)

def correct_grammar(sentence):
    """
    Corrects the grammar of the given sentence using the loaded model.
    """
    if not sentence.strip():
        return "⚠️ Error: Input sentence is empty."

    try:
        # Provide a clear instruction to the model
        prompt = f"Correct the grammar of this sentence: {sentence}"
        corrected = corrector(prompt, max_length=256)
        return corrected[0]['generated_text'].strip()
    except PipelineException as e:
        logging.error(f"PipelineException during grammar correction: {e}")
        return "⚠️ Error during grammar correction. Please try again."
    except Exception as e:
        logging.error(f"Unexpected error during grammar correction: {e}")
        return "⚠️ An unexpected error occurred. Please try again."

def simulate_tutor_session():
    """
    Simulates an interactive tutor session for grammar correction.
    """
    print("👋 Welcome to the Grammar Correction Tutor!")
    print("💡 Type 'exit' anytime to quit the program.")

    while True:
        print("\n📝 Enter a sentence you'd like to correct:", end=" ")
        sentence = input().strip()

        if sentence.lower() == "exit":
            print("👋 Goodbye!")
            break

        if not sentence:
            print("⚠️ Please enter a valid sentence.")
            continue

        corrected = correct_grammar(sentence)
        print("\n✍️ Grammar Correction:")
        print(f"  Original: {sentence}")
        print(f"  Corrected: {corrected}")

        print("\n💡 Tip: Review your corrected sentence carefully.")

if __name__ == "__main__":
    simulate_tutor_session()