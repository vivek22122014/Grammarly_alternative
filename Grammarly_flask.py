from flask import Flask 
import requests
from flask import Flask, request, render_template, send_file, jsonify, Response
from textblob import TextBlob
from flask_cors import CORS

def test(text):
    words=[]
    # print("\n")
    words.append(text)
    corrected_word=[]

    for i in words:
        corrected_word.append(TextBlob(i))

        # print("Corrected words")
    for i in corrected_word:
        res_final=i.correct()
        # print(res_final)
    return res_final



app = Flask(__name__) 
CORS(app)
@app.route("/",methods=["POST"])#
def hello():   
    data=request.get_json(force=True)
    print(data)
    text = data['fname']
    print(text)
    # text="I lov natue."
    # text=input()
    res=str(test(text))
    print(res)
    return jsonify(res)
 
if __name__ == "__main__": 
    app.run() 