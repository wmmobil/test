from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
layour = GridLayout(cols=3)
ab = "введите а"
class MainApp(App):
    def build(self):
        self.wt = TextInput(text=f"{ab}")
        self.ht = TextInput(text="Введите b")
        self.c = TextInput(text="Введите c")
        sm = Button(text="Подтвеодить",on_press=self.submit)
        layour.add_widget( self.wt)
        layour.add_widget(self.ht)
        layour.add_widget(self.c)
        layour.add_widget(sm)
        print(ab)
        return layour
    def submit(self,instance):
        global ab
        global layour
        a = self.wt.text
        b = self.ht.text
        c = self.c.text
        print("a:"+ a)
        print("b:" + b)
        print("c:" + c)
        try:
            a_a = int(a)
            b_b = int(b)
            c_c = int(c)
            d_d = b_b * b_b - 4 * a_a * c_c
            d_sqr = d_d ** (0.5)
            if d_d > 0:
                x_one = -b_b - d_d ** (0.5)
                x_one_x = x_one / 2
                x_two = -b_b + d_d ** (0.5)
                x_two_x = x_two / 2
                instance.text = f"Дискриминант:{d_d}\nКорень из дискриминанта{d_sqr}\n1 корень:{x_one_x}\n2Корень{x_two_x}"
            elif d_d == 0:
                x_one = -b_b - d_d ** (0.5)
                x_one_x = x_one / 2
                instance.text = f"Дискриминант:{d_d}\nКорень из дискриминанта{d_sqr}\nкорень:{x_one_x}"
            else:
                instance.text = f"Дискриминат:{d_d}\nДискриминант отрицательный"
        except:
            instance.text = "Вы Ввели неправельное значение"



if __name__=="__main__":
    MainApp().run()
