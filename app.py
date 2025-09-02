from flask import Flask, redirect, url_for, request

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_pyfile('config.py', silent=True)

    @app.route('/')
    def home():
        return 'Home Page'

    @app.route('/login')
    def login():
        return redirect(url_for('home',_external=True))

    @app.route('/items')
    def items():
        # Get query parameters from the URL
        category = request.args.get('category')
        return f"Items page with category: {category}"
        
    @app.route('/redirect-to-items')
    def redirect_to_items():
        # Redirect with specific query parameters
        return redirect(url_for('items', _external=True,category='books', sort='asc'))
    
    @app.route('/preserve-params-redirect')
    def preserve_params_redirect():
        # Accept a dict of random query params
        all_params = request.args
        return redirect(url_for('destination',_external=True, **all_params)) # unpack all_params using **
    
    @app.route('/destination')
    def destination():
        all_params = list(request.args)
        return f"Destination with parameters {str(all_params)}"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)