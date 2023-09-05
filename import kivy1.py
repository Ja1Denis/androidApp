import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv = """
GridLayout:
    cols: 2
    
    Label:
        text: "Potrošnja goriva (l/100km):"
        
    TextInput:
        id: potrosnja
        text: "7.4"
        
    Label: 
        text: "Udaljenost (km):"
        
    TextInput:
        id: udaljenost
        text: "350"
        
    Label:
        text: "Cijena goriva (EUR/l):"
        
    TextInput:
        id: cijena
        text: "1.5"
        
    Button:
        text: "Izračunaj"
        on_press: app.izracunaj()
        
    Label:
        id: rezultat
        text: "-"
"""

class KalkulatorGorivaApp(App):
    def build(self):
        return Builder.load_string(kv)

    def izracunaj(self):
        potrosnja = float(self.root.ids.potrosnja.text)
        udaljenost = float(self.root.ids.udaljenost.text)
        cijena = float(self.root.ids.cijena.text)

        ukupno = (potrosnja * udaljenost) / 100 * cijena

        self.root.ids.rezultat.text = str(ukupno) + " EUR"

if __name__ == "__main__":
    KalkulatorGorivaApp().run()