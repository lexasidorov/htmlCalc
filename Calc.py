from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("calc.html")

@app.route('/ajax',methods=['POST'])
def calc():
    if request.method == 'POST':
        x = request.json['x']
        try:
            y = eval(x)
            print(str(y))
            return str(y)
        except:
            return {"error": "invalid input"}
    return {"error": "wrong method"}
if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1')