from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    #return '<html><body><h1>Welcome to my Hello World Python Flask webpage!</h1></body></html>'
    return render_template('index.html')

@app.route('/courses')
def inputForm():
    return render_template('indexForm.html')

@app.route('/primary/<int:age>')
def primary(age):
    return "<html><body><h2>Your kid is "+ str(age) + "years old and studying in Little Primary School</h2></body></html>"

@app.route('/secondary/<int:age>')
def secondary(age):
    return "<html><body><h2>Your kid is "+ str(age) + "years old and studying in Higher Secondary School</h2></body></html>"

@app.route('/passingscore')
def passingScore():
    return "<html><body><h2>The passing score is 35 marks.</h2></body></html>"

@app.route('/passingscore/<int:score>')
def checkScore(score):
    result=''
    if score<35:
        result='failed'
    else:
        result='passed'
    return "<html><body><h2>The passing score is 35 marks.</h2><br><h3> Student "+ result+ " with "+ str(score) +"</h3></body></html>"

@app.route('/findgrade/<int:yrs>')
def findgrade(yrs):
    if yrs<11:
        return redirect(url_for('primary',age=yrs))
    else:
       return redirect(url_for('secondary',age=yrs))

@app.route('/submit', methods=['POST'])
def submit():
    return "You are successfully registered for the course. Hooray!"

if __name__ == '__main__':
    app.run(debug=True)

