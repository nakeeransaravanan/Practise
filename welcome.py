import random

cities = ['Halifax', 'Montreal', 'Vancouver', 'Toronto']

def welcome_message():
  city = random.choice(cities)
  return f'Welcome to {city}'
