from openai import OpenAI
from google import genai


client = OpenAI(
    api_key="OpenAI_API_KEY"
)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def chat_with_gemini(prompt):
    client = genai.Client(api_key="GEMINI_API_KEY")


    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    parts = response.candidates[0].content.parts
    text_parts = [part.text for part in parts if hasattr(part, "text")]
    return " ".join(text_parts)

    


if __name__ == "__main__":

    print("Chat with LLM's press 1 or 2\n\n1. Chat-GPT\n2. Gemini")
    user_input_llm = int(input("Choose LLM 1/2: "))

    while True:
        user_input = input("You : ")

        if user_input_llm == 1:
            response = chat_with_gpt(user_input)
            print("Bot: ", response)
        else: 
            response = chat_with_gemini(user_input)
            print("Bot: ", response)
        



        if user_input.lower() in ["quit", "exit", "close"]:
            break

        
