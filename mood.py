mood_dict = {
    "happy": "yellow",
    "sad": "blue",
    "angry": "red",
    "stressed": "blue",
    "relaxed": "green",
    "energetic": "red",
    "confident": "black",
    "compassionate": "pink"
}
outfit_dict = {
    "yellow": "a bright yellow t-shirt or sundress",
    "blue": "a calming blue sweater or denim jacket",
    "red": "a bold red shirt or dress",
    "green": "a soothing green dress or casual hoodie",
    "black": "a sleek black suit or classy dress",
    "pink": "a soft pink shirt or cardigan"
}
def recommend_outfit(mood):
    mood = mood.lower()
    if mood in mood_dict:
        recommended_color = mood_dict[mood]
        outfit_suggestion = outfit_dict.get(recommended_color, "something in that color")
        return f"For a {mood} mood, you should wear {recommended_color}. Suggested outfit: {outfit_suggestion}."
    else:
        return "Sorry, I don't recognize that mood. Try a common emotion like happy, sad, or energetic!"
user_mood = input("How are you feeling today? ").strip()
print(recommend_outfit(user_mood))