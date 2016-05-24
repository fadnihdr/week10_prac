from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.item_list = ['one', 'two', 'three', 'ten']
        print(self.item_list)
        print(self.item_list.__len__())
        self.number_of_items = self.item_list.__len__()
        self.title = "My App"
        self.root = Builder.load_file('app.kv')
        self.create_item_buttons()
        return self.root

    def create_item_buttons(self):
        print("*****", self.item_list)
        for item in self.item_list:
            print(item)
            temp_button = Button(text=item)
            temp_button.bind(on_release=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)

    def press_item(self, instance):
        print("button pressed..", instance.text)

MyApp().run()