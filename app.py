from flask import Flask, render_template, request
from agent import agent_decision
from private_cloud import process_private
from public_cloud import process_public

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    task = request.form["task"]

    decision, load = agent_decision()

    if decision == "private":
        result = process_private(task)
        cloud = "Private Cloud"
    else:
        result = process_public(task)
        cloud = "Public Cloud"

    return render_template("result.html",
                           task=task,
                           cloud=cloud,
                           load=load,
                           result=result)

if __name__ == "__main__":
    app.run(debug=True)