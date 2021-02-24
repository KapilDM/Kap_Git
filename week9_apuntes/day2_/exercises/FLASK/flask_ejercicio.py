from flask import Flask,request,jsonify, render_template
import json
import os, sys
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, bienvenido a la API"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            df = pd.read_csv(request.files.get('file'))
            df.to_csv('output.csv', index=False, header=None)
        except:
            df = pd.read_json(request.files.get('file'))
            df.to_json('output_json.csv', index=False, header=None)
        return render_template('upload.html', shape=df.shape) #render_template significa "provides a template"
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=6060) 