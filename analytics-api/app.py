from config import file_path
import os
from flask import Flask,render_template,request,jsonify
from analytics.data_cleaning_saving import data_cleaner_saver
import pandas as pd
from analytics.general_analytics import generate_finance_img

app = Flask(__name__)

#-------------------------------------------------------#

#To clean the i/p data
@app.route('/show/clean', methods=['GET'])
def show_data():
    data_cleaner_saver(file_path)
    return {"msg":"Data cleaned and saved!"}

#-------------------------------------------------------#

@app.route('/show/general', methods=['GET'])
def general_analytics():
    data_size = data_cleaner_saver(file_path).shape[0]
    # generate_finance_img(data_cleaner(file_path))
    data_json = {"size":data_size, }
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