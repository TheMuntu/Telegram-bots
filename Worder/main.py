from flask import Flask, request
import requests
import json

app = Flask(__name__)

def get_word():
    # code to fetch a new word, definition, and example sentences from Wordnik API
    api_key = "YOUR_API_KEY"
    word_url = f"http://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&api_key={api_key}"
    response = requests.get(word_url)
    word = json.loads(response.text)["word"]
    def_url = f"http://api.wordnik.com/v4/word.json/{word}/definitions?limit=1&api_key={api_key}"
    response = requests.get(def_url)
    definition = json.loads(response.text)[0]["text"]
    ex_url = f"http://api.wordnik.com/v4/word.json/{word}/examples?includeDuplicates=false&useCanonical=false&skip=0&limit=2&api_key={api_key}"
    response = requests.get(ex_url)
    examples = json.loads(response.text)["examples"]
    example_sentences = [example["text"] for example in examples]
    return word, definition, example_sentences

def send_message(chat_id, text):
    # function to send message to Telegram user
    url = f"https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

@app.route('/', methods=['POST'])
def handle_message():
    # function to handle incoming messages
    message = request.get_json()
    chat_id = message["message"]["chat"]["id"]
    word, definition, example_sentences = get_word()
    text = f"Word: {word}\nDefinition: {definition}\nExample Sentences:\n1. {example_sentences[0]}\n2. {example_sentences[1]}"
    send_message(chat_id, text)
    return 'ok', 200

if __name__ == '__main__':
    app.run(port=8443)
