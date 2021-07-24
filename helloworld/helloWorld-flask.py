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
    if age<=5:
        return "<html><body><h2>Your kid is "+ str(age) + "years old and so should be in or admitted to Nursery School</h2></body></html>"
    else:
        return "<html><body><h2>Your kid is "+ str(age) + "years old and so must be studying in Little Primary School</h2></body></html>"

@app.route('/secondary/<int:age>')
def secondary(age):
    if age<18:
        return "<html><body><h2>Your kid is "+ str(age) + "years old and so must be studying in Higher Secondary School</h2></body></html>"
    else:
        return "<html><body><h2>Your kid is "+ str(age) + "years old and so should have completed Higher Secondary School and either pursuing college/university studies or job!</h2></body></html>"


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
    # modified the port from 5000 to 80 to allow execution from mac OS as there is a known bug with Docker Networks 
    # based on the suggestion in the below link, modified this code
    # https://docs.docker.com/docker-for-mac/networking/
    app.run(host='0.0.0.0', port=80, debug=True)

