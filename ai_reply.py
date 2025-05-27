import openai

openai.api_key = "your_openai_api_key_here"  # Replace with your actual key

def generate_reply(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for responding to Instagram messages."},
                {"role": "user", "content": user_message}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[AI Error]: {str(e)}"
