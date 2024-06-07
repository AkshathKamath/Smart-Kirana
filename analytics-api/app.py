from config import file_path
import os
from flask import Flask,render_template,request,jsonify
from analytics.data_cleaning import data_cleaner
import pandas as pd

app = Flask(__name__)

#-------------------------------------------------------#

@app.route('/showData', methods=['GET'])
def show_data():
    data_size = data_cleaner(file_path).shape[0]
    data_json = {"size":data_size}
    return jsonify(data_json)

#-------------------------------------------------------#




@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)