from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
    return render_template("numeri3.html")

@app.route('/numero/<num>', methods=['GET'])
def indovina(num):
  ran=random.randint(1,9)
  if int(num)==ran:
    return render_template("vinto.html")
  else:
    return render_template("perso.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)