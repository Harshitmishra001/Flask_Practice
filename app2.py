from flask import Flask,render_template,request,url_for,redirect
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def welcome():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/index',methods=['GET','POST'])
def index():
    return "This is the Index Page"
## Variable  rules
@app.route('/success/<int:score>',methods=['GET','POST'])
def success(score):
    return f"The person has passed and score is: {score}"
@app.route('/fail/<int:score>',methods=['GET','POST'])
def fail(score):
    return f"The person has failed and score is: {score}"
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths=float(request.form['Maths'])##Write the name defined in form
        science=float(request.form['Science'])

        avgMarks=(maths+science)/2
        if avgMarks>=60:
            res='Success'
        else:
            res='Fail'
        return redirect(url_for(res,Score=avgMarks))
if __name__=="__main__":
    app.run(debug=True)