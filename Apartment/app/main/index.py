# file name : index.py
# pwd : /project_name/app/main/index.py

from flask import Blueprint, request, render_template#, index_add_counter
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/main', methods=['GET'])
def index():
    testData = 'testData array'
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
    return render_template('/main/index.html',testDataHtml = city)

city='1'
gungu='2'
emd =''


@main.route('/main', methods=['POST', 'GET'])
def addRegion():
    #global city = request.form.getvalue['address']
    city = (request.form['city-Input'])
    gungu= str(request.form['gungu-Input'])
    emd = str(request.form['emd-Input'])
    return render_template('/main/index.html', city=city, gungu = gungu, emd=emd)
