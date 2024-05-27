from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Automation/web_apps_desktop_gui/templates/index.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
