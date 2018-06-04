# Project: Movie Trailer Website
This project is part of the Full Stack Developer Nanodegree Program at Udacity. It shows a list of some of my favorite movies along with its details. The website also allows you to watch trailers of the listed movies.

More details can be found here:

**[Project Overview](./project_overview.md)**

**[Project Details](./project_details.md)**

**[Project Display Example](./project_display_example.md)**

**[Project Submission](./project_submission.md)**

# How to run?

## Pre-requisites
- Python 3.6.5
- Web Browser (Recommended: Chrome)
- Internet Connection (its not offline compatible)
- A bit of Curosity ;)

## Run
- `clone` or `download` the code
- Open `IDLE`
- Browse to the source code folder and open `entertainment_center.py`
- Run the script (and wait a while)
- Done - You should see data loading in terminal and web browser displaying the website

# Technology Stack
This website uses the following technologies:
- **Python 3.6.5**
- **Bootstrap 3** (with Bootswatch theme [flatly](https://bootswatch.com/flatly/))
- **The Open Movie Database [OMDb API](http://www.omdbapi.com/)**
- **The Movie DB [TMDb API](https://www.themoviedb.org/documentation/api)** 

## Why multiple APIs?
OMDb API provides almost all necessary movie details found in IMDb website, however, it lacks video trailer. TMDb on the other hand, has video trailer but the movie details are not as elaborative as of IMDb.

The merge of two APIs provides rich movie content and enhances User Experience.

# Issues
- May display error in terminal if the APIs response timed-out (just re-run and it should be fine)
- Feel free to report if you find any

# License
This project is a public domain work, dedicated using CC0 1.0. Feel free to do whatever you want with it. (If you are a udacity student, learn but not cheat :P)
