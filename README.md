# **🚀 Running a Local LLM: DeepSeek-R1-Distill-Qwen-7B on Mac (Fully Offline)**

## **🔹 Overview**  
This guide walks you through **deploying and running a Large Language Model (LLM) locally on your Mac**.  
This allows you to run an **AI chatbot fully offline**—no internet required.

For this example, we will use **DeepSeek-R1-Distill-Qwen-7B**, but you can replace it with **any GGUF-compatible model** like **Qwen, Llama, DeepSeek**, etc.

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
Before running the chatbot, install the necessary dependencies.

### **✅ 1. Install Homebrew (Mac’s Package Manager)**  
If you don’t have **Homebrew**, install it first:

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

If missing or outdated, install it via Homebrew:

```bash
brew install python
```

Verify that Python is installed:
```bash
python3 --version
```

---

### **✅ 3. Install Required Python Libraries**  
Now, install `llama-cpp-python`, which enables local AI execution:

```bash
pip install llama-cpp-python
```

> **Why?**  
> - Runs **GGUF models** efficiently on **Mac (MPS), CPU, and GPU**.  
> - Works for various LLMs like **Qwen, Llama, and DeepSeek**.  

---

## **🔹 3. Download the AI Model**  
We use **DeepSeek-R1-Distill-Qwen-7B**, optimized for **local inference**, but you can **choose any other GGUF model**.

### **1️⃣ Install Hugging Face CLI**  
We will use **Hugging Face** to download the model:

```bash
pip install huggingface-hub
```

### **2️⃣ Download the DeepSeek Model**  
Run this command to download **DeepSeek-R1-Distill-Qwen-7B** (~4.68 GB):

```bash
huggingface-cli download tensorblock/DeepSeek-R1-Distill-Qwen-7B-GGUF \
--include "DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf" --local-dir models \
--local-dir-use-symlinks False
```

> **Want a different model?**  
> Replace `DeepSeek-R1-Distill-Qwen-7B` with another GGUF model, such as:
> - **Qwen2.5-7B**: `huggingface-cli download TheBloke/Qwen2.5-7B-GGUF ...`
> - **Llama 2-7B**: `huggingface-cli download TheBloke/Llama-2-7B-GGUF ...`

### **3️⃣ Move the Model to the Correct Folder**  
```bash
mkdir -p models
mv models/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf models/
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
> `Chatbot ready! Type 'exit' to quit.`  

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

## **🔹 5. Using a Different Model Instead of DeepSeek**  
If you want to **replace DeepSeek with another model**, follow these steps:

### **1️⃣ Download Another Model**  
Example for **Qwen-7B**:

```bash
huggingface-cli download TheBloke/Qwen2.5-7B-Instruct-GGUF \
Qwen2.5-7B-Instruct.Q4_K_M.gguf --local-dir models \
--local-dir-use-symlinks False
```

### **2️⃣ Update `local_inference.py`**  
Open `local_inference.py` and change the `model_path` to:

```python
def load_model():
    """Loads the Qwen model with optimized settings."""
    return Llama(
        model_path="models/Qwen2.5-7B-Instruct.Q4_K_M.gguf",  # Path to Qwen model
        n_gpu_layers=35,  # Offloads computation to GPU for better performance
        verbose=False  # Suppresses unnecessary debug logs
    )
```

### **3️⃣ Run the Chatbot**  
Once the model is downloaded and the script is updated, run:

```bash
python3 local_inference.py
```

This will launch **Qwen2.5-7B** instead of **DeepSeek-R1-Distill-Qwen-7B**. 🚀

---

## **📌 Summary**  
🚀 **You now have a fully offline, private AI chatbot running on your Mac!**  
✅ **No API keys, No cloud, No privacy concerns**  
✅ **Works even without an internet connection**  
✅ **Supports Qwen, DeepSeek, Llama, and other GGUF models**  

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
