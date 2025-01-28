# Media Art Examples with Python
This repository contains example scripts and resources for Media Art Study with LLM, focusing on creative coding and sound generation using Python. The tools covered include **p5**, **Sonic Pi (using `python-sonic`)**, and **Ollama**.

---

## Overview

This project is designed for students and enthusiasts exploring **Media Art** through creative coding and interactive audio-visual art. Below are the main libraries and tools used in this repository:

- **p5**: A Python port of Processing, used for interactive and generative visual art. In example, [the data driven visualization](https://medium.com/@laputa99999/creating-3d-data-visualizations-with-p5-python-7933d5b3a59f) can be developed easily.
- **Sonic Pi (`python-sonic`)**: A Python interface to Sonic Pi for live-coding music.
- **PyAudio**: For real-time audio processing.
- **Ollama**: For using AI tools in interactive art projects.

The repository includes examples to experiment with generative art, live music coding, and real-time audio manipulation.</br>
In addition, you can find Text-to-3D model tool the below link. 
- [Text-to-3D model](https://medium.com/@laputa99999/using-open-source-models-with-blender-for-ai-assisted-3d-modeling-comparative-study-with-openai-9848209f93b8): Using Open-Source Models with Blender for AI-Assisted 3D Modeling: Comparative Study with OpenAI GPT

---

## Installation

Before running the examples, ensure you have Python 3.8 or higher installed. Follow the instructions below to set up your environment:

### 1. Install Python Packages
Run the following command to install the required libraries:

```bash
pip install pytest python-sonic p5 pyaudio
```

### 2. Install Sonic Pi
- Download and install **Sonic Pi** from the [official website](https://sonic-pi.net/).
- Ensure that Sonic Pi is running when using `python-sonic` for sound generation.

### 3. Install Ollama (Optional)
For examples that utilize Ollama, follow the installation instructions from the [Ollama website](https://www.ollama.com/).

---

## Examples

### 1. Sonic Pi Example
Create simple melodies using `python-sonic`:

```python
from psonic import *

set_server_parameter_from_log("127.0.0.1")  # Connect to Sonic Pi server
run("play 60")  # Play middle C (MIDI 60)

play(C5)
sleep(0.5)
play(E5)
sleep(0.5)
play(G5)
```

### 2. p5 Visual Example
Generate interactive art using `p5`:

```python
from p5 import *

def setup():
    size(800, 800)

def draw():
    background(200)
    ellipse((mouse_x, mouse_y), 50, 50)

run()
```

### 3. PyAudio Real-Time Example
Process audio streams in real-time [(see the relevant documents for details)](https://people.csail.mit.edu/hubert/pyaudio/).

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/media-art-examples.git
   cd media-art-examples
   ```

2. Run the desired example:
   ```bash
   python psonic_music.py  # Example using python-sonic
   python p5_con3d.py     # Example using p5
   ```

---

## License

This repository is licensed under the MIT License. You are free to use, modify, and distribute the code for personal or commercial projects.

## Author
laputa99999@gmail.com
