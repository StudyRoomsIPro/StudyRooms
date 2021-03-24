from flask import Flask, render_template, url_for
app= Flask(__name__)

# this file is used by devs for local developement
# to run simply python3 web_app.py and then in your browser go to localhost:5000

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.static_folder='static'
    app.run(debug=True)
