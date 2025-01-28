## Media Art Examples with Python
---
This repository contains example scripts and resources for Media Art Study with LLM, focusing on creative coding and sound generation using Python. The tools covered include **p5**, **Sonic Pi (using `python-sonic`)**, and **Ollama**.
In reference, this is for the purpose of studying in A.DAT media art group, South Korea (2025.1). 

## Overview

This project is designed for students and enthusiasts exploring **Media Art** through creative coding and interactive audio-visual art. Below are the main libraries and tools used in this repository:

- **p5**: A Python port of Processing, used for interactive and generative visual art. In example, [Data driven 3D model visualization](https://medium.com/@laputa99999/creating-3d-data-visualizations-with-p5-python-7933d5b3a59f) can be developed easily.
- **Sonic Pi (`python-sonic`)**: A Python interface to Sonic Pi for live-coding music.
- **PyAudio**: For real-time audio processing.
- **Ollama**: For using AI tools in interactive art projects. You should install NVIDIA cuda for run it. 

The repository includes examples to experiment with generative art, live music coding, and real-time audio manipulation.</br>
In addition, you can find Text-to-3D model tool the below link. 
- [Text-to-3D model](https://medium.com/@laputa99999/using-open-source-models-with-blender-for-ai-assisted-3d-modeling-comparative-study-with-openai-9848209f93b8): Using Open-Source Models with Blender for AI-Assisted 3D Modeling: Comparative Study with OpenAI GPT

---

## Preparation and Installation

Before running the examples, ensure you have Python 3.8 or higher installed. Follow the instructions below to set up your environment:

### 1. Python
Ensure that Python (version 3.7 or later) is installed on your system.

- **Download Python**: [python.org](https://www.python.org/)
- During installation:
  - Check the box for **"Add Python to PATH"**.
  - Install Python along with **pip**.

To confirm installation:
```bash
python --version
```

### 2. Install Ollama 
For examples that utilize Ollama, follow the installation instructions from the [Ollama website](https://www.ollama.com/).

### 3. Blender (for AI-Assisted Modeling)
If the script or application involves Blender for 3D modeling, ensure Blender is installed.

- **Download Blender**: [blender.org](https://www.blender.org/download/)
- After installation:
  - Enable the **Python Console** within Blender to run scripts directly.
  - Ensure Blender uses the same Python environment where required libraries are installed.

### 4. Install Sonic Pi
- Download and install **Sonic Pi** from the [official website](https://sonic-pi.net/).
- Ensure that Sonic Pi is running when using `python-sonic` for sound generation.

### 5. NVIDIA Drivers (for Ollama. optional)
For GPU-accelerated tasks, you need to install the correct NVIDIA drivers for your GPU.

- **Download NVIDIA Drivers**: [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx)
- **Steps**:
  1. Identify your GPU model using the NVIDIA Control Panel or the `nvidia-smi` command in the terminal.
  2. Download the latest driver for your GPU model.
  3. Install the driver and reboot your system.

To confirm installation:
```bash
nvidia-smi
```

### 6. CUDA Toolkit (for NVIDIA. optional)
CUDA is required for running GPU-accelerated operations.

- **Download CUDA Toolkit**: [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
- During installation:
  - Match the CUDA version with your NVIDIA driver and GPU model. Refer to the compatibility chart on the download page.
  - Install the CUDA Toolkit with default options.
  - Add the CUDA binary paths to your environment variables.

   ```

### 7. PyTorch library (for NVIDIA. optional)

- If AI-related models or tools will be used (such as Blender integration for AI-assisted modeling), install additional packages:
   ```bash
   pip install openai
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

### 8. Install Python Packages
Run the following command to install the required libraries:

```bash
pip install ollama openai pytest python-sonic p5 pyaudio pandas numpy 
```
---

## Examples

### 1. p5 Visual Example
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

### 2. Sonic Pi Example
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
   python p5_con3d.py     # Example using p5
   python psonic_music.py  # Example using python-sonic
   ```
---

## **System Environment Checks**

After completing the installations, verify that the environment is set up correctly:

1. **Check Python Version**:
   ```bash
   python --version
   ```

2. **Verify NVIDIA Drivers**:
   ```bash
   nvidia-smi
   ```

3. **Confirm CUDA Version**:
   ```bash
   nvcc --version
   ```

4. **Test Python Libraries**:
   Create a test script and import the installed libraries:
   ```python
   import p5
   import pandas as pd
   import numpy as np
   print("Libraries are installed successfully!")
   ```

---

## License

This repository is licensed under the MIT License. You are free to use, modify, and distribute the code for personal or commercial projects.

## Author
laputa99999@gmail.com
