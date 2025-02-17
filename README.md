# **🚀 Running a Local LLM: Mistral 7B on Mac (Fully Offline)**
### **Workshop Guide – Secure, Private AI Deployment**
**GitHub Repo:** [local_LLM_inference](https://github.com/simon-rb/local_LLM_inference.git)

---

## **🔹 Overview**
This guide walks you through **deploying and running a Large Language Model (LLM) locally on your Mac**.  
This allows you to run an AI chatbot **fully offline**—no internet required.

For this example, we will use **Mistral-7B-Instruct**, but you can replace it with **any GGUF-compatible model** like **Qwen, Llama, DeepSeek**, etc.

---

## **📂 1. Clone the Repository**
First, download all required files from the GitHub repository:

```bash
git clone https://github.com/simon-rb/local_LLM_inference.git
cd local_LLM_inference
```

> **What’s inside?**  
> - `README.md` → This guide  
> - `local_inference.py` → The Python script to run the chatbot  

---

## **🔹 2. Install Required Software**
Before running the chatbot, we need to install some **essential tools**.

### **✅ 1. Install Homebrew (Mac’s Package Manager)**
If you don’t have **Homebrew**, install it first (it makes installing other tools much easier):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify the installation:
```bash
brew --version
```

---

### **✅ 2. Install Python 3.9+**
Check if Python is installed:

```bash
python3 --version
```

If you don’t have **Python 3.9 or later**, install it via Homebrew:

```bash
brew install python
```

Verify that Python is installed:
```bash
python3 --version
```

---

### **✅ 3. Install Pip (Python Package Manager)**
Ensure **pip** is installed:

```bash
python3 -m ensurepip --default-pip
```

Upgrade pip:

```bash
pip install --upgrade pip
```

---

### **✅ 4. Install Required Python Libraries**
Now, install `llama-cpp-python`, which enables local AI execution:

```bash
pip install llama-cpp-python
```

> **Why?**  
> - This library runs **GGUF models** efficiently on **Mac (MPS), CPU, and GPU**.  
> - Works for various LLMs like **Mistral, Qwen, Llama, and DeepSeek**.  

---

## **🔹 3. Download the AI Model**
We use **Mistral-7B-Instruct-Q4_K_M**, optimized for **local inference**, but you can **choose any other GGUF model**.

### **1️⃣ Install Hugging Face CLI**
We will use **Hugging Face** to download the model:

```bash
pip install huggingface-hub
```

### **2️⃣ Download the Mistral Model**
Run this command to download **Mistral-7B-Instruct-Q4_K_M** (~4GB):

```bash
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
mistral-7b-instruct-v0.2.Q4_K_M.gguf --local-dir models \
--local-dir-use-symlinks False
```

> **Want a different model?**  
> You can replace `Mistral-7B-Instruct` with another GGUF model, such as:
> - **Qwen2.5-7B**: `huggingface-cli download TheBloke/Qwen2.5-7B-GGUF ...`
> - **Llama 2-7B**: `huggingface-cli download TheBloke/Llama-2-7B-GGUF ...`
> - **DeepSeek 7B**: `huggingface-cli download TheBloke/DeepSeek-7B-GGUF ...`

### **3️⃣ Move the Model to the Correct Folder**
```bash
mkdir -p ~/local-llm/models
mv models/mistral-7b-instruct-v0.2.Q4_K_M.gguf ~/local-llm/models/
```

---

## **🔹 4. Running the Local Chatbot**
Now that everything is installed, you can run the chatbot.

### **1️⃣ Navigate to the Script**
```bash
cd local_LLM_inference
```

### **2️⃣ Run the Chatbot**
```bash
python3 local_inference.py
```

> **If everything is set up correctly, you should see:**  
> `Chatbot is ready! Type 'exit' to quit.`  

### **3️⃣ Start Chatting**
Once the chatbot is running, type in a question, and it will respond.

Example:
```
You: What is quantum mechanics?
Bot: Quantum mechanics is a fundamental theory in physics that describes the behavior of particles at the smallest scales.
```

To **exit the chatbot**, type:
```
exit
```

---

## **🔹 5. Understanding the Code (`local_inference.py`)**
### **What Does This Script Do?**
1. **Loads a local AI model** (default is **Mistral-7B**, but can be changed).  
2. **Optimizes performance** using **CPU & GPU acceleration**.  
3. **Maintains conversation memory** for multi-turn interactions.  
4. **Runs an interactive chatbot loop** where users can ask questions.  
5. **Measures response time** to track performance.  

### **Key Code Components**
```python
from llama_cpp import Llama

# Load the model with optimized settings
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",  # Path to model
    n_ctx=3072,  # How much history the model remembers
    n_threads=6,  # Number of CPU threads to use
    n_batch=1024,  # Number of tokens processed in a batch
    chat_format="mistral-instruct",  # Ensures conversational behavior
    temperature=0.2,  # Keeps responses factual (lower randomness)
    top_p=0.9,  # Controls response diversity
    n_gpu_layers=35,  # Moves more computation to GPU (Mac optimization)
)
```

---

## **🔹 6. Troubleshooting**
### **Q: The chatbot is running too slow!**
✅ Try:
- Lowering `N_CTX` to `2048`  
- Using a smaller quantized model (`Q3_K_M`)  
- Increasing `n_gpu_layers=35` for **Mac GPU acceleration**  

### **Q: I want to use a different model (like Qwen or Llama). How do I do that?**
✅ Just download the **GGUF file** for your chosen model and update `local_inference.py`:

```python
MODEL_PATH = "models/qwen2.5-7b.Q4_K_M.gguf"  # Example: Qwen2.5-7B
```

### **Q: My Mac is overheating or running too slow**
✅ Reduce CPU load:
```python
NUM_THREADS = 4  # Lower CPU usage
```

---

## **📌 Summary**
🚀 **You now have a fully offline, private AI chatbot running on your Mac!**  
✅ **No API keys, No cloud, No privacy concerns**  
✅ **Works even without an internet connection**  
✅ **Supports Mistral, Qwen, DeepSeek, Llama, and other GGUF models**  

This setup allows you to explore AI **securely and privately**, without relying on OpenAI, Anthropic, or other cloud-based LLMs.

---

## **📂 Repository Structure**
```
📂 local_LLM_inference/
 ├── 📄 README.md  # This guide
 ├── 📄 local_inference.py  # Python script to run the chatbot
 └── 📂 models/  # Folder to store the downloaded LLM model
```

---
