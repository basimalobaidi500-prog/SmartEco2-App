from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

KV = '''
MDScreen:

    md_bg_color: 0.07, 0.12, 0.2, 1  # Dark blue

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDLabel:
            text: "Hi, User 👋"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        # ===== Cards =====

        MDGridLayout:
            cols: 1
            spacing: 15

            MDCard:
                radius: [20]
                elevation: 8
                md_bg_color: 0.1,0.2,0.35,1
                padding: 15

                MDBoxLayout:
                    orientation: "vertical"

                    MDLabel:
                        text: "⚡ Energy"
                        theme_text_color: "Custom"
                        text_color: 1,1,1,1

                    MDProgressBar:
                        value: 67

                    MDLabel:
                        text: "560 kWh"
                        halign: "right"
                        theme_text_color: "Custom"
                        text_color: 0.6,1,0.8,1

            MDCard:
                radius: [20]
                elevation: 8
                md_bg_color: 0.1,0.2,0.35,1
                padding: 15

                MDBoxLayout:
                    orientation: "vertical"

                    MDLabel:
                        text: "💧 Water"
                        theme_text_color: "Custom"
                        text_color: 1,1,1,1

                    MDProgressBar:
                        value: 38

                    MDLabel:
                        text: "119 gal"
                        halign: "right"
                        text_color: 0.6,1,0.8,1

            MDCard:
                radius: [20]
                elevation: 8
                md_bg_color: 0.1,0.2,0.35,1
                padding: 15

                MDBoxLayout:
                    orientation: "vertical"

                    MDLabel:
                        text: "⛽ Fuel"
                        text_color: 1,1,1,1

                    MDProgressBar:
                        value: 50

                    MDLabel:
                        text: "178 L"
                        halign: "right"
                        text_color: 0.6,1,0.8,1

        MDRaisedButton:
            text: "Analyze"
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.2,0.8,0.6,1
'''

class EcoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

EcoApp().run()
