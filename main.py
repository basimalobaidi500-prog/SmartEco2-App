from kivy.lang import Builder
from kivymd.app import MDApp
import requests

KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDLabel:
            text: "🌱 EcoTrack AI"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: electricity
            hint_text: "Electricity (kWh)"
            input_filter: "float"

        MDTextField:
            id: water
            hint_text: "Water (liters)"
            input_filter: "float"

        MDTextField:
            id: fuel
            hint_text: "Fuel (liters)"
            input_filter: "float"

        MDRaisedButton:
            text: "Analyze"
            on_release: app.send_data()

        MDLabel:
            id: result
            text: ""
            halign: "center"
'''

# ⚠️ مهم: مؤقتاً بدون API (محلي)
class EcoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def send_data(self):
        elec = float(self.root.ids.electricity.text or 0)
        water = float(self.root.ids.water.text or 0)
        fuel = float(self.root.ids.fuel.text or 0)

        carbon = (elec * 0.5) + (water * 0.001) + (fuel * 2.3)

        if fuel > 5:
            advice = "🚗 قلل استخدام السيارة"
        elif elec > 50:
            advice = "💡 استخدم أجهزة موفرة للطاقة"
        else:
            advice = "🌿 عمل رائع!"

        self.root.ids.result.text = f"CO2: {carbon:.2f}\n{advice}"

EcoApp().run()
