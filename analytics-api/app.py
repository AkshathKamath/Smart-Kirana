from config import file_path
import os
from flask import Flask,render_template,request,jsonify,json
import pandas as pd
from data.data_cleaning_saving import data_cleaner_saver
from data.data_extracting import data_extractor
from data.data_deleting import data_deleter
from data.data_exist_checking import data_checker
from analytics.general_overview import gen_overview_1, gen_overview_2, gen_overview_3,gen_overview_img_1, gen_overview_img_2

app = Flask(__name__)

#-------------------------------------------------------#

#To check if data exists
@app.route('/show/check', methods=['GET'])
def check_data():
    ct= data_checker()
    return jsonify({"msg":ct})

#-------------------------------------------------------#

#To clean the i/p data
@app.route('/show/clean', methods=['GET'])
def save_data():
    data_deleter()
    msg  = data_cleaner_saver(file_path)
    return msg

#-------------------------------------------------------#

@app.route('/show/general/1', methods=['GET'])
def general_analytics_1():
    df = data_extractor()
    gen_overview_img_1(df)
    gen_1 = gen_overview_1(df)
    
    data_json = gen_1
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/general/2', methods=['GET'])
def general_analytics_2():
    df = data_extractor()
    gen_2 = gen_overview_2(df)

    data_json = gen_2
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/general/3', methods=['GET'])
def general_analytics_3():
    df = data_extractor()
    gen_overview_img_2(df)
    gen_3 = gen_overview_3(df)

    data_json = gen_3
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/size', methods=['GET'])
def show_size():
    df = data_extractor()
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