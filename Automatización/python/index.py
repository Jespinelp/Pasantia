from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return 'holiwi'

if __name__ == 'main':
    app.run()