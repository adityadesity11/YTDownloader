from flask import Flask,render_template,url_for,request,flash,redirect
from pytube import YouTube
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'pydownloader'


@app.route('/', methods=['GET','POST'])

def home():
    if request.method == 'POST':
        url = str(request.form['url'])
        res = str(request.form['resolution'])
        type = str(request.form['type'])
        try:
            yt = YouTube(url)
            title = yt.title
            thumbnail = yt.thumbnail_url
            video = yt.streams.get_by_resolution(res)
            if res == '4K':
                video = yt.streams.get_highest_resolution()
            os.chdir('C:/Users/Admin/Downloads')
            video.download(filename=f'{title}.{type}')
            print("Downloaded!")
            flash("Downloaded sucessfully!!",category='success')
            return render_template('home.html',title=title,thumbnail_url = thumbnail)
        except:
            flash("Invalid url!", category='error')
            return redirect('/')

    return render_template('home.html')



@app.route('/ytmp4',methods =['GET','POST'])
def mp4():
    if request.method=='POST':
        url = request.form.get('url')
        type = request.form.get('type')
        print(type)

        try:

            yt = YouTube(url)
            file=None
            if(type=='audio'):
                file = yt.streams.get_audio_only()
            else:
                file = yt.streams.get_by_resolution('720p')
            os.chdir('C:/Users/Admin/Downloads')
            title = yt.title
            thumbnail = yt.thumbnail_url
            file.download()
            flash('MP4 File Downloaded Successfully!',category='success')
            return render_template('mp4.html',title=title,thumbnail_url=thumbnail)
        except:
            flash('Invalid url!',category='error')
            return redirect(url_for('mp4'))
    return render_template('mp4.html')


@app.route('/ytmp3',methods=['GET','POST'])
def mp3():
    if request.method=='POST':
        url = request.form.get('url')
        type = request.form.get('type')
        print(type)

        try:

            yt = YouTube(url)
            file=None
            if(type=='audio'):
                file = yt.streams.get_audio_only()
            else:
                file = yt.streams.get_by_resolution('720p')

            os.chdir('C:/Users/Admin/Downloads')
            title = yt.title
            thumbnail = yt.thumbnail_url
            file.download(filename=f'{title}.mp3')
            flash('MP3 File Downloaded Successfully!',category='success')
            return render_template('mp3.html',title=title, thumbnail_url=thumbnail)
        except:
            flash('Invalid url!',category='error')
            return redirect(url_for('mp3'))
    return render_template('mp3.html')




@app.route('/audio',methods=['GET','POST'])
def audio():
    if request.method == 'POST':
        url = request.form['url']
        type = request.form['type']
        try:
            yt = YouTube(url)
            title = yt.title
            thumbnail = yt.thumbnail_url
            print(title)
            audio = yt.streams.get_audio_only()
            os.chdir('C:/Users/Admin/Downloads')

            audio.download(filename=f'{title}.{type}')
            flash('Audio File Downloaded Successfully!',category='success')
            return render_template('audio.html',title=title,thumbnail_url=thumbnail)

        except:
            flash('Invalid url!',category='error')
            return redirect(url_for('audio'))
        

    return render_template('audio.html')

@app.route('/playlist')
def playlist():
    return "<h1>Under Development</h2><br><h3>Feature will be live soon</h3>"


if __name__ == "__main__":
    app.run(debug=True,port=5000)