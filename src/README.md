# Motivational Meme Generator

## Overview

Motivational Meme Generator is a multimedia application which dynamically generates memes, including an image with an overlaid quote.

The main modules of the meme generator are:
- **MemeEngine** which manipulates and draws text onto images.
- **QuoteEngine** which loads and parses quotes from files.

## Usage
### Command Line Inferface

To use the app with the command line interface, run the following command in a terminal:

```
pip install -r requirements.txt
python3 meme.py --body 'string body of the quote' --author 'string author of the quote' --path 'path to image location'

```
The script will return a path to the generated meme. If none of the optional arguments (body, author and path) are provided, a random selection is used.

### Flask App 
To launch the flask app, run the following commands in a terminal:
```
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```

## Dependencies
- [ABC](https://docs.python.org/3/library/abc.html)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [os](https://docs.python.org/3/library/os.html)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Pandas](https://pandas.pydata.org/)
- [Python-docx](https://python-docx.readthedocs.io/en/latest/)
- [Subprocess](https://docs.python.org/3/library/subprocess.html)
- [typing](https://docs.python.org/3/library/typing.html)
