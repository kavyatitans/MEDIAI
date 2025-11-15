# 🩺 AI Doctor Voicebot  
### A conversational medical assistant powered by Groq LLMs, Vision analysis, Speech Recognition, and Text-to-Speech.

This project is an interactive AI Doctor that:

🎙️ **Listens to a patient's voice**  
🧠 **Understands symptoms or queries using Groq LLM**  
🖼️ **Analyzes ANY uploaded image** (skin, wounds, X-rays, MRI, reports, photos, etc.)  
💬 **Generates a doctor-style response**  
🔊 **Speaks the response using gTTS or ElevenLabs**

It is designed for **learning, experimentation, and AI research**, not for real clinical use.

---

## 🚀 Features

### 🎤 **Speech-to-Text (STT)**
- Captures live audio from the microphone  
- Uses `speech_recognition` to convert speech to text  
- Saves the original audio as `.mp3`

### 🖼️ **Image Understanding (General Vision Model)**
The model can analyze **any type of medical or non-medical image**, including:

- Skin conditions  
- X-rays / CT scans / MRI  
- Wounds / injuries  
- Medical reports  
- Objects / environments  
- General images  

Groq Vision + LLM pipeline interprets the image and answers questions like:

- “What does this image show?”  
- “What condition might this represent?”  
- “What should the patient do next?”

### 🧠 **Doctor Brain (LLM reasoning)**
Generates:

- Diagnosis-style insights  
- Possible causes  
- Advice  
- Safety alerts  
- Referral suggestions  

### 🔊 **Doctor's Voice (TTS)**  
Supports two engines:

- **gTTS** (free)  
- **ElevenLabs** (natural, realistic voice)

The generated audio is embedded directly inside the Gradio UI.

### 🖥️ **Interactive Gradio Interface**
Includes:

- Microphone recording  
- Image upload box  
- Text + audio output fields  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Voice Input | `speech_recognition`, `PyAudio` |
| LLM Reasoning | **Groq LLMs** |
| General Image Interpretation | **Groq Vision** |
| Voice Output | **gTTS**, **ElevenLabs API** |
| UI | **Gradio** |
| Secrets Management | `.env` file |

---

## 📁 Folder Structure

