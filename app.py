from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def epl_standing():
    respon = requests.get('https://football-standings-api.vercel.app/leagues/eng.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('epl.html', standings=standings)

@app.route('/epl')
def epl_standings():
    respon = requests.get('https://football-standings-api.vercel.app/leagues/eng.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('epl.html', standings=standings)

@app.route('/laliga')
def laliga_standings():
    respon = requests.get('https://football-standings-api.vercel.app/leagues/esp.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('laliga.html', standings=standings)

@app.route('/bundesliga')
def bundesliga_standings():
    respon = requests.get('https://football-standings-api.vercel.app/leagues/ger.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('bundesliga.html', standings=standings)

@app.route('/seriea')
def seriea_standings():
    respon = requests.get('https://football-standings-api.vercel.app/leagues/ita.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('seriea.html', standings=standings)

@app.route('/ligue1')
def ligue1_standings():
    respon = requests.get('https://football-standings-api.vercel.app/leagues/fra.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('ligue1.html', standings=standings)

if __name__ == '__main__':
    app.run(debug=True)