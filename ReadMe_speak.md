# Ollama GUI + Ollama Speak (Tkinter)

A lightweight, local-first GUI for **Ollama** built with **Python + Tkinter**, plus an enhanced variant that adds **speech output** so you can *hear* model responses instead of only reading them.

This project is a fork of the original **ollama-gui** by **chyok**, with improvements and an additional speech-enabled GUI.

---

## Projects in This Fork

### 1) `ollama_gui.py` (Improved GUI)
Enhancements focused on stability and usability:
- Safer cancel/stop behavior using `threading.Event` (no widget-state hacks)
- Network timeouts to prevent hanging
- UI thread-safety improvements for background threads
- Improved menu structure (About dialog + revision metadata)
- Keyboard behavior improvements (binds `<Return>` only to avoid breaking shortcuts)

### 2) `ollama_speak.py` (New GUI With Speech Output)
A new GUI variant that includes:
- **Speech toggle** (Enable/Disable)
- Speaks the **final assistant response** after completion (not partial streaming)
- **Stop Speaking** button
- Piper-based offline speech using `piper` + ALSA `aplay`
- Optional timbre lift (e.g., “Tenor”) via **SoX pitch shift** for brighter voice output

> The speech version is a major usability upgrade for long answers and accessibility—users can listen instead of reading.

---

## Requirements

### System
- Linux recommended (Pop!_OS / Ubuntu tested)
- Ollama installed and running locally
- Python 3.10+ recommended

### Python
- Tkinter (usually included with system Python)
- No extra Python packages required for the GUI itself

Install Tkinter if missing:
```bash
sudo apt update
sudo apt install python3-tk -y
