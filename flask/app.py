import os
import easyocr
from flask import *
from spacyfun import summarize, nlp, Ner
from config import upload_folder, ALLOWED_EXTENSIONS
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from preprocessing import clean_text
from imageai.Detection import ObjectDetection

from googletrans import Translator

current_directory = os.getcwd()

# initializations
text_reader = easyocr.Reader(['en'])  # Initialzing the ocr
translator = Translator()

# image ai
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()

detector.setModelPath(os.path.join(
    current_directory, "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

custom = detector.CustomObjects(person=True, bicycle=True)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Initialize Flask App
app = Flask(__name__)


CORS(app, resources={r"/api/": {"origins": ""}})
cors = CORS(app, supports_credentials=True)
app.config['UPLOAD_FOLDER'] = upload_folder

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'


@app.route('/api/ocr', methods=['GET', 'POST'])
@cross_origin()
def ocr():
    if request.method == "POST":
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            result = text_reader.readtext(path)
            return jsonify({"data": {"ocrText": result}})


@app.route('/api/translate', methods=['GET', 'POST'])
@cross_origin()
def translate():
    if request.method == "POST":
        data = request.get_json()
        translated_text = translator.translate(data['text'])
        return jsonify({"data": {"translatedText": translated_text}})
    if request.method == "GET":
        return jsonify({"data": "Method not allowed"})


@app.route('/api/detection', methods=['GET', 'POST'])
@cross_origin()
def detection():
    if request.method == "POST":
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            detections = detector.detectCustomObjectsFromImage(
                custom_objects=custom,
                input_image=os.path.join(current_directory, path),
                minimum_percentage_probability=70)

            detectionEntites = []
            for eachObject in detections:
                detectionEntites = [eachObject] + detectionEntites

            return jsonify({"data": {"detectionEntites": detectionEntites}})


@app.route('/api/summarize', methods=['GET', 'POST'])
@cross_origin()
def summarization():
    if request.method == "POST":
        data = request.get_json()
        cleanedText = clean_text(data['text'])
        summarizedText = summarize(cleanedText, 0.05)
        return jsonify({"data": {"summarizedText": summarizedText}})
    if request.method == "GET":
        return jsonify({"data": "Method not allowed"})


@app.route('/api/ner', methods=['GET', 'POST'])
@cross_origin()
def nerText():
    if request.method == "POST":
        data = request.get_json()
        cleanedText = clean_text(data['text'])
        nerEntites = Ner(cleanedText)
        return jsonify({"data": {"entites": nerEntites}})
    if request.method == "GET":
        return jsonify({"data": "Method not allowed"})


port = int(os.environ.get('PORT', 7777))
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=port, debug=True)
