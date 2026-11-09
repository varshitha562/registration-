from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('registration.html')
@app.route('/registration', methods=['POST'])
def registration():
    name = request.form.get('name') 
    student_id = request.form.get('student_id')
    email = request.form.get('email')
    year = request.form.get('year')
    return render_template('successfull.html', name=name, student_id=student_id, email=email, year=year)
if __name__ == '__main__':
    app.run(debug=True)