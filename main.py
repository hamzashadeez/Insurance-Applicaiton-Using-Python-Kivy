from kivy.config import Config
Config.set('graphics', 'width', '350')
from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivymd.toast.kivytoast import toast
import time, re
from kivymd.list import ThreeLineListItem
from datetime import date


class Insurance(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):
        return Builder.load_file('main.kv')
        
    def on_start(self):
        self.add()
        pass
    
    def apply(self):
        pass
    def active(self, type):
        with open('files/type.txt', 'w') as f:
            f.write(type)
    def changeScreen(self, name):
        screen = self.root.ids.manager
        screen.current = name
    def apply(self):
        with open('files/type.txt', 'r') as f:
            text = f.read()
        
        if text == 'life':
            self.changeScreen(text)
        elif text == 'property':
            self.changeScreen(text)
        elif text == 'car':
            self.changeScreen(text)
        elif text == 'medical':
            self.changeScreen(text)
        else:
            pass
        
    def p(self, tt):
        t = time.localtime()
        c = time.strftime('%H:%M', t)
        d = date.today()
        w = str(c) +" "+ str(d)
        with open('t.txt', 'a') as f:
            f.write(str(tt)+"~"+str(w)+ '~'+"Complete Application"+str('\n'))
        
    
        
    def add(self):
        mylist = self.root.ids.liste 
        with open('t.txt','r') as f:
            li = f.readlines()
        arr = []
        for i in li:
            arr.append(re.split('~', i)) 
        s = '                          '
        for i in arr:
            item = ThreeLineListItem(text = i[0], secondary_text = i[1]+s+i[2])
            mylist.add_widget(item)
    
    def pay(self):
        toast('This feature is among the project\'s limitations')   
    
    def render(self):
        mylist = self.root.ids.liste 
        mylist.clear_widgets()
        self.add()
        
        
    def applyIn(self, type, a,b):
        if a.text == '' and b.text == 0:
            toast('please fill the form Completely')
        else:
            self.p(type)
            toast('Done')
        self.render()
        
Insurance().run()