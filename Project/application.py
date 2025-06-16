from flask import Flask,render_template,request,redirect, url_for

application = Flask(__name__)

@application.route("/")
def main():
    return render_template('index.html')

@application.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        Temperature = request.form['Temperature']
        RH = request.form['RH']
        Ws = request.form['Ws']
        Rain = request.form['Rain']
        FFMC = request.form['FFMC']
        DMC = request.form['DMC']
        ISI = request.form['ISI']
        Classes = request.form['Classes']
        Region = request.form['Region']
        result = Temperature
        return f'data collected {result}'
    else:
        return render_template('form.html')
    
@application.route('/result/<int:score>')
def marks(score):
    res = ""
    res = "Passed" if score>=50 else "Failed"
    dic = {'score':score, 'result':res}
    return render_template('results.html',results=dic)

if __name__ == "__main__":
    application.run(debug=True)