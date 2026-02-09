---
````markdown
# Ollama-GUI (Enhanced Fork)

![GitHub License](https://img.shields.io/github/license/chyok/ollama-gui)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

A lightweight, local-first **Ollama GUI** built with **Python + Tkinter**, based on the
original work by **chyok**, with stability improvements and an additional
speech-enabled interface.

This fork preserves the original philosophy:
> **Simple, dependency-minimal, local GUI for Ollama**

while extending it in two directions:
- **ollama-gui-enhanced** — stability & usability improvements
- **ollama-speak** — a new GUI that can *read responses aloud*

---

## 📦 Projects in This Fork

### 1️⃣ ollama-gui-enhanced (Text-only GUI)
An improved version of the original `ollama_gui.py`, focused on correctness,
responsiveness, and usability — **no speech, no extra dependencies**.

**Enhancements include:**
- Proper stop/cancel handling using thread-safe cancellation
- Network timeouts to prevent GUI lockups
- Tkinter UI thread-safety fixes
- Keyboard shortcut preservation (`<Return>` only, no key hijacking)
- Revised About menu with version and contributor metadata

This version is ideal if you want a **clean, minimal, text-based Ollama GUI**.

---

### 2️⃣ ollama-speak (Speech-Enabled GUI)
A new GUI variant that adds **offline speech output**, allowing users to **hear**
model responses instead of reading them.

**Key features:**
- Enable / Disable speech toggle
- Speaks the **final assistant response** (not partial streams)
- Stop Speaking button
- Uses **Piper TTS** (offline, local, no cloud)
- Optional timbre adjustment (e.g. tenor/bright voice via SoX)

This version is especially useful for:
- Long responses
- Accessibility
- Hands-free interaction
- Audio-first workflows

---

## 🚀 Original Features (Preserved)

From the upstream project by **chyok**:

- 📁 One-file Tkinter application
- 📦 No external GUI dependencies
- 🔍 Automatic Ollama model discovery
- 🌐 Custom Ollama host support
- 💬 Multiple conversations
- 📋 Menu bar and right-click menu
- 🛑 Stop generation at any time
- 🗂️ Model download & delete
- 💾 Save / Load conversation history
- 📝 Editable conversation bubbles

---

## ⚙️ Requirements

### General
- Python **3.10+**
- Ollama running locally

```bash
ollama serve
````

### Tkinter (if missing)

```bash
sudo apt install python3-tk
```

### Speech GUI Only (`ollama-speak`)

* `piper` (offline TTS)
* `alsa-utils` (`aplay`)
* Optional: `sox` for pitch/timbre control

```bash
sudo apt install alsa-utils sox
```

---

## ▶️ Run

### Text-only enhanced GUI

```bash
python3 ollama_gui.py
```

### Speech-enabled GUI

```bash
python3 ollama_speak.py
```

---

## 🧠 Notes

* `ollama-speak` **does not replace** the original GUI — it is an **additional option**
* Speech is local, offline, and user-controlled
* No telemetry, no cloud APIs, no servers added

---

## 👥 Credits

* **Original Project:** `ollama-gui` by **chyok**
* **Enhancements & Speech GUI:** **Dr. Eric O. Flores** (with AI-assisted development)

---

## 📜 License

MIT License
Original work © 2024 chyok
Enhancements © 2026 Dr. Eric O. Flores

See [LICENSE](LICENSE) for details.

```

---

## ✅ Summary (Clear Answer)

- ✔ Yes, you are allowed to update the README  
- ✔ Yes, you may document **ollama-gui-enhanced** and **ollama-speak**  
- ✔ Your changes are MIT-compliant  
- ✔ Attribution is preserved and clear  
- ✔ This README follows GitHub best practices  
```
