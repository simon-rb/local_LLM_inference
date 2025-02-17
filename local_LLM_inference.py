import time  # Used to measure response time
import multiprocessing  # Helps determine available CPU threads
from llama_cpp import Llama  # Import Llama.cpp for local LLM execution

# Path to the GGUF model file
MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# Optimized performance settings
NUM_THREADS = min(
    6, multiprocessing.cpu_count()
)  # Auto-adjust based on available CPU cores
N_CTX = 3072  # Context size (affects memory & conversation retention)
N_BATCH = 1024  # Number of tokens processed per batch (higher = faster)
MAX_TOKENS = 256  # Limit response length
MAX_HISTORY = 5  # Keep conversation history short to optimize memory


def load_model():
    """Loads the LLM model with optimized settings."""
    print("Loading model... (this takes a few seconds)")
    return Llama(
        model_path=MODEL_PATH,  # Path to the model file
        n_ctx=N_CTX,  # Set context size for conversation memory
        n_threads=NUM_THREADS,  # Optimize CPU usage
        n_batch=N_BATCH,  # Optimize batch size for faster token generation
        chat_format="mistral-instruct",  # Ensures proper chat-style responses
        temperature=0.2,  # Controls randomness (lower = more deterministic)
        top_p=0.9,  # Filters token probabilities (higher = more diverse responses)
        verbose=False,  # Suppress unnecessary debug logs
        n_gpu_layers=35,  # Offloads computation to GPU for speed (Mac MPS optimization)
    )


def run_chatbot():
    """Runs the chatbot in an interactive loop."""
    llm = load_model()  # Load the AI model
    chat_history = []  # Stores conversation history

    print("\nChatbot is ready! Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()  # Get user input
            if user_input.lower() in {"exit", "quit"}:  # Exit condition
                print("Exiting chatbot. Goodbye!")
                break
            if not user_input:  # Ignore empty input
                continue

            # Maintain a limited chat history to avoid memory bloating
            if len(chat_history) >= MAX_HISTORY:
                chat_history.pop(0)  # Remove oldest message to keep history short

            # Append user input to chat history
            chat_history.append({"role": "user", "content": user_input})

            # Measure response time
            start_time = time.time()
            response = llm.create_chat_completion(
                messages=chat_history,  # Provide chat history for context
                max_tokens=MAX_TOKENS,  # Limit response length
                stop=["\n"],  # Stop response at a newline
            )
            end_time = time.time()

            # Extract and clean response
            bot_response = response["choices"][0]["message"]["content"].strip()
            print("\nBot:", bot_response)
            print(f"\nResponse time: {end_time - start_time:.2f} seconds\n")

            # Append bot response to history
            chat_history.append({"role": "assistant", "content": bot_response})

        except KeyboardInterrupt:
            print("\n\nChatbot interrupted. Exiting...\n")
            break
        except Exception as e:
            print(f"\n⚠️ Error: {e}\n")


if __name__ == "__main__":
    run_chatbot()  # Run chatbot if script is executed directly
