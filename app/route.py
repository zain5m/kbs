from flask import render_template
from flask import Flask, redirect, url_for, request
import app.quran as q

app = Flask(__name__)


@app.route('/',methods=['GET'])
def homepage():
   return render_template('test.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':

        Aya = request.form.get('aya')
        print(Aya)
        q.aya = Aya
        engine = q.ES()
        engine.reset()
        engine.run()
        data = q.Alahkam
        return render_template("ahkam.html", data=data,aya=Aya)


if __name__ == '__main__':
    app.run(debug=True)
