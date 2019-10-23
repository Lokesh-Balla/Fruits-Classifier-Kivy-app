import sqlite3

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from predict import getData

fruit = ""

Builder.load_string('''
<CameraClick>:
    orientation: 'horizontal'
    BoxLayout:
        orientation: 'vertical'
        Camera:
            id: camera
            resolution: (640, 480)
            play: True
        Button:
            text: 'Get Info'
            size_hint_y: None
            on_press: root.capture()
            height: '48dp'
    BoxLayout:
        orientation: 'vertical'
        RecycleView:
            data: [{'text':"name:{}".format(name)} for name,calories,total_fat,cholesterol,carbohydrate,protein in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        RecycleView:
            data: [{'text':"calories:{}".format(calories)} for name,calories,total_fat,cholesterol,carbohydrate,protein in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        RecycleView:
            data: [{'text':"Total Fat:{}".format(total_fat)} for name,calories,total_fat,cholesterol,carbohydrate,protein in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        RecycleView:
            data: [{'text':"cholesterol:{}".format(cholesterol)} for name,calories,total_fat,cholesterol,carbohydrate,protein in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        RecycleView:
            data: [{'text':"carbohydrate:{}".format(carbohydrate)} for name,calories,total_fat,cholesterol,carbohydrate,protein in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        RecycleView:
            data: [{'text':"protein:{}".format(protein)} for name,calories,total_fat,cholesterol,carbohydrate,protein in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
''')


class CameraClick(BoxLayout):
    rows = ListProperty([("name", "calories", "total_fat", "cholesterol", "carbohydrate", "protein")])

    def get_data(self):
        conn = sqlite3.connect("fruits_data.db")
        c = conn.cursor()
        t = [fruit, ]
        c.execute("SELECT * FROM fruits where name=?", t)
        self.rows = c.fetchall()
        print(self.rows)

    def capture(self):
        global fruit
        print(list(self.ids))
        camera = self.ids['camera']
        camera.export_to_png("img.png")
        fruit = getData()
        self.get_data()


class Camera(App):
    def build(self):
        return CameraClick()


if __name__ == "__main__":
    # conn = sqlite3.connect("fruits_data.db")
    # c = conn.cursor()
    # c.execute("create table fruits(name varchar2(100),calories int,total_fat int,cholesterol int,carbohydrate int,protein int)")

    # values = [
    #     ('apple', 52, 0.2, 0, 14, 0.3),
    #     ('orange', 47, 0.1, 0, 12, 0.9),
    #     ('grapes', 67, 0.4, 0, 17, 0.6),
    # ]
    # c.executemany('INSERT INTO fruits VALUES (?,?,?,?,?,?)', values)
    # conn.commit()

    # c.execute('SELECT * FROM fruits')
    # print(c.fetchall())
    Camera().run()
