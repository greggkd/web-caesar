from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 520px;
                }
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" />
                <input type="textarea" name="text" />
                <input type="submit">
            </form>
        </body>
    </html>
"""
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotate = request.form['rot']
    message = request.form['text']

    rotate = int(rotate)
    message = str(message)
    
    encrypted = rotate_string(message,rotate)

    return '<h1>You submitted ' + encrypted + '</h1>'


    
app.run()