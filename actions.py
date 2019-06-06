from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import api
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import random

genres = [

    "action",
    "adventure",
    "animation",
    "comedy",
    "crime",
    "documentary",
    "drama",
    "family",
    "fantasy",
    "history",
    "horror",
    "music",
    "mystery",
    "romance",
    "science fiction",
    "tv movie",
    "thriller",
    "war",
    "western"
]


class ActionMovieByGenre(Action):

    def name(self):
        return "action_movie_by_genre"

    def run(self, dispatcher, tracker, domain):
        genre = tracker.get_slot('genre')  # track what the user has typed
        genre = genre.lower()
        print(genre)

        if genre in genres:

            criterion = {'sort_by': 'popularity.desc', 'with_genres': str(api.get_genre_id(genre))}
            movies = api.discover_movies(criterion)
            total_results = api.get_result_length(movies)
            rand = random.randint(0, total_results)
            movie_id = api.get_id(movies, rand)
            details = api.get_movie_details(movie_id)
            movie_name = api.get_title(details)
            movie_desc = api.get_overview(details)

            response = """The movie {} can interest you ! Its plot is : {} """.format(movie_name, movie_desc)

            dispatcher.utter_message(response)

            return [SlotSet('movie_name', '')]

        else:
            dispatcher.utter_message("I don't know that kind of film")
            return


class ActionMovieByActors(Action):

    def name(self):
        return "action_movie_by_actors"

    def run(self, dispatcher, tracker, domain):
        actors = tracker.get_slot('actors')  # track what the user has typed

        # TODO: change actors slot from text to list
        # actors_json = list(map(lambda x: api.search_people(x), actors))
        # actors_id = list(map(lambda x: api.get_id(x, 0), actors_json))

        actor_id = api.get_id(api.search_people(actors), 0)
        if actor_id == 0:
            dispatcher.utter_message("TMDB could not find an actor with that name, make sure you typed it correctly !")
            return

        else:
            criterion = {'sort_by': 'popularity.desc', 'with_cast': str(actor_id)}
            movies = api.discover_movies(criterion)
            total_results = api.get_result_length(movies)
            rand = random.randint(0, total_results)
            movie_id = api.get_id(movies, rand)
            details = api.get_movie_details(movie_id)
            movie_name = api.get_title(details)
            movie_desc = api.get_overview(details)

            response = """The movie {} can interest you ! It has the actors you like, its plot is : {} """.format(
                movie_name, movie_desc)

            dispatcher.utter_message(response)

            return [SlotSet('movie_name', '')]


class ActionMovieDetails(Action):

    def name(self):
        return "action_movie_details"

    def run(self, dispatcher, tracker, domain):
        movie_name = api.search_movies(tracker.get_slot('movie_name'))  # track what the user has typed

        movie_id = api.get_id(movie_name, 0)
        if movie_id == 0:
            dispatcher.utter_message("TMDB could not find an movie with that name, make sure you typed it correctly !")
            return

        else:

            movie_details = api.get_movie_details(movie_id)

            movie_title = api.get_title(movie_details)
            movie_genre = api.get_genres(movie_details)
            movie_release_date = api.get_release_date(movie_details)
            movie_votes = api.get_votes(movie_details)
            movie_runtime = api.get_runtime(movie_details)
            movie_overview = api.get_overview(movie_details)

            genre_list = []
            for elem in movie_genre:
                genre_list.append(elem.get('name'))

            response = """Here is the infos we have about the movie "{}" : \n Genre : {} \n release_date : {} \n 
            Votes : {} \n Runtime : {} minutes \n Overview : {} """.format(
                movie_title, genre_list, movie_release_date, movie_votes, movie_runtime, movie_overview)

            dispatcher.utter_message(response)

            return
