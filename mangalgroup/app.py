from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)

# Route for the index page (UI)
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling chatbot responses
@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json['message'].lower()

    # Check the message and respond accordingly
    if 'hello' in user_message or 'hi' in user_message or 'whatsapp' in user_message:

        bot_response = "Hello! How can I assist you today?"
    elif 'services' in user_message:
        # Provide a download link for the services brochure or image
        bot_response = "We offer a variety of services. You can view our brochure here: <a href='/download-brochure'>Download Brochure</a>"
    elif 'contact' in user_message:
        bot_response = "You can contact us at contact@digitaledge.com."
    else:
        bot_response = "Let me look into that for you."

    return jsonify({'response': bot_response})

# Route for serving the brochure PDF or image
@app.route('/download-brochure')
def download_brochure():
    brochure_path = os.path.join('static', 'brochure.pdf')  # Assuming brochure.pdf is in the 'static' folder
    return send_file(brochure_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
