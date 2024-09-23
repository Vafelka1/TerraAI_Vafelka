import os
print("We are currently in the folder of ",os.getcwd())
print("We are currently in the folder of ",os.listdir())

from flask import Flask, request, render_template,redirect
from PIL import Image
from predict_ensemble import *


UPLOAD_FOLDER = 'predicted'

app = Flask(__name__, static_folder='predicted')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('new_index.html')

@app.route("/predicted")
def predicted():
    return render_template('predicted.html')


@app.route("/predict", methods=["post"])
def predict():

    img = request.files['file']
    if not img is None:
        path = os.path.join(app.config['UPLOAD_FOLDER'],'predict.jpg')
        img.save(path)                                  # Выполнение блока, если загружено изображение                                # Открытие изображения
        predict = predict_img_ensamble(path)         # Обработка изображения с помощью функции, реализованной в другом файле
        print(predict)
    return render_template('predicted.html',predict = predict)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
