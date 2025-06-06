# -*- coding: utf-8 -*-
"""resume_parser.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WuSQab3rcWgOvnG8hb0vKfPoA--GdTEo
"""

import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text