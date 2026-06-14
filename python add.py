# Hello World!
pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/run-python')
def run_python():
    result = "Hello World!"
    return f"""
    <html>
    <head>
        <title>Python Result</title>
        <style>
            body {{ background-color: #1e1e1e; color: #00ff00; font-family: monospace; padding: 50px; font-size: 24px; }}
        </style>
    </head>
    <body>
        <p>> {result}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=8000, debug=True)
