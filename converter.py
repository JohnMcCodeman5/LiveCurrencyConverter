import kivy
kivy.require('1.0.7')
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from matplotlib.pyplot import title
from numpy import source
import converterLib 


class PopErr(FloatLayout):
    pass


class CurrentCurrencyConverter(App):
  
    def build(self):
       
        self.main = GridLayout()
        self.main.cols = 1

        self.window = GridLayout()
        self.window.rows = 4
        self.window.cols = 2
        #self.window.add_widget(Image(source = "background.jpg"))

        #self.user = TextInput(multiline = False)
        #self.window.add_widget(self.user)

        #labels
        l1 = Label(
            text = "Amount in input currency",
            size_hint=(0.02, 0.02),
            color=(1,1,0.1,1),
            font_size = "20sp"       
        )
        self.window.add_widget(l1)

        l2 = Label(
            text = "Amount in desired currency",
            size_hint=(0.02, 0.02),
            color=(0,1,0,1),
            font_size = "20sp"
        )
        self.window.add_widget(l2)


        #input box
        self.input = TextInput(multiline = False,size_hint=(0.1, 0.05), font_size = "40sp") 
        self.window.add_widget(self.input)

        #output box
        self.output = TextInput(multiline = False,size_hint=(0.1, 0.05), font_size = "40sp") 
        self.window.add_widget(self.output)


        self.curr = converterLib.getCurrencies()

        self.dropdown1 = DropDown()
        self.mainbutton1 = Button(text='from', size_hint=(0.032, 0.032), font_size = "20sp")
        self.mainbutton1.bind(on_release=self.dropdown1.open)
        for key,value in self.curr.items():

            btn1 = Button(text= key, size_hint_y=None, height=45)

            btn1.bind(on_release=lambda btn: self.dropdown1.select(btn.text))
    
            self.dropdown1.add_widget(btn1)

            self.dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton1, 'text', x))


        self.window.add_widget(self.mainbutton1)
        


        self.dropdown2 = DropDown()
        self.mainbutton2 = Button(text='to', size_hint=(0.032, 0.032), font_size = "20sp")
        self.mainbutton2.bind(on_release=self.dropdown2.open)
        for key,value in self.curr.items():

            btn2 = Button(text= key, size_hint_y=None, height=45)

            btn2.bind(on_release=lambda btn: self.dropdown2.select(btn.text))
    
            self.dropdown2.add_widget(btn2)

            self.dropdown2.bind(on_select=lambda instance, x: setattr(self.mainbutton2, 'text', x))


        self.window.add_widget(self.mainbutton2)


        convert = Button(
            text = "Convert",
            size_hint = (0.2,0.2),
            font_size = "23sp"
        )
        convert.bind(on_press = self.press)
        self.main.add_widget(self.window)


        self.main.add_widget(convert)  

        return self.main


    def press(self, instance):
        if self.mainbutton1.text == "from" or self.mainbutton2.text == "to" or self.input.text == "":
            show1 = PopErr()
            self.popup = Popup(title = "Error!", content = show1, size_hint=(None, None), size = (400,400))
            #self.popup = Popup(title = "Error!", size_hint=(None, None), size = (300,300))
            self.popup.open()   

        else:
            #print(self.curr[self.mainbutton1.text])
            self.output.text = str(float((float(self.input.text) * float(self.curr[self.mainbutton2.text])) / float(self.curr[self.mainbutton1.text])))  


if __name__ == "__main__":
    CurrentCurrencyConverter().run()