from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/texts',methods = ['POST', 'GET'])
def RDF_TEXT():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('RDF',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('RDF',name = user))

if __name__ == '__main__':
   app.run(debug = True)
