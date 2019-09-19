#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:25:14 2019

@author: ubuntu
"""
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract as pys
from werkzeug import secure_filename


from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('/home/ubuntu/Diyab/uploads/out.pdf')
      print(f)
      images = convert_from_path('/home/ubuntu/Diyab/uploads/out.pdf')
      i=0
      txt=""
      for page in images:
          page.save('/home/ubuntu/Diyab/out'+str(i)+'.jpg','JPEG')
          txt = txt+pys.image_to_string(Image.open('/home/ubuntu/Diyab/out'+str(i)+'.jpg'))
          i=i+1
      return txt


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)