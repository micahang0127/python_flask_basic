from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/test', methods=['GET', 'POST']) 
def testRoute(): 
    if request.method == 'GET': 
        return "GET으로 전달" 
    else: 
        return "POST로 전달"








#  [실행] 
#   방법1 - 해당 폴더에서  $ flask run   입력

#   방법2 -  아래 코드 있으면,  $ py app.py   입력
if __name__ == '__main__':
    # app.run()

    app.run(debug=True)         
    #  debug=True를  넣으면 route 추가 시 마다 재시작 안해도 된다.(없을경우 재시작 필요)
    #  app.debug = True 또는 app.run(debug=True)  -> 둘다 같은 작용