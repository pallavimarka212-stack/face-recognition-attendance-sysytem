from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    os.system('python main.py')  # runs your backend
    return "Attendance Started... Check your webcam!"

if __name__ == '__main__':
    app.run(debug=True)