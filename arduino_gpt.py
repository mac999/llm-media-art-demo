# title: Arduino Code Generator
# description: Generate Arduino code from natural language input and upload to Arduino board.
# author: taewook kang
# email: laputa99999@gmail.com
# version: 0.1
# 
import os, json, subprocess, sys, time, shutil, re, subprocess, textwrap, argparse
import openai
from ollama import chat
from ollama import ChatResponse
from openai import OpenAI

def llm_agent(prompt):
	response = chat(
		model='gemma2',
		messages=[{"role": "user", "content": prompt}]
	)
	if response and isinstance(response, ChatResponse):
		return response.message.content
	else:
		raise Exception("Failed to get a valid response from the model")

client = OpenAI(api_key='<input your openai api key here>')
def openai_agent(prompt, system_prompt="You are Arduino coder.", model="gpt-4o"):
	response = client.chat.completions.create(
		model="gpt-4o",
		messages=[
			{
				"role": "system",
				"content": system_prompt
			},
			{
			"role": "user",
			"content": prompt
			}
		],
		temperature=0.1,
		max_tokens=1024,
		top_p=1
	)
	return response.choices[0].message.content

def preprocess_code(text: str) -> str:
	try:
		match = re.search(r'```cpp\n(.*?)```', text, re.DOTALL) # extract code from text between ```python\n and ```
		code = match.group(1).strip()
		code = code.replace('\t', '    ')
		code = textwrap.dedent(code)
	except IndentationError as e:
		print(f"IndentationError detected: {e}")
		code = ''
	except SyntaxError as e:
		print(f"SyntaxError detected: {e}")
		code = ''
	except Exception as e:
		print(f"Error: {e}")
		code = ''
	return code

def generate_code(prompt):
	code_prompt = f"generate Arduino code, no comment: {prompt}" # loop led13 on, off with 1 second repeatly. # loop rotate angle from 0 to 90 about each step 5, delay 50 using servo motor, repeadly.
	code = openai_agent(code_prompt) # llm_agent(code_prompt)
	code = preprocess_code(code)

	return code

def send_code(code, port='COM4'):
	try:
		filename = 'gen_code.ino'
		folder_name = os.path.splitext(filename)[0]
		os.makedirs(folder_name, exist_ok=True)
		filename = os.path.join(folder_name, filename)

		with open(filename, 'w') as file:
			file.write(code)
			
		subprocess.call(['arduino-cli', 'lib', 'install', 'servo'])  
		subprocess.call(['arduino-cli', 'compile', '--clean', '--fqbn', 'arduino:avr:uno', './gen_code'])
		subprocess.call(['arduino-cli', 'upload', './gen_code', '-p', port, '-b', 'arduino:avr:uno'])   
		return "Code uploaded successfully."
	except subprocess.CalledProcessError as e:
		return f"Error uploading code: {e}"

def main():
    parser = argparse.ArgumentParser(description='Generate and upload Arduino code from natural language input.')
    parser.add_argument('--prompt', type=str, default='loop led13 on, off with 1 second repeatly', help='The prompt to generate Arduino code.')
    parser.add_argument('--port', type=str, default='COM4', help='The port to upload the Arduino code.')
    args = parser.parse_args()

    code = generate_code(args.prompt)
    send_code(code, args.port)

if __name__ == "__main__":
	main()
