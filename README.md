# Dot-to-Dot Image Processor (Flask Web UI Fork)

This is a modernized fork of the original dot-to-dot image processing project. It provides a simple, responsive web interface for generating dot-to-dot puzzles from images, powered by Flask and Bootstrap 5.

## Features
- **Web-based UI**: Upload an image, preview it, and generate a dot-to-dot puzzle directly in your browser.
- **Responsive Design**: Works seamlessly on laptops, tablets, and mobile devices.
- **Side-by-side Preview**: See the original and processed images in matching, autoscaled tiles.
- **Progress Feedback**: Watch processing progress in real time.
- **Easy Download**: Download the result as a PDF with a single click.
- **No extra controls**: The UI is intentionally minimal and user-friendly.

## Usage
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app**:
   ```bash
   python app.py
   ```
3. **Open your browser** and go to [http://localhost:5000](http://localhost:5000)
4. **Upload an image** (JPG or PNG), click "Generate", and download your dot-to-dot PDF.

## Project Structure
- `app.py` — Flask backend and processing logic
- `templates/` — Bootstrap 5 HTML templates for the web UI
- `DotToDot.py` and related files — Image processing backend
- `output/` — Generated results (JPG and PDF)
- `input/` — Uploaded images

## About This Fork
This repository is a fork of the original dot-to-dot image processor, with the following improvements:
- Modern Python 3 compatibility
- Flask web backend
- Bootstrap 5 adaptive UI
- Streamlined, user-focused workflow

Original project: [link to original repo if available]

## License
See `LICENSE` for details.
