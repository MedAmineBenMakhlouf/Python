from flask import Flask, render_template, redirect, request
from artist_model import Artist
app = Flask(__name__)


@app.route('/')
def dashboard():
    all_artists = Artist.get_all()
    return render_template('dashboard.html', artists= all_artists)

@app.route('/artists/new')
def new_artist():
    return render_template("new_artist.html")

@app.route('/artists/new', methods=['POST'])
def create_artist():
    data_dict = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'nationality':request.form['nationality'],
        'rate':request.form['rate'],
        'image':request.form['image']
    }
    if 'is_dead' in data_dict:
        data_dict['is_dead']=1
    else:
        data_dict['is_dead']=0
    
    Artist.create_artist(data_dict)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)