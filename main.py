import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
import urllib3
import pdfplumber
import io

def extract_text_from_pdf_by_url(url):
    all_text = ''

    http = urllib3.PoolManager()
    temp = io.BytesIO()
    temp.write(http.request("GET", url).data)
    try:    # to verify is the url has valid pdf file!
        pdf = pdfplumber.open(temp)
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            # TypeError: can only concatenate str (not "NoneType") to str
            if single_page_text is not None: 
                all_text += '\n' + single_page_text
        pdf.close()
    except:
        pass
    return all_text


url  = 'https://github.com/domdrag/Python/raw/main/test.pdf'
text = extract_text_from_pdf_by_url(url)
print(text)

class DataTableApp(App):
    def build(self):
        return Label(text = text)

if __name__=='__main__':
    DataTableApp().run()
