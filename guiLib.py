from typing import Text
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from numpy import source
import converter 

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
            size_hint=(0.2, 0.2)
        )
        self.window.add_widget(l1)

        l2 = Label(
            text = "Amount in desired currency",
            size_hint=(0.2, 0.2)
        )
        self.window.add_widget(l2)


        #input box
        self.input = TextInput(multiline = False,size_hint=(0.2, 0.1)) 
        self.window.add_widget(self.input)

        #output box
        self.output = TextInput(multiline = False,size_hint=(0.2, 0.1)) 
        self.window.add_widget(self.output)


        self.curr = converter.getCurrencies()

        self.dropdown1 = DropDown()
        self.mainbutton1 = Button(text='from', size_hint=(0.1, 0.1))
        self.mainbutton1.bind(on_release=self.dropdown1.open)
        for key,value in self.curr.items():

            btn1 = Button(text= key, size_hint_y=None, height=35)

            btn1.bind(on_release=lambda btn: self.dropdown1.select(btn.text))
    
            self.dropdown1.add_widget(btn1)

            self.dropdown1.bind(on_select=lambda instance, x: setattr(self.mainbutton1, 'text', x))


        self.window.add_widget(self.mainbutton1)
        


        self.dropdown2 = DropDown()
        self.mainbutton2 = Button(text='to', size_hint=(0.1, 0.1))
        self.mainbutton2.bind(on_release=self.dropdown2.open)
        for key,value in self.curr.items():

            btn2 = Button(text= key, size_hint_y=None, height=35)

            btn2.bind(on_release=lambda btn: self.dropdown2.select(btn.text))
    
            self.dropdown2.add_widget(btn2)

            self.dropdown2.bind(on_select=lambda instance, x: setattr(self.mainbutton2, 'text', x))


        self.window.add_widget(self.mainbutton2)


        convert = Button(
            text = "Convert",
            size_hint = (0.2,0.2)
        )
        convert.bind(on_press = self.press)
        self.main.add_widget(self.window)


        self.main.add_widget(convert)  

        return self.main

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Hello " + self.user.text + "!"

    def press(self, instance):
        #print(self.curr[self.mainbutton1.text])
        self.output.text = str(float((float(self.input.text) * float(self.curr[self.mainbutton2.text])) / float(self.curr[self.mainbutton1.text])))  


if __name__ == "__main__":
    CurrentCurrencyConverter().run()