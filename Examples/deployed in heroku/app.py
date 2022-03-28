from flask import Flask, render_template, send_from_directory, request, send_file
import os
from threading import Thread
from os import path

from werkzeug.datastructures import MultiDict
from werkzeug.utils import redirect, secure_filename

from Facebook import madangowri

app = Flask(__name__)
file_path_main = path.abspath(__file__)
dir_path_main = path.dirname(file_path_main)


@app.route('/')
def hello():
    return 'Home Page'


@app.route("/facebook/permlove")
def dontbecorner():
    thread_b = Thread(target=madangowri.Run, args=())
    thread_b.start()
    return render_template("timepage.html", title="perm Love")



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
