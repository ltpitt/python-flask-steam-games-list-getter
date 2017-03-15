from flask import Flask, send_file, make_response, render_template, request, redirect, url_for, jsonify
import requests
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] =  os.getcwd()

@app.route('/', methods=['GET', 'POST'])
def main():
    """
    Show the main page
    :return:
    """
    if request.method == 'POST':
        return request.data
    else:
        print "Get"
        return render_template('index.html')

@app.route('/get-steam-games-owned-by', methods=['GET', 'POST'])
@app.route('/get-steam-games-owned-by/', methods=['GET', 'POST'])
def get_steam_games_owned_by():
    """
    Get complete list of games for specified user using Steam API
    :return:
    """
    if request.method == 'POST':
        steam_username = request.form['steam-username']
        steam_api_string = "http://steamcommunity.com/id/" + steam_username + "/games?tab=all&xml=1"
        result = requests.get(steam_api_string)
        response = make_response(result.content)
        response.headers["Content-Disposition"] = "attachment; filename=steamgames.xml"
        print request.data
        return response
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
