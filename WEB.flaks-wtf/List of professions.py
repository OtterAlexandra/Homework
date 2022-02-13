from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<type>')
def li(type):
    list_prof = ['p', 'o', 'p']
    return render_template('list_prof.html', l=type, profession=list_prof)


app.run(port=8080, debug=True)
