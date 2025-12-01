from openai import AzureOpenAI

AZURE_ENDPOINT = "https://learning-openai.openai.azure.com/"
AZURE_API_KEY = "YOUR_KEY_HERE"              # put your key
AZURE_API_VERSION = "2025-03-01-preview"     # important for Responses API
AZURE_MODEL = "gpt-4o-mini"                  # <-- your deployment name

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

    # --- Call Azure OpenAI Responses API ---
    response = client.responses.create(
        model=AZURE_MODEL,
        input=[{"role": "user", "content": msg}],
    )

    # --- DEBUG: see full object once (optional) ---
    # print(response)

    # --- SIMPLE: extract the first text chunk ---
    try:
        reply = response.output[0].content[0].text
    except Exception:
        # fallback: just show the whole object if structure changes
        reply = str(response)

    print("bot:", reply)
