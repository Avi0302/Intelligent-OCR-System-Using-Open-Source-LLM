# 📄 Intelligent OCR System Using Open-Source LLM

An advanced document processing and analysis application that combines deep learning OCR (**PaddleOCR**) and LLMs (**Llama 3.1** via Groq) to preprocess documents, extract text, categorize them, pull structured fields into valid JSON, validate metadata, and support interactive question-answering.

---

## 🚀 Key Features

*   **Multi-Format Upload**: Upload images (`.png`, `.jpg`, `.jpeg`) or document files (`.pdf`).
*   **Intelligent Image Preprocessing**: Converts inputs to grayscale, applies fast non-local means denoising, and runs Otsu's thresholding before mapping back to 3-channel format to maximize OCR accuracy.
*   **High-Performance OCR**: Extracts text from preprocessed images using the robust PaddleOCR engine.
*   **AI-Powered Information Extraction**: Uses the open-source **Llama-3.1-8b-instant** model via Groq to correct OCR errors, classify the document, and extract metadata fields into a structured JSON payload.
*   **Regex Validation Suite**: Automatically validates common parsed document fields (Email, Phone Numbers, PAN Number, Aadhaar Number).
*   **Interactive Document Q&A**: Enter custom questions about the uploaded document and receive answers based solely on the extracted text.
*   **Downloadable Outputs**: Export the final structured JSON metadata with a single click.

---

## 🛠️ Technology Stack

*   **Frontend**: Streamlit
*   **OCR**: PaddleOCR (PaddlePaddle)
*   **LLM API**: Groq Cloud SDK (Llama 3.1 8B)
*   **PDF Parsing**: PyMuPDF (fitz)
*   **Image Processing**: OpenCV & Pillow

---

## 📁 Directory Structure

```text
Intelligent OCR System/
├── llm/
│   ├── groq_client.py           # Configures and instantiates the Groq client
│   ├── information_extractor.py # AI prompt for document classification & field extraction
│   └── qa.py                    # AI prompt for interactive Q&A
├── ocr/
│   ├── extractor.py             # Configures PaddleOCR and handles text extraction
│   └── preprocess.py            # OpenCV image preprocessing pipeline
├── utils/
│   └── json_parser.py           # Standardizes LLM outputs to clean JSON
├── validation/
│   └── validator.py             # Validation regex rules for phone, email, Aadhaar, PAN
├── app.py                       # Main Streamlit web application
├── requirements.txt             # Python dependencies
└── .env                         # Local environment configuration file
```

---

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Avi0302/Intelligent-OCR-System-Using-Open-Source-LLM.git
cd Intelligent-OCR-System-Using-Open-Source-LLM
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a file named `.env` in the root directory and add your Groq API Key:
```env
GROQ_API_KEY=your_groq_api_key_here
```
> [!NOTE]
> You can acquire a free API key from the [GroqCloud Console](https://console.groq.com/).

### 5. Launch the Application
```bash
streamlit run app.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser to view the application.

---

## 💡 How It Works

1. **Upload**: Drag and drop any image or PDF. If it's a PDF, PyMuPDF renders the first page as an image.
2. **Preprocess**: The image undergoes grayscale conversion, denoising, and adaptive thresholding to produce a clean, binary representation.
3. **Extract (OCR)**: PaddleOCR detects and recognizes text characters from the processed image.
4. **Structured Parsing**: The raw text is passed to Llama 3.1. It repairs character misreadings and formats the data into JSON matching a pre-defined schema.
5. **Validate**: The parsed fields are checked against regex patterns to identify errors or mismatched documents.
6. **Query**: Ask any query, and the LLM will find answers based strictly on the document text.
