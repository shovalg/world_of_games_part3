# from flask import Flask, render_template, request
# from Utils import SCORES_FILE_NAME
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def score_server():
#     with open(SCORES_FILE_NAME, 'r', encoding='utf-8') as scores_file:
#         score = scores_file.read()
#     return render_template("public/index.html", SCORE=score)
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
