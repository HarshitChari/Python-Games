from flask import Flask, request

from TTT import Tic_Tac_Toe

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():
    return '''
                <html>
                    <title> Tic Tac Toe </title>
                    <body>
                        <p> Click To Play </p>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)
