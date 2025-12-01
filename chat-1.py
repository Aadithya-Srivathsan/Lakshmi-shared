from openai import AzureOpenAI
import os

# 👉 Replace these with your real values
AZURE_ENDPOINT = "https://learning-openai.openai.azure.com/"
AZURE_API_KEY = "YOUR_API_KEY_HERE"          # <-- put your key here (or use env var)
AZURE_API_VERSION = "2025-01-01-preview"
AZURE_MODEL = "gpt-4o-mini"                  # <-- use your deployment/model name

client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
)

print("welcome to chatbot! (type 'quit' to exit)")

while True:
    msg = input("you: ")
    if msg.strip().lower() == "quit":
        break

    # Call the new Responses API
    response = client.responses.create(
        model=AZURE_MODEL,
        input=[
            {
                "role": "user",
                "content": msg
            }
        ]
    )

    # Extract the text reply
    reply = ""
    for item in response.output:
        if item.type == "message":
            for c in item.content:
                if c.type == "text":
                    reply += c.text

    print("bot:", reply)
