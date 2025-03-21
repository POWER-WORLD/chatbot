import openai

# write here api key
openai.api_key = "api_key"

def is_safe(response):

    blocked_words = ["hate", "violence", "abuse", "offensive_word_1", "offensive_word_2"]  # Add more words as needed
    response_lower = response.lower()
    return not any(word in response_lower for word in blocked_words)

def get_ai_response(user_query):

    try:

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_query}],
            max_tokens=500  # Limit response length
        )

        ai_text = response["choices"][0]["message"]["content"]

        if is_safe(ai_text):
            return ai_text
        else:
            return "Response blocked due to inappropriate content."
    
    except openai.error.OpenAIError as e:
        return f"OpenAI API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

def main():
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        response = get_ai_response(query)
        print(f"AI: {response}")
if __name__ == "__main__":
    main()