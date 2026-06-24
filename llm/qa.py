from llm.groq_client import client


def ask_question(document_text, question):

    prompt = f"""
Use only the document text.

Document:

{document_text}

Question:

{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content