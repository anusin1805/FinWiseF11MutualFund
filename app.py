import os
from flask import Flask, send_from_directory

# We set static_folder to '.' because your JS/CSS files are in the root directory
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # Check if the requested path exists as a file (like CSS or JS)
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        # Otherwise, always serve index.html (important for React Router)
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # Use the port Render provides, or default to 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
