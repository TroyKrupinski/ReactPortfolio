from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linkedin')
def linkedin():
    return render_template('linkedin.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you'd handle your form submission, e.g., save data, send an email
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # For now, let's just redirect to the home page
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
