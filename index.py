import sys
from flask import Flask, render_template, request
from numpy.core import double

from model import ClassifierModel

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route("/checkResults", methods=['POST'])
def return_winner():
	sepal_length_cm = request.form['SepalLengthCm']
	sepal_width_cm = request.form['SepalWidthCm']
	petal_length_cm = request.form['PetalLengthCm']
	petal_width_cm = request.form['PetalWidthCm']
	print(sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm, file=sys.stderr)
	return get_predictions(double(sepal_length_cm), double(sepal_width_cm), double(petal_length_cm), double(petal_width_cm))


def get_predictions(sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm):

	classifier = ClassifierModel()
	classifier.load_pickle()
	predicted_class = classifier.run_model([[sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm]])
	print(predicted_class)
	return predicted_class[0]


if __name__ == '__main__':
	app.run(debug=True)
