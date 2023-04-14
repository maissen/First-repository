import random

# Get user input
name = input("What's your name? ")
gender = input("What's your gender? ")

# Generate a random number between 1 and 10 for the year of marriage
year = random.randint(2024, 2040)

# Generate a list of potential partners based on gender
if gender.lower() == 'male':
    partners = ['Emma', 'Olivia', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn']
else:
    partners = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander']

# Guess the future partner's name randomly
partner = random.choice(partners)

# Print the results
print(f"Hi {name}! I think your future partner's name is {partner} and you'll get married in {year}.")

