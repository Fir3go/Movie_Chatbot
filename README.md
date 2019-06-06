# INSTALL

Make sure you have these installed on your computer :
- pip 3
- last python 3
- NodeJS
- NPM
- Ngrok (if you want to run the bot on slack on localhost)

## Requirements

Install the requirements from rasa git.

```bash
git clone https://github.com/RasaHQ/rasa_nlu.git
sudo pip3 install -r rasa_nlu/requirements.txt
sudo pip3 install -e .
sudo pip3 uninstall scikit-learn
sudo pip3 install scikit-learn==0.19.1
```

NOTE: You can use this if you want to have all the requirements and dependencies but it won't be needed for this project.
```bash
sudo pip3 install -r rasa_nlu/alt_requirements/requirements_full.txt
```

## More installation

Install the english module

```bash
sudo python3 -m spacy download en
```

Install Rasa NLU trainer

```bash
npm i -g rasa-nlu-trainer
```

Install Rasa Core

```bash
sudo pip3 install rasa_core==0.13.2
```

## ADD data

If you want to add data to the chatbot go to the data repository and launch Rasa NLU trainer to add data in Rasa GUI.

```bash
rasa-nlu-trainer
```

Or you can simply add data directly in the data/data.json file.

# Get access to the movie Database

To get access to the database you have to create an account and request an API key (https://www.themoviedb.org/?language=en-US). Once you have it, simply put in the api.py file at line 6 and you will be able to use it.

NOTE : This is totally free.

# RUN

## Train NLU

First you have to train your nlu model.

```bash
python3 nlu_model.py
```

## Train Rasa Core and execute bot (user oriented)

1) Start custom action server :

```bash
python3 -m rasa_core_sdk.endpoint --actions actions
```

2) In new terminal, run the bot :

```bash
python3 dialogue_management_model.py
```

## Train in interactive learning and execute in interactive mode (dev oriented)

1) Start custom action server :

```bash
python3 -m rasa_core_sdk.endpoint --actions actions
```

2) In new terminal, start interactive learning :

```bash
python3 train_interactive.py
 ```

# RUN ON SLACK

Before running it you have to create your own application on Slack and get the oauth key. This key has to be replace in the run_app.py file at line 12.

To run on slack :

```bash
python3 run_app.py
```

On slack API account change the url from "Event Subscription" to :
https://"your_ngrok_url"/webhooks/slack/webhook

where "your_ngrok_url" is the one from your tunnel.

To have the ngrok tunnel up just run (after installing ngrok) :

```bash
 ./ngrok http -region eu 5004
```

(Change your region according)
