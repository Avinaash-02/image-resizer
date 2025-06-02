# from flask import Flask,render_template,request,send_file
# from PIL import Image
# import os
# from io import BytesIO

# app=Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def upload():
#     if request.method=='POST':
#         file = request.files['image']
#         if file:
#             img=Image.open(file)
#             img=img.convert("RGB")
#             original_size=img.size

#             img=img.resize(original_size,Image.Resampling.LANCZOS)
#             output=BytesIO()
#             img.save(output,format='PNG',optimize=True,quality=95)
#             output.seek(0)

#             return send_file(output,as_attachment=True,download_name="resized_image.png",mimetype="image/png")
#         return render_template('upload.html')


from flask import Flask, render_template, request, send_file
from PIL import Image
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            img = Image.open(file)
            img = img.convert('RGB')
            original_size = img.size
            img = img.resize(original_size, Image.Resampling.LANCZOS)

            # Save image in memory
            output = BytesIO()
            img.save(output, format='WEBP', optimize=True, quality=80)
            output.seek(0)

            return send_file(output, as_attachment=True, download_name='resized_image.webp', mimetype='image/png')
    return render_template('upload.html')
