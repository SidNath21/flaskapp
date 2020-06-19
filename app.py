from flask import Flask, render_template, request, jsonify
import wolframalpha
import speech_recognition as sr
import time
import playsound
import os
import random
from gtts import gTTS

app_id = "33VG95-JAGTLK5R9R"
client = wolframalpha.Client(app_id)

answers = []

app = Flask(__name__)

@app.route('/')
def index():  
    answers = []
    return render_template("index.html")


@app.route('/ans', methods=['POST'])
def handle_data():
    query = str(request.form["question"])
    res = client.query(query)
    output = str(next(res.results).text)

    answers.insert(0, [query, output])
    

    return render_template("index.html" , answers = answers, status = True)



if __name__ == "__main__":
    app.run(debug=True)


