from flask import Flask, request
import git
app = Flask(__name__)

# @app.route("/update_server", methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         repo = git.Repo('https://tatiyana.pythonanywhere.com')
#         origin = repo.remotes.origin
#
#         origin.pull()
#         return 'Обновление прошло успешно', 200
#     else:
#         return 'Что-то пошло не так', 400

@app.route("/", methods=['GET'])
def webhook():
    if request.method == 'GET':
        repo = git.Repo('~/GitPython/.git')
        origin = repo.remotes.origin

        origin.pull()
        return 'Обновление прошло успешно', 200
    else:
       return 'Что-то пошло не так', 400

# @app.route("/")       #?
# def home():
#     return "Вовка морковка!"
#
# if __name__ == '__main__':
#     app.run(host='192.168.136.138')
