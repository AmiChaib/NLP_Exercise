import jokeapi
import pandas as pd
from jokeapi import Jokes # Import the Jokes class
import asyncio

categories_set = ['Any', 'Misc', 'Programming', 'Dark', 'Pun', 'Spooky', 'Christmas']
selected_category = 'Programming'

async def print_joke(selected_category):
    category = [selected_category]
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(category=category)
    if joke["type"] == "single": # Print the joke
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])

asyncio.run(print_joke(selected_category))