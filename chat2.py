from openai import AzureOpenAI

AZURE_ENDPOINT = "https://learning-openai.openai.azure.com/"
AZURE_API_KEY = "YOUR_KEY_HERE"          # put your real key
AZURE_API_VERSION = "2025-03-01-preview" # 🔴 updated
AZURE_MODEL = "gpt-4o-mini"              # use your deployment name

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

    response = client.responses.create(
        model=AZURE_MODEL,
        input=[
            {"role": "user", "content": msg}
        ]
    )

    # Extract text reply
    reply = ""
    for item in response.output:
        if item.type == "message":
            for c in item.content:
                if c.type == "text":
                    reply += c.text

    print("bot:", reply)
