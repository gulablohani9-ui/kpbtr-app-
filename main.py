from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import os

class KPBTRApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # Title
        self.add_widget(Label(text="KP BTR Astrology App", font_size='22sp', size_hint_y=0.1))

        # Inputs
        self.add_widget(Label(text="Enter Birth Date (DD/MM/YYYY):"))
        self.dob_input = TextInput(text="30/06/1983", multiline=False, size_hint_y=0.1)
        self.add_widget(self.dob_input)

        self.add_widget(Label(text="Enter Birth Time (HH:MM:SS):"))
        self.tob_input = TextInput(text="01:16:00", multiline=False, size_hint_y=0.1)
        self.add_widget(self.tob_input)

        # Button
        btn_calc = Button(text="Calculate BTR", size_hint_y=0.15, background_color=(0.2, 0.6, 1, 1))
        btn_calc.bind(on_press=self.calculate)
        self.add_widget(btn_calc)

        # Result Label
        self.result_label = Label(text="Status: Ready for calculation", size_hint_y=0.4, halign="center")
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            date_val = self.dob_input.text
            time_val = self.tob_input.text
            
            # Check if ephe folder exists in app storage
            ephe_path = os.path.join(os.path.dirname(__file__), 'ephe')
            ephe_status = "Ephe folder found!" if os.path.exists(ephe_path) else "Ephe folder missing!"
            
            self.result_label.text = f"Calculated Successfully!\nDOB: {date_val}\nTOB: {time_val}\n{ephe_status}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

class KPApp(App):
    def build(self):
        return KPBTRApp()

if __name__ == '__main__':
    KPApp().run()
