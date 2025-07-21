from flask import Flask ,render_template, request

## WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the flask course"

@app.route('/hello')
def index():
    return render_template('hello.html')



@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'hello{name}¡'
    else:
        return render_template('form.html')
        #
        #



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('re ',  results=res)






   



if __name__=="__main__":
    app.run(debug=True)