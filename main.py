"""main file to run flask app"""

from flask import Flask, render_template, make_response, request
from models import get_all_players, get_weeks

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST', 'GET'])
def players():
    """home page displays all players"""
    players = get_all_players()
    html = render_template('players.html',
                           players=players)
    response = make_response(html)
    return response

@app.route('/details', methods=['GET'])
def details():
    """player stats"""
    player_id = request.args.get('player_id')
    player = request.args.get('player')
    # print(player_id)
    weeks = get_weeks(player_id)
    html = render_template('details.html',
                           weeks=weeks,
                           player=player)
    response = make_response(html)
    return response

if __name__ == '__main__':
    """runs the application on a server"""
    app.run(debug=False, host='0.0.0.0', port=8000)
