from forer import get_text_from_horoscope
from forer import signs
from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def send_horoskop():
    return render_template('test.html', signs=signs)


@app.route('/<sign>')
def get_horoskop_for_sign(sign):

    hor = get_text_from_horoscope(sign)
    if hor == TypeError:
        return "<h2> error </h2>"

    else:
        hoftext = json.loads(hor)["text"]

        return render_template("horoskop.html", sign=sign, hor=hoftext)
        #return render_template("horoskop.html", sign=sign, hor=hor)



if __name__ == '__main__':
    app.run(debug=True, port=8080)