
from flask import Flask, render_template, request
import pyshorteners
app = Flask(__name__)
  
@app.route("/", methods=['POST', 'GET'])
def home():
  print('Preparing to execute')
  if request.method=="POST":
    url_received = request.form["url"]
    try:
        short_url = pyshorteners.Shortener().tinyurl.short(url_received)
    except Exception as e:
        short_url = "Error generating short URL"
    print('executing')
    print(short_url)
    return render_template("form.html", new_url=short_url, old_url=url_received)
  else:
    print('in else block')
    return render_template('form.html')
  
if __name__ == "__main__":
 app.run()
