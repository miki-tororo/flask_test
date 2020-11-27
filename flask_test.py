from flask import Flask,render_template,request
import codecs

app=Flask(__name__)


@app.route("/")
def hello_world():
    name_list=["a","b","c"]

    return render_template("index.html",name_list=name_list)

@app.route("/form")
def form():
    text="from"
    file=codecs.open("articles.txt","r","utf-8")
    lines=file.readlines()
    file.close()

    return render_template("form.html",text=text,lines=lines)



@app.route("/menu2")
def menu2():
    text="text2"
    return render_template("menu2.html",text=text)

@app.route("/result", methods=["GET","POST"])
def result():
    text="result"

    if request.method=="POST":
        article=request.form["article"]
        name=request.form["name"]
    else:
        article=request.args.get("article")
        name=request.args.get("name")

        #a is add_text_mode
    file=codecs.open("articles.txt","a","utf-8")
    file.write("\n" + article + "," + name + "\n")
    file.close()

    return render_template("result.html",text=text,article=article,name=name)



if __name__ == "__main__":
    app.run(debug=True)


#http://localhost:5000/
