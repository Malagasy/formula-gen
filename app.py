import json
import sys  # noqa
from argparse import ArgumentParser

from flask import Flask, jsonify

from Equation import Generator

sys.path.append('lib')  # noqa


parser = ArgumentParser()

parser.add_argument("-e", "--equation", help="Equation to be parsed")

args = parser.parse_args()

app = Flask(__name__)


@app.route("/equation/<int:number_terms>/<string:signs>")
def calcul(number_terms, signs):
    signs = signs.split(",")
    try:
        equation = Generator().generate(number_terms, signs)
        return json.dumps({
            "data": str(equation)
        })
    except Exception:
        return json.dumps({
            "error": "Invalid arguments provided to generate equation."
        })


if __name__ == '__main__':
    app.run(debug=True)
