from dotenv import load_dotenv
from openai import OpenAI
from unittest.mock import MagicMock

load_dotenv()

client = OpenAI()

client.chat.completions.create = MagicMock(return_value={
    "choices": [
        {"message": {"content": "Hello! This is a mock response."}}
    ]
})

# Now call your code
response = client.chat.completions.create(
    model="gpt-5.2",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response["choices"][0]["message"]["content"])


# response = client.chat.completions.create(
#     model="gpt-5.2",
#     messages=[
#         {"role": "user", "content": "Hello!"}
#     ]
# )


# print(response.choices[0].message.content)

# openai_client = OpenAI(

# prompt = "Give me a very short recipe for a cake please."

# response = openai_client.chat.completions.create(
#     model = "gpt5.2"
# )
