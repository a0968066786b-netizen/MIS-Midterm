import os
from flask import Flask, render_template

# 加上 os.path 確保 Vercel 能在伺服器上精確定位資料夾
app = Flask(__name__, 
            static_folder=os.path.join(os.getcwd(), 'static'),
            template_folder=os.path.join(os.getcwd(), 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/direction')
def direction():
    return render_template('direction.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

if __name__ == '__main__':
    app.run(debug=True)
