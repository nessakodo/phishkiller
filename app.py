from flask import Flask, render_template, request
from analyzer import analyze_url, analyze_header_text
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

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

            if filename.endswith(('.png', '.jpg', '.jpeg')):
                image = Image.open(io.BytesIO(header_file.read()))
                header_text = pytesseract.image_to_string(image)
            else:
                header_text = header_file.read().decode('utf-8')

            results = analyze_header_text(header_text)
            header_analysis = results

    return render_template('index.html', url_analysis=url_analysis, header_analysis=header_analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
