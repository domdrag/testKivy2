import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label

import os
import requests
import pdfplumber
import re

def download_file(url):
    local_filename = url.split('/')[-1]
    
    with requests.get(url) as r:
        assert r.status_code == 200, f'error, status code is {r.status_code}'
        with open(local_filename, 'wb') as f:
            f.write(r.content)
        
    return local_filename

invoice = 'https://github.com/domdrag/Python/raw/main/test.pdf'
invoice_pdf = download_file(invoice)

pdf = pdfplumber.open(invoice_pdf)
page = pdf.pages[0]
text = page.extract_text()
print(text)

class DataTableApp(App):
    def build(self):
        return Label(text = text)

if __name__=='__main__':
    DataTableApp().run()
