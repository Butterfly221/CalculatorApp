import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW



class Calculator(toga.App):
    def button_press(self, button):
        def on_press(button):
            res_text = self.res_label.text
            if button.text == "=":
                if self.command == "%":
                    self.res_label.text = float(self.first_value) % float(res_text) if res_text != "" else ""
                elif self.command == "/":
                    self.res_label.text = float(self.first_value) / float(res_text) if res_text != "" else ""
                elif self.command == "x":
                    self.res_label.text = float(self.first_value) * float(res_text) if res_text != "" else ""
                elif self.command == "-":
                    self.res_label.text = float(self.first_value) - float(res_text) if res_text != "" else ""
                elif self.command == "+":
                    self.res_label.text = float(self.first_value) + float(res_text) if res_text != "" else ""
                else:
                    self.res_label.text = ""   
                self.command = ""
            elif button.text == "%":
                self.res_label.text = ""
                self.command = "%"
                self.first_value = res_text
            elif button.text == "C":
                self.res_label.text = ""
            elif button.text == "/":
                self.res_label.text = ""
                self.command = "/"
                self.first_value = res_text
            elif button.text == "x":
                self.res_label.text = ""
                self.command = "x"
                self.first_value = res_text
            elif button.text == "-":
                self.res_label.text = ""
                self.command = "-"
                self.first_value = res_text
            elif button.text == "+":
                self.res_label.text = ""
                self.command = "+"
                self.first_value = res_text
            elif button.text == "del":
                self.res_label.text = res_text[:-1] if res_text != "" else ""
            else:
                self.res_label.text = res_text + button.text if res_text != "0" else button.text
        return on_press
    def startup(self):
        self.command = ""
        self.first_value = ""
        self.size_x = 300
        self.size_y = 600
        buttons_box = toga.Box(style=Pack(direction=COLUMN))
        button_styles = Pack(width=60, height=60, font_size=20)
        buttons_row = []
        buttons_row.append(["C", "%", "del", "/"])
        buttons_row.append(["7", "8", "9", "x"])
        buttons_row.append(["4", "5", "6", "-"])
        buttons_row.append(["1", "2", "3", "+"])
        buttons_row.append(["0", "00", "000", "="])

        self.res_label = toga.Label(text="", style=Pack(background_color="GRAY", text_align="center", font_size=20))
        result_box = toga.Box(style=Pack(width=self.size_x, height=100, background_color="GRAY", direction="row", alignment="center"))
        result_box.add(self.res_label)

        for it in buttons_row:
            buttons_box.add(toga.Box(children=[toga.Button(str(i), on_press=self.button_press(str(i)), style=button_styles) for i in it], style=Pack(direction=ROW)))


        main_box = toga.Box(
            children=[
                result_box,
                buttons_box
            ],
            style=Pack(direction="column")
        )

        self.main_window = toga.MainWindow(title="Calculator", size=(self.size_x, self.size_y))
        self.main_window.content = main_box
        self.main_window.show()
        
def main():
    return Calculator("Calculator", "org.calculator")
if __name__ == "__main__":
    main().main_loop()