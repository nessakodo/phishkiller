from flask import Flask, render_template, request, flash
from analyzer import analyze_url, analyze_header_text
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import io

# Check if running locally on Mac
if os.getenv('RUNNING_IN_DOCKER') != '1':
    # Only set this if running locally (Mac Homebrew install)
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

@app.route('/', methods=['GET', 'POST'])
def home():
    url_analysis = None
    header_analysis = None

    if request.method == 'POST':
        if 'url' in request.form and request.form['url']:
            url = request.form['url']
            risk, reasons = analyze_url(url)
            url_analysis = {
                'url': url,
                'risk': risk,
                'reasons': reasons
            }

        if 'header' in request.files and request.files['header']:
            header_file = request.files['header']
            filename = header_file.filename.lower()

            header_text = ""
            ocr_error = None

            if filename.endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Open image safely
                    image = Image.open(io.BytesIO(header_file.read()))
                    
                    # Standardize to RGB
                    image = image.convert('RGB')
                    
                    # Convert to Grayscale
                    image = image.convert('L')
                    
                    # Enhance Contrast
                    enhancer = ImageEnhance.Contrast(image)
                    image = enhancer.enhance(2.0)  # 2x contrast
                    
                    # Slightly sharpen
                    image = image.filter(ImageFilter.SHARPEN)

                    # Run OCR
                    header_text = pytesseract.image_to_string(image)

                except Exception as e:
                    ocr_error = f"OCR failed: {str(e)}. Please upload a .txt file instead."
            else:
                try:
                    header_text = header_file.read().decode('utf-8')
                except Exception as e:
                    ocr_error = f"Failed to read file: {str(e)}"

            if header_text.strip():
                results = analyze_header_text(header_text)
            else:
                results = {
                    'ips': [],
                    'spf_dmarc_failures': []
                }

            results['filename'] = filename
            if ocr_error:
                results['ocr_error'] = ocr_error

            header_analysis = results

    return render_template('index.html', url_analysis=url_analysis, header_analysis=header_analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
