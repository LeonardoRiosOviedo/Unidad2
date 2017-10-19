from area import rombo_area
from flask import Flask, render_template,redirect,request

app = Flask (__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')

@app.route('/entry/')
def go_entry()->'html':
    return render_template('entry.html', tittle='welcome to the form')

@app.route('/calculate/', methods=['POST'])
def calculate()->'html':
    D= float(request.form['D'])
    d = float(request.form['d'])

    result = rombo_area(D,d)
    tittle = "Area rombo result.html"
    return render_template('result.html',the_D=D ,the_d=d, the_result = result,the_tittle=tittle)
app.run(debug=True)