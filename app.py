from flask import Flask, render_template

from candidates import candidates, json_candidates, candidates_skills

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template("index.html", candidates=json_candidates)


@app.route("/candidates/<int:id>")
def page_candidates(id):
    return candidates(id)


@app.route("/skills/<skill>")
def page_skills(skill):
    return candidates_skills(skill)


if __name__ == '__main__':
    app.run(debug=True)
