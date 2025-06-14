from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
import threading
from DotToDot import makeMaxSizeDot

UPLOAD_FOLDER = 'input'
PROCESSED_FOLDER = 'output/jpg'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB

progress = {'percent': 0, 'status': '', 'stdout': ''}

# Utility to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Background processing thread
def process_image(filename):
    global progress
    try:
        progress['percent'] = 10
        progress['status'] = 'Processing...'
        makeMaxSizeDot(os.path.join(UPLOAD_FOLDER, filename), 800)
        progress['percent'] = 100
        progress['status'] = 'Done!'
    except Exception as e:
        progress['status'] = f'Error: {e}'
        progress['percent'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Start processing in a background thread
            thread = threading.Thread(target=process_image, args=(filename,))
            thread.start()
            return redirect(url_for('progress_view', filename=filename))
    return render_template('index.html')

@app.route('/progress/<filename>')
def progress_view(filename):
    return render_template('progress.html', filename=filename)

@app.route('/progress_status')
def progress_status():
    return jsonify(progress)

@app.route('/preview/<filename>')
def preview(filename):
    # Show both original and processed images
    orig_path = os.path.join(UPLOAD_FOLDER, filename)
    processed_path = os.path.join(PROCESSED_FOLDER, filename)
    orig_exists = os.path.exists(orig_path)
    processed_exists = os.path.exists(processed_path)
    return render_template('preview.html', filename=filename, orig_exists=orig_exists, processed_exists=processed_exists)

@app.route('/download/<filename>')
def download(filename):
    pdf_name = os.path.splitext(filename)[0] + '.pdf'
    return send_from_directory('output/pdf', pdf_name, as_attachment=True)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
