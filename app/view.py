from flask import Blueprint, render_template,request

main = Blueprint('main',__name__,static_folder='static')

@main.route('/')
def index():
    return render_template("index.html")


@main.route('/sign',methods=["GET","POST"])
def sign():
    if request.method == "POST":
        print(request.form)
    return render_template("sign.html")    