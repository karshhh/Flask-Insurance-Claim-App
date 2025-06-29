from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

claims = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/claim', methods=['GET', 'POST'])
def claim():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'policy_number': request.form['policy_number'],
            'amount': request.form['amount'],
            'status': 'Pending'
        }
        claims.append(data)
        return redirect(url_for('status'))
    return render_template('claim.html')

@app.route('/status')
def status():
    return render_template('status.html', claims=claims)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)