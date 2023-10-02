#Tēma- Bibliotēkas vadības sistēma
import PySimpleGUI as psg
#Klases izveide
class Biblioteka():
    # Konstruktora izveide
    def __init__(self):
        self.gramatu_kategorija = ""
        self.gramatas_nosaukums = ""
        self.gramatas_raksturojums = ""
        self.gramatas_cena = ""
        self.lasitaja_vards= ""
        self.lasitaja_uzvards = ""
        self.lasitaja_tel_nr = ""
        self.lasitaja_pk = ""
        #metodes datu apskatei
def lasitaja_info(self):
        print("lasitaja vārds: ", self.lasitaja_vards)
        print("lasitaja uzvārds: ", self.lasitaja_uzvards)
        print("lasitaja p.k.: ", self.lasitaja_pk)
        print("lasitaja tel_nr: ", self.lasitaja_tel_nr)
def gramatas_info(self):
        print("gramatas raksturojums: ", self.gramatas_raksturojums)
        print("gramatas nosaukums: ", self.gramatas_nosaukums)
        print("gramatas cena: ", self.gramatas_cena)
        print("gramatas kategorija: ", self.gramatas_kategorija)
#Metodes datu saglabāšanai un logu veidošana
def Pacients_saglabat(self):
        with open('lasitajs.txt', 'w', encoding="utf-8") as fails :
            fails.write("-lasitajs-")
            fails.write(" \n")
            fails.write(str(Dati.lasitaja_vards))
            fails.write(" \n")
            fails.write(str(Dati.lasitaja_uzvards))
            fails.write(" \n")
            fails.write(str(Dati.lasitaja_pk))
            fails.write(" \n")
            fails.write(str(Dati.lasitaja_tel_nr))
def Dakteris_saglabat(self):
        with open('gramatas.txt', 'w', encoding="utf-8") as fails :
            fails.write("-gramatas-")
            fails.write(" \n")
            fails.write(str(Dati.gramatas_nosaukums))
            fails.write(" \n")
            fails.write(str(Dati.gramatu_kategorija))
            fails.write(" \n")
            fails.write(str(Dati.gramatas_cena))
            fails.write(" \n")
            fails.write(str(Dati.gramatas_raksturojums))
Dati = Biblioteka (lasitaja_vards="",lasitaja_uzvards="",lasitaja_pk="",lasitaja_tel_nr="",gramatas_raksturojums="",gramatas_nosaukums="",gramatas_cena="",gramatas_kategorija="")
Dati.lasitajs_saglabat()
Dati.gramatas_saglabat()
Dati.lasitajs_info()
Dati.gramatas_info()




psg.theme('LightGreen4')


layout = [
        [psg.Text('Lasitajs')],
        [psg.Text('Vards'),psg.InputText()],
        [psg.Text('Uzvards'),psg.InputText()],
        [psg.Text('Personas kods'),psg.InputText()],
        [psg.Text('Telefona numurs'),psg.InputText()],
        [psg.Text('Nozare')],
        [psg.Button('Saglabat lasitaja datus')],
        [psg.Button('lasitaja datu apskate')]
]


layout2 = [
    [psg.Text("gramatas")],
    [psg.Text('nosaukums'),psg.InputText()],
    [psg.Text('Telefona numurs'),psg.InputText()],
    [psg.Text('autors'),psg.InputText()],
    [psg.Button('Saglabat gramatas datus')],
    [psg.Button('gramatas datu apskate')]    
    
]


logugrupa = [[
    psg.TabGroup(
        [
         [
            psg.Tab('lasitajs',layout),
            psg.Tab('gramata',layout2)
         ]   
        ]
    ),
    psg.Button('Aizvert')
]]

window = psg.Window('Biblioteka', logugrupa)
while True:
    event,values = window.read()
