from flask import Flask, flash , redirect ,url_for
#WSGI APPLICATION
app = Flask(__name__)

@app.route('/')
def wecome():
    return 'welcome '

@app.route('/sucess/<int:score>')
def success(score):
    return 'your score is ' + str(score) +' you have passed the exam'

@app.route('/fail/<int:score>')
def fail(score):
    return 'your score is ' + str(score) +' you have failed the exam'

#result checker 
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks <50 :
        result = 'fail'
    else :
        result = 'success'
    return   redirect(url_for(result,score= marks))       


if __name__ == '__main__':
    app.run(debug= True)
    
    
