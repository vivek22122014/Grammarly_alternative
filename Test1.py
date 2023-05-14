# from textblob import TextBlob

# def test(text):
#     words=[]
#     print("\n")
#     words.append(text)
#     corrected_word=[]

#     for i in words:
#         corrected_word.append(TextBlob(i))

#         print("Corrected words")
#     for i in corrected_word:
#         res_final=i.correct()
#         # print(res_final)
#     return res_final
# text=input("Enter text: ")
# res=str(test(text))

# print(res)

from flask import Flask 

app = Flask(__name__) 
 
 
@app.route("/") 
def hello():   
    return "Hello there vivek!"
 
if __name__ == "__main__": 
    app.run() 