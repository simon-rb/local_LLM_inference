# **🚀 Running a Local LLM: Mistral 7B on Mac**
### **Workshop Guide – Secure, Private AI Deployment**

## **🔹 Overview**
This guide will help you set up and run a **local AI chatbot using Mistral-7B-Instruct on your Mac**.  
This model runs **completely offline**, ensuring **full privacy and security** without relying on the cloud.  

By the end of this workshop, you will:  
✅ **Install all necessary software and tools** (even if you’ve never done it before).  
✅ **Download and run an AI model locally**.  
✅ **Chat with the AI completely offline**.  

Follow along step-by-step, and you’ll have your own **AI assistant running locally!** 🚀  

---

## **📂 1. Clone the Repository**
First, download all the required files by cloning the **GitHub repository**:

```bash
git clone <YOUR_GITHUB_REPO_LINK>
cd <YOUR_REPO_FOLDER>
```

> **What's inside?**  
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

Verify that it was installed correctly:
```bash
brew --version
```

---

### **✅ 2. Install Python 3.9+**
Check if you already have Python 3.9 or later:

```bash
python3 --version
```

If the version is **lower than 3.9** or missing, install the latest Python:

```bash
brew install python
```

Verify that Python was installed:
```bash
python3 --version
```

---

### **✅ 3. Install Pip (Python Package Manager)**
Ensure **pip** is installed (you will use this to install required Python libraries):

```bash
python3 -m ensurepip --default-pip
```

Upgrade `pip` to the latest version:

```bash
pip install --upgrade pip
```

---

### **✅ 4. Install Required Python Libraries**
Now, install the **Llama-cpp** library, which allows local AI execution:

```bash
pip install llama-cpp-python
```

> **Why?**  
> - This enables fast, **offline** execution of AI models on **Mac (MPS), CPU, and GPU**.  
> - It removes the need for cloud APIs, making it **fully private**.  

---

## **🔹 3. Download the AI Model**
The **Mistral-7B-Instruct-Q4_K_M GGUF** model is optimized for **local inference**.

### **1️⃣ Install Hugging Face CLI**
We will use **Hugging Face** to download the model:

```bash
pip install huggingface-hub
```

### **2️⃣ Download the Model**
Run this command to download the model (~4GB):

```bash
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
mistral-7b-instruct-v0.2.Q4_K_M.gguf --local-dir models \
--local-dir-use-symlinks False
```

### **3️⃣ Move the Model to the Correct Folder**
```bash
mkdir -p ~/local-llm/models
mv models/mistral-7b-instruct-v0.2.Q4_K_M.gguf ~/local-llm/models/
```

> **Why this model?**  
> - **Mistral-7B-Instruct** → One of the best AI models for reasoning and conversation.  
> - **Q4_K_M quantization** → Runs **fast** on Mac while maintaining good quality.  
> - **Works 100% offline** → No internet needed after setup.  

---

## **🔹 4. Running the Local Chatbot**
Now that everything is installed, you can run the chatbot.

### **1️⃣ Navigate to the Script**
```bash
cd <YOUR_REPO_FOLDER>
```

### **2️⃣ Run the Chatbot**
```bash
python3 local_inference.py
```

> **If everything is working, you should see:**  
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
1. **Loads a local AI model (Mistral-7B-Instruct).**
2. **Optimizes performance** using **CPU & Apple Metal (MPS GPU) acceleration**.
3. **Maintains conversation memory** to improve multi-turn interactions.
4. **Runs an interactive chatbot loop** where users can input queries.
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

### **Q: I get a "command not found" error for `huggingface-cli`**
✅ Run:
```bash
pip install huggingface-hub
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
✅ **Supports long conversations & complex queries**  

This setup allows you to explore AI **securely and privately**, without relying on OpenAI, Anthropic, or other cloud-based LLMs.

---

## **📂 Repository Structure**
```
📂 <YOUR_REPO_FOLDER>/
 ├── 📄 README.md  # This guide
 ├── 📄 local_inference.py  # Python script to run the chatbot
 └── 📂 models/  # Folder to store the downloaded LLM model
```

---

## **📌 Additional Resources**
📂 **Mistral Model Repo:** [Mistral-7B-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)  
📖 **Llama.cpp Documentation:** [GitHub](https://github.com/ggerganov/llama.cpp)  

---
