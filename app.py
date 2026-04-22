## create a simple flast application 
## For learning
from flask import Flask, render_template,request,redirect,url_for

## create the flask app

app = Flask(__name__)

@app.route('/')
def home ():
    return "Hellow world"

@app.route('/welcome')
def welcome ():
    return "welocme to the flask tutorials"

@app.route('/success/<int:score>')
def success (score):
        return "The person is passsed with score" + str(score)
@app.route('/Failed/<int:score>')
def Failed (score):
        return "The person is failed" + str(score)

@app.route('/Calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template("calculate.html") 
    else: 
         maths=float(request.form['maths'])
         science=float(request.form['science'])
         english=float(request.form['english'])

    average_marks= (maths+science+english)/3
    result = ""
    if average_marks>=50:
        result = "success"
    else:
         result ="fail"
    #return redirect(url_for(result,score=average_marks))
    return render_template('result.html',results=average_marks)


@app.route('/index')
def index ():
    return render_template('index.html') ##h1 tag is used for font change thats it





if __name__=='__main__':
    app.run(debug=True)

