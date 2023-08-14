# integrate html with flask 
# http verb GET and POST
# jinja2 template engine
'''
{%...%} for statements
{{}}   --> expressions to print output
{#...#} --> this is for comments 

'''


from flask import Flask, flash , redirect ,url_for ,render_template,request
#WSGI APPLICATION
app = Flask(__name__)

@app.route('/')
def wecome():
    return render_template('index.html')

@app.route('/sucess/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res='FAIL'
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)

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

#result checker, post,get
@app.route('/submit' , methods =['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths= float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    res ="" 
    return redirect(url_for('success', score = total_score))       
      


if __name__ == '__main__':
    app.run(debug= True)