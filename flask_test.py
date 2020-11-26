from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def hello_world():
    name_list=["a","b","c"]
    
    return render_template("index.html",name_list=name_list)

@app.route("/info")
def info():
    return "Flask"



if __name__ == "__main__":
    app.run(debug=True)


#http://localhost:5000/
