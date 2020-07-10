from flask import Flask , render_template
import  requests
app = Flask (__name__)

@app.route('/')
def home():
    data= requests.get("https://disease.sh/v2/countries/India")
    data_dic=data.json()

    return render_template("home.html", data=data_dic)

if __name__=="__main__":
    app.run()
