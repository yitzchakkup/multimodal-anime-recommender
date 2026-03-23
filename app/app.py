# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import sys
import os

# Add the directory containing trainig_vals_for_website.py to the Python path
# This assumes trainig_vals_for_website.py is in the same directory as app.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from trainig_vals_for_website import recommend # Import your recommendation function

app = Flask(__name__)

MAX_RECOMMENDED = 50 # Define the maximum number of recommendations todo change

@app.route('/', methods=['GET', 'POST'])
def index():
    top_anime = pd.read_csv("top_animes.csv", keep_default_na=False)
    anime_titles = top_anime["working_title"].tolist()
    recommended_animes = []
    error_message = None

    if request.method == 'POST':
        user_ratings = []
        rated_count = 0
        for title in anime_titles:
            rating_str = request.form.get(f'rating_{title}')
            if rating_str:
                try:
                    rating = float(rating_str)
                    if 1 <= rating <= 10: # Assuming ratings are 1-10
                        user_ratings.append((title, rating))
                        rated_count += 1
                    else:
                        error_message = "Ratings must be between 1 and 10."
                        break
                except ValueError:
                    error_message = "Invalid rating. Please enter a number."
                    break

        if error_message:
            pass # Error message will be displayed
        elif not user_ratings:
            error_message = "Please rate at least one anime to get recommendations."
        else:
            try:
                amount_str = request.form.get('amount_to_recommend')
                if amount_str:
                    amount = int(amount_str)
                    if amount <= 0:
                        error_message = "Number of recommendations must be positive."
                    elif amount > MAX_RECOMMENDED:
                        error_message = f"You can request a maximum of {MAX_RECOMMENDED} recommendations."
                    else:
                        # Call your recommendation function
                        recommended_animes = recommend(user_ratings, amount)
                else:
                    error_message = "Please specify the number of recommendations."
            except ValueError:
                error_message = "Invalid number of recommendations. Please enter an integer."

    return render_template('index.html',
                           anime_titles=anime_titles,
                           recommended_animes=recommended_animes,
                           max_recommended=MAX_RECOMMENDED,
                           error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for automatic reloading and detailed error messages