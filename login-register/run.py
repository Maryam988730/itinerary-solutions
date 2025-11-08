from app import create_app, db

app = create_app()

@app.route('/')
def home():
    return "Welcome! Go to /login or /register"

@app.route('/dashboard')
def dashboard():
    return "You are logged in!"

if __name__ == '__main__':
    app.run(debug=True)
