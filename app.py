from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Load portfolio data
def load_portfolio_data():
    with open('data/portfolio.json', 'r') as file:
        return json.load(file)

# Routes
@app.route('/')
def index():
    portfolio_data = load_portfolio_data()
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    portfolio_data = load_portfolio_data()
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    portfolio_data = load_portfolio_data()
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you would typically save this to a database or send an email
        print(f"Message from {name} ({email}): {message}")
        
        return redirect(url_for('contact_success'))
    
    portfolio_data = load_portfolio_data()
    return render_template('contact.html', data=portfolio_data)

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')

if __name__ == '__main__':
    # Get the port from the environment variable or use 10000 as default
    port = int(os.environ.get('PORT', 10000))
    # Run the app on all available IPs (0.0.0.0) and the specified port
    app.run(host='0.0.0.0', port=5000, debug=False)

