
# Simple Mental Wellness Chatbot - Text Based

import random

# Mood-based responses
responses = {
    "sad": [
        "I'm here for you. Want to talk about it?",
        "It's okay to feel sad. You are not alone.",
        "Sending you a big hug. You're stronger than you know."
    ],
    "happy": [
        "That's great to hear! 😊",
        "Yay! Keep spreading those positive vibes.",
        "I'm so happy you're feeling good!"
    ],
    "angry": [
        "Take a deep breath... want to share what's bothering you?",
        "It's okay to feel angry sometimes. Let it out safely.",
        "Let's find a way to calm things down together."
    ],
    "confused": [
        "It’s okay to not have all the answers. Let’s figure it out slowly.",
        "Do you want to talk about what’s confusing you?",
        "I’m here… no rush, just take your time."
    ],
    "default": [
        "I'm listening... tell me more.",
        "Hmm, want to talk more about how you're feeling?",
        "I'm right here. Say whatever’s on your mind."
    ]
}

# Keyword matching
def detect_mood(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["sad", "lonely", "upset", "cry"]):
        return "sad"
    elif any(word in user_input for word in ["happy", "excited", "great", "good"]):
        return "happy"
    elif any(word in user_input for word in ["angry", "mad", "frustrated", "annoyed"]):
        return "angry"
    elif any(word in user_input for word in ["confused", "lost", "don't know", "not sure"]):
        return "confused"
    else:
        return "default"

# Chatbot main loop
def chatbot():
    print("Hi, I'm your Bunny Bot 🐰. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bunny Bot: Take care! Talk to you soon 🤍")
            break
        mood = detect_mood(user_input)
        response = random.choice(responses[mood])
        print("Bunny Bot:", response)

if __name__ == "__main__":
    chatbot()
