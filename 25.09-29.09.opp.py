#Bibliotēkas vadības sistēma
#Bibliotēkas importēšana
import PySimpleGUI as psg

#Izveidota klase
class Biblioteka():

    #Izveidots konstruktors
    def __init__(self,lasitajs_vards,lasitajs_uzvards,lasitajs_pk,lasitajs_tel_numurs,gramatas_kategorija,gramatas_raksturojums,gramatas_cena,gramatas_nosaukums):
            self.lasitajs_vards = lasitajs_vards
            self.lasitajs_uzvards = lasitajs_uzvards
            self.lasitajs_pk = lasitajs_pk
            self.lasitajs_tel_numurs = lasitajs_tel_numurs
            self.gramatas_cena = gramatas_cena
            self.gramatas_nosaukums = gramatas_nosaukums
            self.gramatas_raksturojums = gramatas_raksturojums
            self.gramatas_kategorija = gramatas_kategorija
    #Izveidotas metodes datu apskatei
    def lasitajs_info(self):
        print("lasitajs vārds: ", self.lasitajs_vards)
        print("lasitajs uzvārds: ", self.lasitajs_uzvards)
        print("lasitajs p.k.: ", self.lasitajs_pk)
        print("lasitajs tel numurs: ", self.lasitajs_tel_numurs)
    def gramatas_info(self):
        print("gramatas vārds: ", self.gramatas_nosaukums)
        print("gramatas uzvārds: ", self.gramatas_raksturojums)
        print("gramatas kategorija: ", self.gramatas_kategorija)
        print("gramatas cena: ", self.gramatas_cena)

    #Izveidotas metodes datu saglabāšanai
    def lasitajs_saglabat(self):
        with open('lasitajs.txt', 'w', encoding="utf-8") as fails :
            fails.write("-lasitajs-")
            fails.write(" \n")
            fails.write(str(Dati.lasitajs_vards))
            fails.write(" \n")
            fails.write(str(Dati.lasitajs_uzvards))
            fails.write(" \n")
            fails.write(str(Dati.lasitajs_pk))
            fails.write(" \n")
            fails.write(str(Dati.lasitajs_tel_numurs))

    def gramatas_saglabat(self):
        with open('gramatas.txt', 'w', encoding="utf-8") as fails :
            fails.write("-gramatas-")
            fails.write(" \n")
            fails.write(str(Dati.gramatas_nosaukums))
            fails.write(" \n")
            fails.write(str(Dati.gramatas_raksturojums))
            fails.write(" \n")
            fails.write(str(Dati.gramatas_kategorija))
            fails.write(" \n")
            fails.write(str(Dati.gramatas_cena))

Dati = Biblioteka(lasitajs_vards="Jānis",lasitajs_uzvards="Kalniņš",lasitajs_pk="132435-32153",lasitajs_tel_numurs="25436789",gramatas_nosaukums=" Ronja un viņa laupītāju meita",gramatas_raksturojums="raksturots",gramatas_kategorija="Bērnu",gramatas_cena="25 EUR")
Dati.lasitajs_saglabat()
Dati.gramatas_saglabat()
Dati.lasitajs_info()
Dati.gramatas_info()



psg.theme('LightGreen4')
layout = [
        [psg.Text('LASĪTĀJS')],
        [psg.Text('Vārds'),psg.InputText()],
        [psg.Text('Uzvārds'),psg.InputText()],
        [psg.Text('Personas kods'),psg.InputText()],
        [psg.Text('Telefona numurs'),psg.InputText()],
        [psg.Button('Saglabāt lasitaja datus')],
        [psg.Button('lasitaja datu apskate')]
]
layout2 = [
    [psg.Text("GRĀMATAS")],
    [psg.Text('Nosaukums'),psg.InputText()],
    [psg.Text('Raksturojums'),psg.InputText()],
    [psg.Text('Kategorija'),psg.InputText()],
    [psg.Text('Cena'),psg.InputText()],
    [psg.Button('Saglabāt grāmatas datus')],
    [psg.Button('Grāmatas datu apskate')]    
    
]



logugrupa = [[
    psg.TabGroup(
        [
         [
            psg.Tab('lasitajs',layout),
            psg.Tab('gramatas',layout2)
         ]   
        ]
    ),
    psg.Button('Aizvērt')
]]


window = psg.Window('Biblioteka', logugrupa)
while True:
    event,values = window.read()
