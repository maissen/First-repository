import random

# Get user input for name and gender
name = input("What is your name? ")
gender = input("What is your gender? ")

# Generate random partner name, year of marriage, and nationality
partner_name = random.choice(["John", "Emily", "David", "Sarah", "Michael"])
year_of_marriage = random.randint(2025, 2045)
nationality = random.choice(["American", "British", "Canadian", "Australian", "French", "Japanese", "Russian"])

# Print prediction
print("Hi", name + "!", "Based on our calculations, your future partner's name will be", partner_name + ". You will get married in the year", year_of_marriage, "and your partner will be of", nationality, "nationality.")

