from config import file_path
import os
from flask import Flask,render_template,request,jsonify,json
import pandas as pd
from analytics.data_cleaning_saving import data_cleaner_saver
from analytics.general_overview import gen_overview_1, gen_overview_2, gen_overview_3,gen_overview_img
from analytics.financial_analysis import generate_finance_img_1

app = Flask(__name__)

#-------------------------------------------------------#

#To clean the i/p data
@app.route('/show/clean', methods=['GET'])
def save_data():
    data_cleaner_saver(file_path)
    return {"msg":"Data cleaned and saved!"}

#-------------------------------------------------------#

@app.route('/show/general/1', methods=['GET'])
def general_analytics_1():
    df = data_cleaner_saver(file_path)
    gen_1 = gen_overview_1(df)
    

    data_json = gen_1
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/general/2', methods=['GET'])
def general_analytics_2():
    df = data_cleaner_saver(file_path)
    gen_2 = gen_overview_2(df)

    data_json = gen_2
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/general/3', methods=['GET'])
def general_analytics_3():
    df = data_cleaner_saver(file_path)
    gen_overview_img(df)
    gen_3 = gen_overview_3(df)

    data_json = gen_3
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/size', methods=['GET'])
def show_size():
    df = data_cleaner_saver(file_path)
    data_size = df.shape[0]
    gen_1 = {"size": data_size}

    data_json = gen_1
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