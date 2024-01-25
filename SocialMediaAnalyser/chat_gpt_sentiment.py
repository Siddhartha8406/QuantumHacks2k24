api_keys = "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"
text_analysis = "One of the Most Entertaining episodes"


from openai import OpenAI
client = OpenAI(api_key=api_keys)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"give me sentiment analysis score  without any other content only for the following text, {text_analysis}"},
  ]
)

print(completion.choices[0].message.content.strip())
