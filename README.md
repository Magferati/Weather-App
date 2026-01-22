Project Overview

This is a Django-based Weather Application that fetches and displays real-time weather data for any city using third-party APIs.
It demonstrates integration of APIs, handling user input, and presenting dynamic content in a clean, responsive interface.

Features

Search for weather by city name.

Displays current temperature, humidity, weather description, and other relevant data.

Integration with OpenWeatherMap API (or any weather API).

Responsive design for desktop and mobile.

Clean and user-friendly UI.

Technologies Used

Backend: Django, Python

Frontend: HTML, CSS, Bootstrap

API: OpenWeatherMap API

Others: Git, GitHub, python-decouple/django-environ for environment variables

Installation

Clone the repository:

git clone https://github.com/Magferati/Weather-App.git


Navigate to the project folder:

cd weather-app


Create a virtual environment:

python -m venv env


Activate the virtual environment:

Windows: env\Scripts\activate

Mac/Linux: source env/bin/activate

Install dependencies:

pip install -r requirements.txt


Add your API key in a .env file (see instructions below).

Apply migrations:

python manage.py migrate


Run the server:

python manage.py runserver


Open in browser: http://127.0.0.1:8000/

Environment Variables (.env)

This project uses a .env file to store sensitive information like API keys.

Create a .env file in the project root if not already present.

Add your API key in the .env file:

WEATHER_API_KEY=your_api_key_here


Make sure .env is listed in .gitignore to avoid pushing it to GitHub.

The project uses python-decouple or django-environ to automatically load these variables.

Usage

Enter a city name in the search bar.

View current weather details including temperature, humidity, and weather description.

Refresh for updated weather data.

License

Open-source and free to use.
