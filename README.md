## Media Art Examples with Python
This repository contains AI tool installation link, example code and resources for Media Art Study with LLM, focusing on creative coding, modeling, sound generation and physical computing using Python, LLM. The tools covered include **pygame**, **Sonic Pi (using `python-sonic`)**, **p5**, **Blender**, **Arduino** and **Ollama**.
In reference, this is for the purpose of studying in A.DAT media art group, South Korea (2025.1). A.DAT is open media art group from 2014 and focuses on how to represent social message using emerging tech like Gen AI, Physical Computing, LLM, Sensor based on creative artist. </br>
<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*3kNBB0E4xDwKiC1SQcYbhA.png" width=600><br>Prompt: Create sphere and cube around the sphere</br></img></br>
<img src="https://github.com/mac999/llm-media-art-demo/blob/main/openg_anime.gif" width=600><br>Prompt: Create cubes grid with color (temperature) and height (energy) after reading input.csv including bulidings dataset with temperature, energy using pandas</br></img>
## Overview

This project is designed for students and enthusiasts exploring **Media Art** through creative coding and interactive audio-visual art. Below are the main libraries and tools used in this repository:

- **pygame**: Pygame is a Python library designed for creating video games. It provides tools and functionalities for handling graphics, sound, and user input, making it easy to develop 2D/3D games or interactive applications. It’s beginner-friendly and works on multiple platforms. [pygame](http://programarcadegames.com/index.php?chapter=example_code).
- **Blender**: LLM-based Graphic Modeling using Blender. In example, [Blender LLM Addin blog](https://medium.com/@laputa99999/using-open-source-models-with-blender-for-ai-assisted-3d-modeling-comparative-study-with-openai-9848209f93b8)
- **Arduino**: LLM-based Arduino Coding. In example, [Arduino programming using LLM](https://neural-maze.github.io/blog/posts/202405-crewai-ollama-arduino/)
- **Sonic Pi (`python-sonic`)**: A Python interface to Sonic Pi for live-coding music.
- **PyAudio**: For real-time audio processing.
- **p5**: A Python port of Processing, used for interactive and generative visual art. In example, [Data driven 3D model visualization](https://medium.com/@laputa99999/creating-3d-data-visualizations-with-p5-python-7933d5b3a59f) can be developed easily.
- **Ollama**: For using AI tools in interactive art projects. You need to install NVIDIA cuda for run it.
- **Huggingface**: For uisng LLM, Stable Diffusion-based model, You need to sign up Huggingface. In example, [Single Image-to-3D model](https://huggingface.co/spaces/stabilityai/stable-point-aware-3d)
- **ROS(Robot Operation System)**: LLM-based ROS coding. In example, [ROS-LLM](https://github.com/Auromix/ROS-LLM/tree/ros2-humble)

The repository includes examples to experiment with generative art, live music coding, and real-time audio manipulation.</br>
In addition, you can find Text-to-3D model tool the below link. 
- [Text-to-3D model code](https://github.com/mac999/blender-llm-addin): Using Open-Source Models with Blender for AI-Assisted 3D Modeling: Comparative Study with OpenAI GPT

---

## Preparation and Installation

Before running the examples, ensure you have Python 3.8 or higher installed. Some tool or library use NVIDIA GPU, so if you want to use it, prepare notebook computer with NVIDIA GPU(recommend 8GB. minimum 4GB)
Follow the instructions below to set up your environment:

### 1. Huggingface, OpenAI (Optinnal) Account 
Make Accounts for OpenAI, Huggingface
- Sign up [Huggingface](https://huggingface.co/) to develop Open source LLM-base application
- Sign up [OpenAI API](https://platform.openai.com/) to develop ChatGPT-based application (*Note: don't check auto-subscription option)

### 2. Python
Ensure that Python (version 3.7 or later) is installed on your system. About macbook, please refer to [how to install python on mac](https://www.youtube.com/watch?v=u4xUUBTER4I).

- **Download Python**: [python.org](https://www.python.org/)
- During installation:
  - Check the box for **"Add Python to PATH"**.
  - Install Python along with **pip**.

To confirm installation in terminal(DOS command in windows. Shell terminal in linux):
```bash
python --version
```

### 3. Anaconda (Optional)
Ensure that Anaconda (version 24.0 or later) is installed on your system.

- **Download Anaconda**: [Anaconda](https://docs.anaconda.com/anaconda/install/)

### 4. Install Ollama 
For examples that utilize Ollama, follow the installation instructions from the [Ollama website](https://www.ollama.com/).

### 5. Blender (for AI-Assisted Modeling)
If the script or application involves Blender for 3D modeling, ensure Blender is installed.

- **Download Blender**: [blender.org](https://www.blender.org/download/)
- After installation:
  - Enable the **Python Console** within Blender to run scripts directly.
  - Ensure Blender uses the same Python environment where required libraries are installed.

### 6. Install Sonic Pi
- Download and install **Sonic Pi** from the [official website](https://sonic-pi.net/).
- Ensure that Sonic Pi is running when using `python-sonic` for sound generation.

### 7. NVIDIA Drivers (for Ollama. optional)
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

### 8. CUDA Toolkit (for NVIDIA. optional)
CUDA is required for running GPU-accelerated operations.

- **Download CUDA Toolkit**: [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
- During installation:
  - Match the CUDA version with your NVIDIA driver and GPU model. Refer to the compatibility chart on the download page.
  - Install the CUDA Toolkit with default options.
  - Add the CUDA binary paths to your environment variables.

### 9. PyTorch library (for NVIDIA. optional)

- If AI-related models or tools will be used (such as LLM model fine-tuning with Ollama), install stable [PyTorch](https://pytorch.org/get-started/locally/)(11.8 version) and additional packages:
   ```bash
   pip install openai
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

### 10. Install Python Packages
Run the following command to install the required libraries:
```bash
pip install pygame pytest python-sonic pyaudio pandas numpy
pip install ollama openai transformers huggingface_hub
```

p5 can be executed under Python version 3.11 (Refer to https://github.com/p5py/p5/issues/469)  
```bash
pip install p5
```
---

### 11. Install sublime and vscode (Optional)
Install [Sublime](https://www.sublimetext.com/) for editing source code</br>
Install [vscode](https://code.visualstudio.com/download) for debuging code. Please refer to how to [install vscode](https://www.youtube.com/watch?v=vesxpfOAOCw).</br>

---

## Usage

Before clone this source code, you need to install [Github CLI (Korea version)](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98). ([Github CLI (English)](https://github.com/git-guides/install-git))

1. Clone this repository:
   ```bash
   git clone https://github.com/mac999/llm-media-art-demo.git
   cd llm-media-art-demo
   ```

2. Run the desired example:
   ```bash
   python game1.py     # Example using pygame
   python psonic_music.py  # Example using python-sonic
   ```
---

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

## Examples

### 1. pygame 
Generate interactive art using `pygame`:

```python
import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
WIDTH = 20
HEIGHT = 20
MARGIN = 5
 
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
grid[1][5] = 1
 
pygame.init()
 
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed Grid")
done = False
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    screen.fill(BLACK)
 
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
```
In detail, refer to [pygame example](http://programarcadegames.com/index.php?chapter=example_code).

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


### 4. p5 Visual Example
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

### 5. arduino_gpt example
To test Arduino agent powered by GPT or Ollama, install the below
```bash
pip install subprocess pyserial requests
```
and run below. 
```bash
python arduino_gpt.py
```
The parameters are 
- prompt: prompt for arduino code generation
- port: arduino port for uploading the generated code.
<img src="https://github.com/mac999/llm-media-art-demo/blob/main/arduino.gif" width=600>

## Reference
- [Python과 node.js기반 데이터 분석 및 가시화](https://www.slideshare.net/slideshow/python-nodejs/252348474?from_search=2)
- [NVIDIA cuda programming, open source and AI](https://www.slideshare.net/slideshow/nvidia-cuda-programming-open-source-and-ai/270372806?from_search=6)
- [Docker 에서 Ollama, ComfyUI][https://www.youtube.com/watch?v=IxxOMLkcYNY]
- [Chat with ChatGPT through Arduino IoT Cloud](https://projecthub.arduino.cc/dbeamonte_arduino/chat-with-chatgpt-through-arduino-iot-cloud-6b4ef0)
- [chatGPT-Arduino-library](https://github.com/programming-electronics-academy/chatGPT-Arduino-library/tree/main)
- [ChatGPT_Client_For_Arduino](https://github.com/0015/ChatGPT_Client_For_Arduino)
- [I tried ChatGPT for Arduino - It’s Surprising](https://blog.wokwi.com/learn-arduino-using-ai-chatgpt/)
- [Using ChatGPT to Write Code for Arduino and ESP32](https://dronebotworkshop.com/chatgpt/)

## License

This repository is licensed under the MIT License. You are free to use, modify, and distribute the code for personal or commercial projects.

## Author
laputa99999@gmail.com
