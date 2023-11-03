import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])  #Se agrega la ruta para la multiplicación
def multiply(op_1, op_2): #se define la funcióon para la operación de multiplicación
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.multiply(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"]) #Se agrega la ruta para la división
def divide(op_1, op_2): #se define la funcióon para la operación de división
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        if num_2 == 0:
            return ("Division by zero is not allowed", http.client.BAD_REQUEST, HEADERS)
        return ("{}".format(CALCULATOR.divide(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"]) #Se agrega la ruta para la potenciación
def power(op_1, op_2): #se define la funcióon para la operación de potenciación
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.power(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/square_root/<op_1>", methods=["GET"]) #Se agrega la ruta para la raiz cuadrada
def square_root(op_1): #se define la funcióon para la operación de raiz cuadrada
    try:
        num_1 = util.convert_to_number(op_1)
        if num_1 < 0:
            return ("Square root is not defined for negative numbers", http.client.BAD_REQUEST, HEADERS)
        return ("{}".format(CALCULATOR.square_root(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/logarithm/<op_1>", methods=["GET"]) #Se agrega la ruta para el logarítmo
def logarithm(op_1): #se define la funcióon para la operación de logarítmo
    try:
        num_1 = util.convert_to_number(op_1)
        if num_1 <= 0:
            return ("Logarithm is not defined for non-positive numbers", http.client.BAD_REQUEST, HEADERS)
        return ("{}".format(CALCULATOR.logarithm(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)