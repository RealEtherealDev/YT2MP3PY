from flask import Flask, render_template, request, flash, redirect, url_for, session
from pytube import YouTube

app = Flask(__name__)
app.secret_key = b'12312fsdgdfghdassdfl,hjkhjsdrtzdf'


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/", methods=["POST"])
def index_post():

    session["link"] = request.form.get("youtube_url")
    try:
        url = YouTube(session["link"])
        url.check_availability()
    except:
        return render_template("error.html")

    try:
        url = YouTube(session["link"])
        stream = url.streams.get_audio_only()
        stream.download(filename=url.streams[0].title + ".mp3")
        return render_template("success.html")

    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run()
