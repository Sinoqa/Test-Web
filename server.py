from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key ="coolaid"



@app.route('/')
def home():
    animals = [    "Lion",    "Tiger",    "Elephant",    "Giraffe",    "Zebra",    "Hippopotamus",    "Rhinoceros",    "Jaguar",    "Leopard",    "Gorilla",    "Chimpanzee",    "Kangaroo",    "Koala",    "Panda",    "Bear",    "Wolf",    "Fox",    "Deer",    "Squirrel",    "Raccoon"]
    return render_template("index.html", animal_list = animals)

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['age'] = request.form['AGE']
    session['type'] = request.form['type']
    session['comments'] = request.form['comments']
    print(session)
    return redirect('/results')

@app.route('/results')
def result():
    return render_template('result.html')
















if __name__ == "__main__":
    app.run(debug=True)
