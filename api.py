import http.client
import json
import urllib
import urllib.parse

api_key = "0739XXXXXXXX" # Replace the api_key with the one received on the https://www.themoviedb.org/?language=en-US


################################################
# Get  various information about a JSON result #
################################################


def get_title(json_res):
    return json_res['title']


def get_result_length(json_res):
    total_results = json_res['total_results']
    if total_results > 10:
        return 10
    else:
        return total_results


def get_biography(json_res):
    return json_res['biography']


def get_id(json_res, number):
    if json_res['total_results'] == 0:
        return 0
    else:
        return json_res['results'][number]['id']


def get_genres(json_res):
    return json_res['genres']


def get_release_date(json_res):
    return json_res['release_date']


def get_votes(json_res):
    return json_res['vote_average']


def get_runtime(json_res):
    return json_res['runtime']


def get_revenue(json_res):
    return json_res['revenue']


def get_budget(json_res):
    return json_res['budget']


def get_overview(json_res):
    return json_res['overview']


def is_adult(json_res):
    return json_res['adult']


def get_name(json_res):
    return json_res['name']


# returns a JSON containing detailed information about the movie corresponding to the parameter 'film_id'
def get_movie_details(film_id):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    f = {'api_key': api_key, 'language': 'en-US'}
    request = "/3/movie/" + str(film_id) + '?' + urllib.parse.urlencode(f)
    try:
        conn.request("GET", request, payload)
        res = conn.getresponse()
        data = res.read()
        json_res = json.loads(data)
        return json_res
    except Exception as e:
        print(type(e))
        r1 = conn.getresponse()
        print(r1.status, r1.reason)


# returns the DB id corresponding to the genre in argument
def get_genre_id(genre):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    f = {'api_key': api_key, 'language': 'en-US'}
    request = "/3/genre/movie/list" + '?' + urllib.parse.urlencode(f)
    try:
        conn.request("GET", request, payload)
        res = conn.getresponse()
        data = res.read()
        json_res = json.loads(data)
        genres = get_genres(json_res)
        for i in genres:
            if i['name'].lower() == genre.lower():
                print(i['id'])
                return i['id']
    except Exception as e:
        print(type(e))
        r1 = conn.getresponse()
        print(r1.status, r1.reason)


# returns a JSON containing detailed information about the person corresponding to the parameter 'person_id'
def get_person_details(person_id):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    f = {'api_key': api_key, 'language': 'en-US'}
    request = "/3/person/" + str(person_id) + '?' + urllib.parse.urlencode(f)
    try:
        conn.request("GET", request, payload)
        res = conn.getresponse()
        data = res.read()
        json_res = json.loads(data)
        return json_res
    except Exception as e:
        print(type(e))
        r1 = conn.getresponse()
        print(r1.status, r1.reason)


# returns a JSON containing basic information about all movies containing the keyword in their title
def search_movies(title):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    f = {'api_key': api_key, 'language': 'en-US', 'query': title}
    request = "/3/search/movie?" + urllib.parse.urlencode(f)
    try:
        conn.request("GET", request, payload)
        res = conn.getresponse()
        data = res.read()
        json_res = json.loads(data)
        return json_res
    except Exception as e:
        print(type(e))
        r1 = conn.getresponse()
        print(r1.status, r1.reason)


# returns a JSON containing basic information about all people having the keyword in their name
def search_people(name):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    print(name)
    payload = "{}"
    f = {'api_key': api_key, 'language': 'en-US', 'query': name}
    try:
        request = "/3/search/person?" + urllib.parse.urlencode(f)
        conn.request("GET", request, payload)
        res = conn.getresponse()
        data = res.read()
        json_res = json.loads(data)
        return json_res
    except Exception as e:
        print(type(e))
        r1 = conn.getresponse()
        print(r1.status, r1.reason)


# returns a JSON containing a dictionary of films that satisfy the criteria
def discover_movies(criteria):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    print(criteria)
    payload = "{}"
    f = {'api_key': api_key, 'language': 'en-US'}
    f.update(criteria)
    request = "/3/discover/movie?" + urllib.parse.urlencode(f)
    try:
        print(request)
        conn.request("GET", request, payload)
        res = conn.getresponse()
        data = res.read()
        json_res = json.loads(data)
        return json_res
    except Exception as e:
        print(type(e))
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
