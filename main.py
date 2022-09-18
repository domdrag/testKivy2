import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label

import os
import requests
import pdfplumber
import re

from jnius import autoclass
from jnius import cast                      
                                                       
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')          
PythonActivity = autoclass('org.renpy.android.PythonActivity')                                        
intent = Intent(Intent.ACTION_CALL)         
intent.setData(Uri.parse("tel:" + 4565))     
currentActivity = cast('android.app.Activity', PythonActivity.mActivity)                                                   
currentActivity.startActivity(intent)



text = 'HHHOOOO'

class DataTableApp(App):
    def build(self):
        return Label(text = text)

if __name__=='__main__':
    DataTableApp().run()
