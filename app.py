from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


#  [실행] 
#   방법1 - 해당 폴더에서  $ flask run   입력

#   방법2 -  아래 코드 있으면,  $ py app.py   입력
if __name__ == '__main__':
    app.run()