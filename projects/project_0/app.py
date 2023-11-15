from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask application
app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')


if __name__ == '__main__':
    app.run(debug=True)