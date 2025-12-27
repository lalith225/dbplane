from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TripSplitter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.num_input = TextInput(hint_text="Enter total number of people", input_filter='int')
        self.add_widget(self.num_input)

        self.name_input = TextInput(hint_text="Enter names separated by commas")
        self.add_widget(self.name_input)

        self.info_label = Label(text="Enter trip details below")
        self.add_widget(self.info_label)

        self.expenses_input = TextInput(hint_text="Example: Arul,200,breakfast\nManish,1200,lunch\nMohan,300,dinner", multiline=True)
        self.add_widget(self.expenses_input)

        self.calc_button = Button(text="Calculate Split")
        self.calc_button.bind(on_press=self.calculate)
        self.add_widget(self.calc_button)

        self.result_label = Label(text="", halign="left", valign="top")
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            num_people = int(self.num_input.text.strip())
            names = [n.strip() for n in self.name_input.text.split(",") if n.strip()]
            lines = self.expenses_input.text.strip().splitlines()

            expenses = {n: 0.0 for n in names}
            for line in lines:
                p, amt, *rest = line.split(",")
                expenses[p.strip()] += float(amt.strip())

            total = sum(expenses.values())
            share = total / num_people
            balances = {n: round(expenses[n] - share, 2) for n in names}

            result = [f"Total: ₹{total:.2f}", f"Each Share: ₹{share:.2f}\n"]
            for name, bal in balances.items():
                if bal > 0:
                    result.append(f"{name} should RECEIVE ₹{bal:.2f}")
                elif bal < 0:
                    result.append(f"{name} should PAY ₹{-bal:.2f}")
                else:
                    result.append(f"{name} is settled up")

            self.result_label.text = "\n".join(result)
        except Exception as e:
            self.result_label.text = f"Error: {e}"

class TripSplitterApp(App):
    def build(self):
        return TripSplitter()

if __name__ == '__main__':
    TripSplitterApp().run()
