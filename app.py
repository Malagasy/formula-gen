import sys  # noqa # isort:skip
sys.path.append('lib')  # noqa # isort:skip

import json

from flask import Flask, jsonify
from flask.globals import request

from Equation import Generator
from Response import Response

app = Flask(__name__)


@app.route("/batch/<int:count>/equation/<int:number_terms>")
def get_multiple_equation(count, number_terms):
    i = 0
    error: str = None
    data: [str] = []
    while i < count:
        equation_response = get_equation(number_terms)
        response_object = json.loads(equation_response)
        if "error" in response_object:
            error = response_object["error"]
            break
        data.append(response_object["data"])
        i += 1

    if error is not None:
        return Response.failure(error)

    return Response.success(data)


@app.route("/equation/<int:number_terms>")
def get_equation(number_terms):
    if request.args.get('signs') is None:
        return Response.failure("Parameter `signs` is not provided.")

    signs = request.args.get('signs').split(",")
    try:
        equation = Generator().generate(number_terms, signs)
        return Response.success(str(equation))
    except Exception as error:
        return Response.failure(format(error))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
