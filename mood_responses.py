#Assignment 1

def mood_response(mood):
    mood = mood.lower() 

    if mood == "happy" or mood == "great":
        return "Awesome! Keep doing what you're doing."
    if mood == "sad" or mood == "depressed":
        return "I'm sorry to hear that. Maybe try reaching out to a loved one for support."
    if mood == "excited":
        return "Heck yeah!"
    if mood == "angry" or mood == "mad":
        return "I'm sorry to hear that. Maybe try journaling your feelings or have a snack."
    else:
        return "Hmm...I'm not sure I understand. I hope you're feeling okay!"