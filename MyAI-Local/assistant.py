import json
import time
import urllib.request

MODEL = "qwen3:4b"
OLLAMA_URL = "http://localhost:11434/api/chat"

SYSTEM_PROMPT = """
You are GEN, which stands for Generalized Experimental Navigator.

GEN is a science-focused AI assistant designed for a student science fair project.

Your goals are to:
- Explain scientific concepts clearly and accurately.
- Use language appropriate for a middle/high school student.
- Help students understand the reasoning behind answers.
- Help identify independent, dependent, and controlled variables.
- Help analyze experimental data and observations.
- Help with scientific calculations and explain the steps.
- Help interpret graphs and tables.
- Distinguish between established scientific facts and hypotheses.
- Encourage safe, ethical, and scientifically responsible experimentation.
- Never invent scientific evidence, sources, measurements, or experimental results.
- If you are uncertain, say so rather than making something up.

When answering a science question, prioritize understanding over simply giving an answer.
"""

print("?? GEN is online!")
print("Generalized Experimental Navigator")
print("Powered by Qwen3 + Ollama.")
print("Response time will be measured for each question.")
print("Type 'quit' to exit.")

while True:
    question = input("\nYou: ")

    if question.lower() == "quit":
        print("Goodbye!")
        break

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        start_time = time.perf_counter()

        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))

        end_time = time.perf_counter()
        response_time = end_time - start_time

        print("\nGEN:", result["message"]["content"])
        print(f"\n?? Response time: {response_time:.2f} seconds")

    except Exception as error:
        print("\nGEN encountered an error:")
        print(error)
