# from flask import Blueprint, render_template, request

# view = Blueprint('view', __name__)

# @view.route('/', methods = ['GET, POST'])
# def home():
#     data = request.form
#     print(data)
#     return render_template('uploadFile.html')

from flask import Blueprint, Flask, render_template, request
from mutagen.mp3 import MP3

view = Blueprint('view', __name__)

@view.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['mp3_file']
        if file:
            mp3 = MP3(file)
            duration = mp3.info.length
            return render_template('index.html', duration=duration)
    return render_template('index.html')
