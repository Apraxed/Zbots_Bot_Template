"""THIS ONLY WORKS IN REPLIT"""
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)
#REPLIT ONLY!!!!!!!
def keep_alive():
    t = Thread(target=run)
    t.start()

"""if you are not using replit, don't remove the `#` next to `from keep_alive import keep_alive" and don't remove the `#` from `keep_alive()` in main.py"""
