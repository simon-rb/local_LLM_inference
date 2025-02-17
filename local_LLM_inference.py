from llama_cpp import Llama  # Import Llama.cpp for local LLM execution

def load_model():
    """Loads the LLM model with optimized settings."""
    return Llama(
        model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",  # Path to the downloaded model
        n_gpu_layers=35,  # Offloads computation to GPU for better performance (Mac MPS optimization)
        verbose=False  # Suppresses unnecessary debug outputs for a clean terminal experience
    )

def run_chatbot():
    """Runs the chatbot in an interactive loop."""
    llm = load_model()  # Load the AI model

    print("\nChatbot ready! Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            # Get user input and clean up whitespace
            user_input = input("You: ").strip()
            
            # 🔹 Check for exit command
            if user_input.lower() in {"exit", "quit"}:
                print("\nExiting chatbot. Goodbye!\n")
                break  # Exit the loop
            
            # 🔹 Generate response from the model
            response = llm.create_chat_completion(
                messages=[{"role": "user", "content": user_input}]  # Pass user input as a chat message
            )

            # 🔹 Extract and clean the bot's response
            bot_response = response["choices"][0]["message"]["content"].strip()

            # Print the chatbot's response
            print("\nBot:", bot_response, "\n")

        except KeyboardInterrupt:
            print("\n\nChatbot interrupted. Exiting...\n")
            break  # Handle Ctrl + C interruption gracefully
        except Exception as e:
            print(f"\n⚠️ Error: {e}\n")  # Catch unexpected errors without crashing

if __name__ == "__main__":
    run_chatbot()  # Run chatbot only when the script is executed directly
