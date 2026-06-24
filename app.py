import os
os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"

import streamlit as st
import json
from PIL import Image

from ocr.preprocess import preprocess_image
from ocr.extractor import extract_text

from llm.information_extractor import (
    extract_information
)

from llm.qa import ask_question

from validation.validator import validate_data

from utils.json_parser import parse_json

st.set_page_config(
    page_title="Intelligent OCR System",
    layout="wide"
)

st.title("📄 Intelligent OCR using OCR + LLM")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file:

    if uploaded_file.name.lower().endswith(".pdf"):
        import fitz
        import io
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        page = doc.load_page(0)
        pix = page.get_pixmap(dpi=150)
        image = Image.open(io.BytesIO(pix.tobytes("png")))
    else:
        image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image)

    processed = preprocess_image(image)

    with col2:
        st.subheader("Processed Image")
        st.image(processed)
        st.write(f"Processed image shape: {processed.shape}")
        print(f"DEBUG: processed shape: {processed.shape}", flush=True)

    if st.button("Run OCR"):

        with st.spinner("Running OCR..."):
            print(f"DEBUG: Passing to extract_text: shape={processed.shape}", flush=True)
            ocr_text = extract_text(processed)

        st.subheader("OCR Text")

        st.text_area(
            "",
            ocr_text,
            height=250
        )

        with st.spinner("Running LLM..."):

            llm_output = extract_information(
                ocr_text
            )

        st.subheader("LLM Output")

        st.code(llm_output)

        extracted_json = parse_json(
            llm_output
        )

        st.subheader("Structured JSON")

        st.json(extracted_json)

        validations = validate_data(
            extracted_json
        )

        st.subheader("Validation Results")

        st.json(validations)

        st.download_button(
            "Download JSON",
            json.dumps(
                extracted_json,
                indent=4
            ),
            file_name="output.json"
        )

        st.subheader("Ask Questions")

        question = st.text_input(
            "Enter your question"
        )

        if question:

            answer = ask_question(
                ocr_text,
                question
            )

            st.success(answer)