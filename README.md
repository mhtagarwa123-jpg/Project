
# CollegeBot - Rule-Based Chatbot

## task 1
This project is a Rule-Based College FAQ Chatbot developed using Python. The chatbot answers common college-related questions such as admissions, fees, courses, hostel facilities, placements, greetings, and farewells.

## Features
- Greeting and Farewell Responses
- Admission Information
- Fee Structure Details
- Course Information
- Hostel Information
- Placement Details
- Unknown Query Handling
- Regex-Based Pattern Matching

## Technologies Used
- Python 3
- Regular Expressions (re)
- Random Module

## Working
1. User enters a query.
2. The input is preprocessed.
3. Regex and keyword matching are used to identify the intent.
4. The chatbot provides a suitable response.
5. If no match is found, a fallback response is displayed.

## How to Run
```bash
python chatbot.py# Project

---

# README - Task 2 (NLP Chatbot)

```markdown
# CollegeBot - NLP Enhanced Chatbot

## task 2
This project is an NLP-based College FAQ Chatbot developed using Python and Machine Learning techniques. It uses TF-IDF Vectorization and Cosine Similarity to identify user intent and provide relevant responses.

## Features
- NLP-Based Intent Detection
- TF-IDF Vectorization
- Cosine Similarity Matching
- College FAQ Responses
- Better Understanding of User Queries
- Handles Different Sentence Variations

## Technologies Used
- Python 3
- Scikit-Learn
- TF-IDF Vectorizer
- Cosine Similarity

## Working
1. User enters a query.
2. The query is converted into a TF-IDF vector.
3. Cosine similarity is calculated with existing patterns.
4. The most similar intent is identified.
5. A corresponding response is returned.

## How to Run
```bash
python nlp_chatbot.py
