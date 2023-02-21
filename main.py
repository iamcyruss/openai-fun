import os
import openai
#openai.organization = "org-T7DjdhGMLtljxFtsGHLN48JS"
openai.api_key = os.getenv("OPENAI_API_KEY")
#print(openai.api_key)
returned = openai.Model.list()
#print(f"{returned}")

# for count, i in enumerate(returned.data):
#     print(f"{count}. {i.id}")

text_response = openai.Completion.create(
    model = "ada",
    prompt = "what is ai?",
    temperature = 0,
    max_tokens = 300
)

print(text_response)
