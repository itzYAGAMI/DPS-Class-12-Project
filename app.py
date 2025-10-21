from flask import Flask, render_template, request, flash, redirect, url_for, session

# Initialize the Flask app
app = Flask(__name__)

# A secret key is needed for sessions and 'flashed messages' to work
app.config['SECRET_KEY'] = 'your_very_secret_key_12345' 

# --- Demo User Data ---
# In a real app, this would come from your SQLite database
DEMO_USERS = {
    "123456789": "1234",
    "987654321": "4321",
    "111122223": "1111"
}
# ----------------------


# Route for the Login Page
@app.route('/')
def index():
    # If user is already logged in, send them to the dashboard
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


# Route to handle the login form submission
@app.route('/login', methods=['POST'])
def login():
    card_number = request.form.get('card_number')
    pin = request.form.get('pin')

    # Check if the card number exists and the PIN is correct
    if card_number in DEMO_USERS and DEMO_USERS[card_number] == pin:
        # Login successful!
        # Store the user's ID in the session to "remember" them
        session['user_id'] = card_number
        return redirect(url_for('dashboard'))
    else:
        # Login failed
        flash("Invalid Card Number or PIN. Please try again.", "error")
        return redirect(url_for('index'))


# Route for the main Dashboard (after login)
@app.route('/dashboard')
def dashboard():
    # Protect this page: if user isn't logged in, send them back to login
    if 'user_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('index'))
    
    # User is logged in, show them the dashboard
    return render_template('dashboard.html')


# Route to handle logging out
@app.route('/logout')
def logout():
    # Remove the user's ID from the session
    session.pop('user_id', None)
    flash("You have been logged out successfully.", "success")
    return redirect(url_for('index'))


# --- Add routes for your other features here ---
# Example:
# @app.route('/withdraw')
# def withdraw_page():
#     if 'user_id' not in session:
#         return redirect(url_for('index'))
#     return render_template('withdraw.html')
#
# (You would need to create 'withdraw.html', 'deposit.html', etc.)
# ------------------------------------------------


# This part runs the app
if __name__ == '__main__':
    app.run(debug=True)