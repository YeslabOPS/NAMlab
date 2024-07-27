from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    about_url = url_for('about')

    return render_template('sample.html', about_url=about_url)

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True)
