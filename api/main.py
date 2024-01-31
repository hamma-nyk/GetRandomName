from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__) 

@app.route('/')
def home():
    return "Hello World"
