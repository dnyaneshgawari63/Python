from flask import Flask

app = Flask(__name__)

@app.route('/')

def abc():
    return "Hi everyone, how are you! I think the journey is going to quite interesting"


if __name__ == '__main__':
    app.run(debug=True,port = 5000)
