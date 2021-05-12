from flask import Flask, Response
import random

app = Flask(__name__)

africa = ["Cairo", "Mogadishu", "Harare", "Accra", "Luanda"]
europe = ["Riga", "Valletta", "Pristina", "Reykjavik", "Sarajevo"]
south_america = ["Caracas", "Lima", "Buenos Aires", "Montevideo", "Bogota"]
north_america = ["Port Au Prince", "New Orleans",
                 "Mexico City", "Havana", "Nuuk"]
asia = ["Kuala Lumpur", "Hanoi", "Kabul", "Amman", "Islamabad"]


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def place():
    
    return Response(, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
