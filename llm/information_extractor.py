from llm.groq_client import client


def extract_information(ocr_text):

    prompt = f"""
You are an intelligent OCR assistant.

Tasks:

1. Correct OCR mistakes.

2. Classify document into one category:
Invoice
Receipt
Resume
Aadhaar Card
PAN Card
Driving License
Passport
Bank Statement
Other

3. Extract information.

Return ONLY valid JSON.

Format:

{{
"document_type":"",
"confidence":"",
"document_title":"",
"name":"",
"date":"",
"invoice_number":"",
"total_amount":"",
"address":"",
"phone_number":"",
"email":"",
"pan_number":"",
"aadhaar_number":"",
"other_fields":{{}}
}}

OCR Text:

{ocr_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content