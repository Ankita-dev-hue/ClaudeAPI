import anthropic

try:

    client = anthropic.Anthropic(api_key="")
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=100,
        messages=[{"role": "user", "content": "Explain black holes simply."}],
    )

    print(response.content[0].text)
except Exception as e:
    print(e)
