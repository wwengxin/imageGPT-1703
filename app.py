from flask import Flask,request,render_template
import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "f8f1b15c353f4e978b75ae95e22b730d45f0e345"
model = replicate.models.get("tstramer/mid-journey-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        p = request.form.get("txt")
        inputs = {"prompt":p}
        out = version.predict(**inputs)
        return(render_template("index.html",result=out[0]))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()
    
