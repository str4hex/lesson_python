from flask import Flask, render_template
from json_load_info_candidates import candidates
from skills import skill_conditations

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("index.html", candidates_all=candidates)


@app.route("/candidates/<int:id>")
def page_candidates(id):
    if id > len(candidates):
        return "Пользователь не найден"
    id = id - 1
    return render_template("candidates.html", name=candidates[id]["name"], picture=candidates[id]["picture"],
                           position=candidates[id]["position"], skills=candidates[id]["skills"])


@app.route("/skills/<skill>")
def skills(skill):
    return render_template("skills.html", skill=skill_conditations(skill))


app.run()