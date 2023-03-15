import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)
app.debug = True

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for qf in quote_files:
        if Ingestor.parse(qf) is not None:
            quote = Ingestor.parse(qf)
            quotes.append(quote)
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path, topdown=True):
        imgs = [os.path.join(root, file) for file in files
                if os.path.isfile(os.path.join(root, file))]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quotemodels = random.choice(quotes)
    try:
        quote = random.choice(quotemodels)
    except IndexError as e:
        print(f"IndexError: {e}, no quote was found")
        quote = QuoteModel("WOOFWOOFWOOF", "Shakespeare")
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    img_url = request.form.get('image_url')
    img_data = requests.get(img_url)
    tmp = f'./tmp/{random.randint(0,100000000)}.jpg'
    with open(tmp, 'wb') as handler:
        handler.write(img_data.content)
    body = request.form.get('body')
    author = request.form.get('author')
    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()