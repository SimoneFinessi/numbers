from flask import Flask,render_template
import random
app = Flask(__name__)
x=0
@app.route('/', methods=['GET'])
def tour():
    return render_template("PhotoFolio/index.html")

@app.route('/numero/<num>', methods=['GET'])
def indovina(num):
  global x
  x+=1
  ran=random.randint(1,9)
  print(ran)
  if int(num)==ran:
    vinto=x
    x=0
    return render_template("vinto5.html",tenta=vinto)
  else:
    return render_template("perso5.html",tenta=x)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)