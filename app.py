import os
from flask import Flask,render_template,request
from src.data_cleaning import data_cleaner

app = Flask(__name__)

## Root path
@app.route('/')
def home():
    return render_template('data_upload.html')

#-------------------------------------------------------#

## Upload Dataset
@app.route('/analyticsForm', methods=['POST'])
def upload_file():
    ## If no file uploaded
    if 'file' not in request.files:
        return 'No file part'
    ## Access file
    file = request.files['file']
    ## If file name null
    if file.filename == '':
        return 'No selected file'
    ##Ideal
    file.filename='supermarket.csv'
    file_path = './datasets/' + file.filename
    file.save(file_path)
    df=data_cleaner(file_path)
    msg = 'File uploaded successfully.'
    return render_template('analytics_form.html', msg=msg,df="")

#-------------------------------------------------------#

## Get to same page
@app.route('/analyticsForm', methods=['GET'])
def show_file():
    file_path = './datasets/supermarket.csv'
    df=data_cleaner(file_path)
    msg="Summary view of file:"
    return render_template('analytics_form.html', msg=msg,df=df.head(5))

#-------------------------------------------------------#



@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)