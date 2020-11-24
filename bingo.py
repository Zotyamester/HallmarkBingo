import random

from flask import Flask, render_template, url_for

words = []
with open('./static/items.txt', 'r') as f:
    words = f.read().split('\n')

def rand_mat(n):
    mywords = words.copy()
    random.shuffle(mywords)
    return [[mywords[i * n + j] for j in range(n)] for i in range(n)]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def bingo():
    mat = rand_mat(5)
    return render_template('index.html', mat=mat)

app.run()
