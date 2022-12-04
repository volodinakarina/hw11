from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = utils.load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<name>")
def get_candidates_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skill(skill):
    candidates = utils.get_candidates_by_skill(skill)
    return render_template('skill.html', skill=skill, candidates=candidates, count=len(candidates))


app.run(debug=True)
