from flask import Flask, Response
import random

app = Flask(__name__)

africa = ["Cairo", "Mogadishu", "Harare", "Accra", "Luanda"]
europe = ["Riga", "Valletta", "Pristina", "Reykjavik", "Sarajevo"]
south_america = ["Caracas", "Lima", "Buenos Aires", "Montevideo", "Bogota"]
north_america = ["Port Au Prince", "New Orleans",
                 "Mexico City", "Havana", "Nuuk"]
asia = ["Kuala Lumpur", "Hanoi", "Kabul", "Amman", "Islamabad"]


@app.route('/place', methods=['GET'])
def place():
    pick1 = random.choice(africa)
    pick2 = random.choice(europe)
    pick3 = random.choice(south_america)
    pick4 = random.choice(north_america)
    pick5 = random.choice(asia)
    rplace = [pick1, pick2, pick3, pick4, pick5]
    return Response(random.choice(rplace), mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
