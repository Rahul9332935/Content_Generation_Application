from flask import Flask, jsonify, request,render_template
from openai_integration import analyze_sentiment, generate_text, summarize_documents
import PyPDF2
from PyPDF2 import PdfReader


app = Flask(__name__)

@app.route('/pdfhtml')
def pdfhtml():
  return render_template('pdftotext.html')
  
@app.route('/sentiment')
def sentiment():
  return render_template('sen.html')

@app.route('/bot')
def bot():
  return render_template('bot.html')
  
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_summarize():
  if 'pdf_file' not in request.files:
    return "No file uploaded", 400

  pdf_file = request.files['pdf_file']

  if pdf_file.filename == '':
    return "No file selected", 400

  if pdf_file:
    pdf_text = convert_pdf_to_text(pdf_file)
    print(pdf_text)
    summary = summarize_documents([pdf_text])
    return jsonify(summary)

def convert_pdf_to_text(pdf_file):
  pdf_text = ""
  pdf_reader = PdfReader(pdf_file)
  for page in pdf_reader.pages:
    pdf_text += page.extract_text()
  return pdf_text

@app.route('/generate-text', methods=['POST'])
def generate_text_route():
    data = request.json
    response = generate_text(data['prompt'], data['context'])
    return jsonify({'response': response})


@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment_route():
    data = request.json
    sentiment = analyze_sentiment(data['text'])
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
