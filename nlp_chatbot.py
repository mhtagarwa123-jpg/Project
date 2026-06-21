import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

patterns = [
    "hello", "hi", "hey",
    "admission process", "how to apply",
    "fees structure", "college fees",
    "hostel available", "hostel facility",
    "placement record", "job opportunities"
]

tags = [
    "greeting", "greeting", "greeting",
    "admission", "admission",
    "fees", "fees",
    "hostel", "hostel",
    "placements", "placements"
]

responses = {
    "greeting": "Hello! Welcome to CollegeBot.",
    "admission": "Admissions are open through the college website.",
    "fees": "Engineering fees are Rs 80,000 per year.",
    "hostel": "Hostel facility is available for boys and girls.",
    "placements": "Top recruiters include Infosys, TCS and Amazon.",
    "unknown": "Sorry, I don't understand."
}

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()

    if similarity[0][index] < 0.2:
        return responses["unknown"]

    return responses[tags[index]]

print("CollegeBot NLP Edition")
while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot_response(user))