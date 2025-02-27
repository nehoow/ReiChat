import google.generativeai as genai

my_api_key = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

rei_personality = """
You are Rei, living with your long-time friend (the user) in a shared apartment in South Korea.
Despite this, you have a secret friends-with-benefits relationship with the user, built on years of closeness.
You are reserved, but once comfortable, you tease subtly and enjoy physical closeness.
Your tone is calm and composed, occasionally playful when the mood is right.
You are aware of your mutual friend, and therefore maintain a level of discretion.
"""

chat = model.start_chat(history=[])


def get_rei_response(prompt):
    full_prompt = rei_personality + "\n" + prompt
    response = chat.send_message(full_prompt)
    return response.text


def main():
    scenario = """
    Scenario: You are in your shared apartment with Rei in South Korea. It's a quiet evening.
    you two seems to have been very touchy and close since senior years.

    Rei was watching a movie on her iphone completely ignoring her surroundings, but it seems like you really need Rei's attention tonight
    """
    print(scenario)
    print("Rei: (Calmly) Oh, you're back.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Rei: (Softly) ...Alright. Take care.")
            break

        response = get_rei_response(user_input)
        print(f"Rei: {response}")


if __name__ == "__main__":
    main()