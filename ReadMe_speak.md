````markdown
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
````

### Speech Dependencies (for `ollama_speak.py`)

**Required**

* `piper` (offline TTS)
* `alsa-utils` (provides `aplay`)

**Optional but recommended**

* `sox` (pitch/timbre presets like “Tenor”)

Install audio tools:

```bash
sudo apt update
sudo apt install alsa-utils sox -y
```

---

## Ollama Setup

Ensure Ollama is running:

```bash
ollama serve
```

Test:

```bash
curl http://127.0.0.1:11434/api/tags
```

Download a model (example):

```bash
ollama pull llama3
```

---

## Piper Setup (Speech Version)

You need a Piper binary and at least one voice model.

### Piper binary

Example:

* `/home/eric/.local/bin/piper` (default in the script)
* or `piper` available in `$PATH`

Check:

```bash
command -v piper && piper --version
```

### Voice models

This fork expects Piper models like:

* `/opt/piper/voices/en_US-joe-medium.onnx`
* `/opt/piper/voices/en_US-amy-low.onnx`

Each model must also have its JSON beside it:

* `en_US-joe-medium.onnx.json`
* `en_US-amy-low.onnx.json`

---

## Install

```bash
git clone <your-fork-url>
cd <repo-folder>
```

---

## Run

### Standard GUI

```bash
python3 ollama_gui.py
```

### Speech GUI

```bash
python3 ollama_speak.py
```

---

## Using the Speech GUI (`ollama_speak.py`)

1. Enable **Speech**
2. Choose a Piper voice model (Joe default)
3. Ask your question
4. The GUI speaks the **final** assistant response automatically
5. Use **Stop Speaking** to interrupt audio output

### Timbre / Tenor Mode

If you enable a tenor/bright preset, SoX pitch shift is used.
Install SoX if missing:

```bash
sudo apt install sox -y
```

---

## Notes / Troubleshooting

### “I hear nothing”

* Verify Ollama returns text normally
* Verify `aplay` exists:

  ```bash
  command -v aplay
  ```
* Verify Piper works:

  ```bash
  command -v piper && piper --version
  ```
* Verify voice model + `.json` exist at the expected path

### Wrong voice tone (too deep / bass-heavy)

Use a tenor/bright preset (SoX pitch shift) or switch to a different Piper voice model.

---

## Credits

* **Original Project:** `ollama-gui` by **chyok**
* **This Fork:** Enhancements and speech GUI additions by **Dr. Eric O. Flores**

---

## License

This fork follows the upstream license unless you explicitly change it.
Check the upstream repository and include/retain the original license file.

---

## Disclaimer

This project is intended for **local use** with user-provided models and resources.
All trademarks and model names belong to their respective owners.

```

::contentReference[oaicite:0]{index=0}
```
