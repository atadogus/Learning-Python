# dictionary comprehension
import random

names = ["a", "b", "c"]

scores = {name: random.randint(0, 100) for name in names}
print(scores)

passing_grades = {name: score for (name, score) in scores.items() if score > 60}
# to create a dictionary using comprehension on another existing dictionary, .item() is included at the end of the dict
# in foreach loop and the traversing value this time is not a single value but a key: value tuple represented as (key, value)
print(passing_grades)

question = "What is the airspeed velocity of an unladen swallow?"

question_words = question.split(" ")
print(question_words)
character_count = {word: len(word) for word in question_words}
print(character_count)

weather_C = {"monday": 12, "tuesday": 14, "wednesday": 18, "thursday": 21, "friday": 20}

weather_F = {day: round(32 + temp * 1.8, 2) for (day, temp) in weather_C.items()}
print(weather_F)