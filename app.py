import json
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    data=[]
    with open('data.json','r') as f:
        data=json.load(f)
    f.close()
    return render_template('index.html',user=data)

if __name__=="__main__":
    app.run(debug=True)
    