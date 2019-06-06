import csv
import json

entity_name = "movie_name"
input_file = "titles_generate.csv"
intent = "inform_movie_name"

actor_strings = {
    "I would like to see a movie with entity_name",
    "Is there a movie starring entity_name ?", "Give me a movie with entity_name, please",
    "I like movies with entity_name",
    "My favorite actor is entity_name", "Propose me a movie with the actor entity_name, please"}

genre_strings = {
    "I like entity_name movies",
    "Show me a popular entity_name movie", "I want to see an entity_name movie, please",
    "I would like to see a entity_name film",
    "entity_name movie, please", "Propose me a entity_name film, please", "What is a good entity_name movie ?",
    "Show me a good entity_name movie", "Do you have a good entity_name film ?",
    "I want to watch a entity_name movie", "I love entity_name movies", "a good entity_name film please",
    "I want to do an entity_name movie night", "Propose me a nice entity_name movie please"}

film_strings = {
    "Give me informations about the movie entity_name",
    "I want details about entity_name", "I want to have informations about the entity_name movie",
    "Give me details about entity_name",
    "Infos about entity_name", "I want to know about entity_name movie please", "What is entity_name about ?",
    "Give me some infos about entity_name", "How much time is the movie entity_name ?",
    "What genre is the movie entity_name ?", "give me the plot of the movie entity_name",
    "How old is the movie entity_name ?",
    "Give me the release date of the movie entity_name", "do you have the synopsis of the movie entity_name"}

output = open("output.json", "w")
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    entities = []
    for row in csv_reader:
        entity = row[0]
        entities.append(entity)

        for s in film_strings:
            new_string = s.replace("entity_name", entity)

            start = new_string.find(entity)
            end = start + len(entity)

            data = {'text': new_string,
                    'intent': intent,
                    "entities": [{"start": start,
                                  "end": end,
                                  "value": entity,
                                  "entity": entity_name
                                  }]
                    }
            json.dump(data, output, indent=4)
            output.write(",\n")
