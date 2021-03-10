from flask import Flask, Response
import random

app = Flask(__name__)

species = ["Witch", "Vampire", "Werewolf", "Siphoner", "Hybrid",
           "Original", "Ancestor", "Original Witch", "Vampire Hunter"]


@app.route('/thespecies', methods=["GET"])
def thespecies():
    rspecies = random.choice(species)
    return Response(rspecies, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
