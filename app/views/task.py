from flask import blueprints

task = blueprints.Blueprint("task", __name__, url_prefix="/task")

@task.route("/", methods=["GET"])
def test():
    return "ok"