import os
import hmac
import hashlib
from flask import Flask, request, abort

app = Flask(__name__)


# Your existing routes (e.g., the home page)
@app.route('/')
def home():
    return "Вовка морковка! 🌟"


# Webhook endpoint to handle GitHub pushes
@app.route('/gitlab-webhook', methods=['POST'])
def gitlab_webhook():
    # Verify the request is from GitHub (see Section 4.5)
    signature = request.headers.get('X-Gitlab-Token')
    if not verify_signature(request.data, signature, 'ce022f09d3ab982c5c49efe5374659328f1c515e158f767bdb53f655dc70f6e8'):
        abort(403)  # Forbidden if signature invalid

        # Pull the latest changes from GitHub
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_path)
    os.system('git pull origin main')  # Replace "main" with your branch name
    # Note: After pulling, you need to manually reload the app via PythonAnywhere's
    # "Web" tab or use their reload API. The virtual environment and WSGI reload
    # cannot be triggered reliably from within a webhook handler.
    return "Changes pulled successfully!", 200


# Helper function to verify GitHub's signature
def verify_signature(payload, signature, secret):
    if not signature:
        return False
    sha_name, signature = signature.split('=')
    if sha_name != 'sha256':
        return False
        # Compute the expected signature
    mac = hmac.new(secret.encode('utf-8'), payload, hashlib.sha256)
    return hmac.compare_digest(mac.hexdigest(), signature)


if __name__ == '__main__':
    app.run(debug=True)