# python_flask_basic
python flask 기본사용

---

### Flask(플라스트)란? 
python backend framwork

---
    
### 기본사용구조

       
    from flask import 
    Flask app = Flask(__name__)
    
    // flask 모듈(해당파일)을 소스에 포함시키고 Flask를 사용가능하게 선언
    // app에 Flask()를 넘겨 app 전역객체로 사용 할 수있게 해준다.
    // __name__ 은 파이썬의 내부적인 특변한 변수로써, 모듈의 이름을 뜻하는데 실행이 되는 파일(모듈)은 __main__이된다. 

<br/>

    app = Flask(__name__)                      // 단일모듈
    app = Flask('application명 지정')          // 패키지 형태
    
    // 단일 모듈을 사용할 때는 따로 지정 하지 않고 __name__ 을 사용 하면 되지만 
    // 패키지 형태로 사용 할 경우 패키지 이름을 직접 써줘야 합니다.

<br/>

    if __name__ == '__main__': 
    app.run()
    
    // 이 파일(모듈)이 직접사용되는지, import되어 사용되는지 알 수 있는 부분이다.
    // 즉, 프로그램의 시작점이라고 볼 수 있다.
    // 만약, 실행 시, 위 코드가 있는 파일(모듈)의 __name__은  __main__이 들어가므로 app.run() 실행이 된다. 
    
 <br/>
 
    @app.route('/')
    
    @은 데코레이터(decorator)라고 부르고 이를 app의 객체의 route함수에 request인자를 넘겨 HTTP요청을 처리한다

