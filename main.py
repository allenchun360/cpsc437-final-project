"""main file to run flask app"""

from flask import Flask, render_template, make_response, request
from models import get_all_players, get_kickers
from get_weeks_models import get_weeks, get_kickers_weeks

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST', 'GET'])
def players():
    """home page displays all players"""
    qbs, rbs, wrs, tes = get_all_players()
    kickers = get_kickers()
    html = render_template('players.html',
                           qbs=qbs,
                           rbs=rbs,
                           wrs=wrs,
                           tes=tes,
                           kickers=kickers)
    response = make_response(html)
    return response

@app.route('/details', methods=['GET'])
def details():
    """player stats"""
    player_id = request.args.get('player_id')
    player = request.args.get('player')
    # print(player)
    # print(player_id)
    weeks = get_weeks(player_id)
    kicker = request.args.get('kicker')
    # print(kicker)
    kickers_weeks = get_kickers_weeks(kicker)
    photo = request.args.get('photo')
    # print(kickers_weeks)
    html = render_template('details.html',
                            player_id=player_id,
                           weeks=weeks,
                           player=player,
                           kicker=kicker,
                           kickers_weeks=kickers_weeks,
                           photo=photo)
    response = make_response(html)
    return response

if __name__ == '__main__':
    """runs the application on a server"""
    app.run(debug=False, host='0.0.0.0', port=8000)
