import media
import fresh_tomatoes
import urllib.request
import urllib.parse
from urllib.parse import urljoin
import json

# API Variables
omdb_api_url = 'http://www.omdbapi.com/'
omdb_api_key = 'c497f6ec'

tmdb_data_api_url = 'https://api.themoviedb.org/3/find/'
tmdb_video_api_url = 'https://api.themoviedb.org/3/movie/'
tmdb_api_key = 'e70dfa434baa19e37a3fae92106bcb47'

# List of favorite movies
favorite_movies_imdb_id = ['tt1375666', 'tt0133093', 'tt0482571', 'tt0167404',
                           'tt0111161', 'tt0468569', 'tt4154756']


""" This method calls OMDB API to get the movie data (as found in IMDB) """


def get_movie_data_omdb(imdb_id):
    omdb_params = urllib.parse.urlencode(
        {'i': imdb_id, 'apikey': omdb_api_key})
    # connection = urllib.request.urlopen(
    #    "http://www.omdbapi.com/?i=tt0111161&apikey=c497f6ec")
    connection = urllib.request.urlopen(omdb_api_url + "?%s" % omdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    result = parse_json(result)
    return result


""" This method calls TMDB API to get the movie data mainly TMDB ID for getting
trailer (as found in themoviedb.org) """


def get_movie_data_tmdb(imdb_id):
    tmdb_params = urllib.parse.urlencode(
        {'external_source': 'imdb_id', 'language': 'en-US',
         'api_key': tmdb_api_key})
    # connection = urllib.request.urlopen(
    #    "https://api.themoviedb.org/3/find/tt0111161?external_source=imdb_id&language=en-US&api_key=e70dfa434baa19e37a3fae92106bcb47")
    base_url = urljoin(tmdb_data_api_url, imdb_id)
    connection = urllib.request.urlopen(base_url + "?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    result = parse_json(result)
    return result


""" This method calls TMDB Video API to get the
movie trailer (as found in themoviedb.org) """


def get_movie_video_tmdb(tmdb_id):
    tmdb_params = urllib.parse.urlencode(
        {'language': 'en-US', 'api_key': tmdb_api_key})
    # connection = urllib.request.urlopen(
    #    "https://api.themoviedb.org/3/movie/278/videos?api_key=e70dfa434baa19e37a3fae92106bcb47&language=en-US")
    base_url = urljoin(tmdb_video_api_url, tmdb_id)
    # print(base_url)
    connection = urllib.request.urlopen(base_url + "/videos?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    result = parse_json(result)
    return result


def parse_json(data):
    # load the json to a string
    return json.loads(data)


def generate_movie_list():
    movies = []

    for fav_imdb_id in favorite_movies_imdb_id:

        # Calling OMDB API to get details of the movie (as found in IMDB)
        omdb_data = get_movie_data_omdb(fav_imdb_id)

        print(omdb_data)

        """ Calling TMDB API to get tmdb_id and details of the movie
        (as found in TMDB) """
        tmdb_data = get_movie_data_tmdb(fav_imdb_id)

        print(tmdb_data)

        # Calling TMDB Video API to get the trailer of the movie
        video = get_movie_video_tmdb(str(tmdb_data['movie_results'][0]['id']))

        """ Looping over videos of the movie
        and Assigning the appropriate trailer """
        video_key = ''
        if video['results']:
            for v in video['results']:
                if v['site'] == 'YouTube' and v['type'] == 'Trailer':
                    video_key = v['key']
                    break

        # Constructing movie object
        movie = media.Movie(omdb_data['Title'],
                            omdb_data['Plot'],
                            # 'https://image.tmdb.org/t/p/w500' +
                            # tmdb_data['movie_results'][0]['poster_path'],
                            omdb_data['Poster'],
                            'https://www.youtube.com/watch?v=' + video_key)

        movie.set_additional_information(omdb_data['Year'],
                                         omdb_data['Rated'],
                                         omdb_data['Runtime'],
                                         omdb_data['Genre'],
                                         omdb_data['imdbRating'])

        # Pushing the movie to the movies list
        movies.append(movie)

    return movies


movies = generate_movie_list()
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
