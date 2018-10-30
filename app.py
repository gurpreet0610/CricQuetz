from flask import Flask, request, jsonify, render_template
from get_players import players
from final_result import finale
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/players', methods=['POST'])
def player():
    t1=request.form['t1']
    t2=request.form['t2']
    p=players()
    return json.dumps({'team_1':p.get_players(t1),'team_2':p.get_players(t2)})

@app.route('/result', methods=['POST'])
def get_result():
    content= request.json
    f=finale()
    out=f.finale_result(content)
    return json.dumps(out)



if __name__ == "__main__":
    app.run()







    
