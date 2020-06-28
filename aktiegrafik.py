#lyckas rensa output-fönstret mellan omgångarna när man klickar på knapparna
#när koden är klar - integrera den korrekt med grafiken
from tkinter import *
import aktie
from aktie import Aktie


ericsson_AV = "772"
electrolux_AV = "2193"
astraZeneca_AV = "1295"
volvo_AV = "1146"

ericsson_NN = "100"
electrolux_NN = "81"
astraZeneca_NN = "3524"
volvo_NN = "365"

class Grafik():
   

#Skapar ett fönster som man inte kan formatera om
    def __init__(self):
        self.root = Tk()
        self.root.geometry("484x300")
        self.root.resizable(width=False, height=False)
        self.root.title("Aktieinköp")
 
#Hälsningsfrasen och output-fönstret

    
        self.text1 = Label(self.root, text = "Välkommen till Aktieanalytikern! Gör ditt val nedan.")
        self.text1.place(x=75, y=1)
        self.rad1 = Label(self.root, text = "")
        self.rad1.place(x=1, y=40)
        self.rad2 = Label(self.root, text = "")
        self.rad2.place(x=1, y=60)
        self.rad3 = Label(self.root, text = "")
        self.rad3.place(x=1, y=80)
        self.rad4 = Label(self.root, text = "")
        self.rad4.place(x=1, y=100)
 
#Fundamentala analysen, text och knappar
        self.text2 = Label(self.root, text = "En fundamental analys kan genomföras på följande aktier:")
        self.text2.place(x=1, y=140)
        self.knapp_ericsson = Button(self.root, text = aktie.get_stock_name(ericsson_AV), width=13, command = lambda : self.fundamenta(ericsson_AV))
        self.knapp_ericsson.place(x=1, y=160)
        self.knapp_astra = Button(self.root, text = aktie.get_stock_name(astraZeneca_AV), width=13, command = lambda : self.fundamenta(astraZeneca_AV))
        self.knapp_astra.place(x=120, y=160)
        self.knapp_electro = Button(self.root, text = aktie.get_stock_name(electrolux_AV), width=13, command = lambda : self.fundamenta(electrolux_AV))
        self.knapp_electro.place(x=240, y=160)
        self.knapp_volvo = Button(self.root, text = aktie.get_stock_name(volvo_AV), width=13, command = lambda : self.fundamenta(volvo_AV))
        self.knapp_volvo.place(x=360, y=160)
 
#Tekniska analysen, text och knappar
        self.text3 = Label(self.root, text = "En teknisk analys kan genomföras på följande aktier:")
        self.text3.place(x=1, y=200)
        self.knapp2_ericsson = Button(self.root, text = aktie.get_stock_name(ericsson_AV), width=13, command = lambda : self.teknisk(ericsson_NN, "ERIC"))
        self.knapp2_ericsson.place(x=1, y=220)
        self.knapp2_astra = Button(self.root, text = aktie.get_stock_name(astraZeneca_AV), width=13, command = lambda : self.teknisk(astraZeneca_NN, "ELUX-B.ST" ))
        self.knapp2_astra.place(x=120, y=220)
        self.knapp2_electro = Button(self.root, text = aktie.get_stock_name(electrolux_AV), width=13, command = lambda : self.teknisk(electrolux_NN, "AZN"))
        self.knapp2_electro.place(x=240, y=220)
        self.knapp2_volvo = Button(self.root, text = aktie.get_stock_name(volvo_AV), width=13, command = lambda : self.teknisk(volvo_NN, "VOLV-B.ST"))
        self.knapp2_volvo.place(x=360, y=220)
 
#Sista raden med beta-ranking och hjälp-knapp
        self.knapp_beta = Button(self.root, text = "Ranking efter betavärde", width=20, command = self.beta)
        self.knapp_beta.place(x=1, y=260)
        self.knapp_hjälp = Button(self.root, text = "Hjälp", width=16, command = self.hjälp)
        self.knapp_hjälp.place(x=190, y=260)
        self.knapp_rensa = Button(self.root, text = "Rensa", width=15, command = self.rensa)
        self.knapp_rensa.place(x=340, y=260)
        self.root.mainloop()
 
    def rensa (self):
        rad1 = Label(self.root, text = "                                                                                                                                                          ")
        rad1.place(x=1, y=40)
        rad2 = Label(self.root, text = "                                                                                                                                                     ")
        rad2.place(x=1, y=60)
        rad3 = Label(self.root, text = "                                                                                                                                                   ")
        rad3.place(x=1, y=80)
        rad4 = Label(self.root, text = "                                                                                                                                                   ")
        rad4.place(x=1, y=100)
 
    def fundamenta (self, ticker):
        self.rensa()
        rad1 = Label(self.root, text = "företagets soliditet är: " + aktie.get_stock_solidity(ticker)) #addera anrop till funktion/metod som ger mig soliditet
        rad1.place(x=20, y=40)
        rad2 = Label(self.root, text = "företagets p/e-tal är: " + aktie.get_stock_PE(ticker))
        rad2.place(x=20, y=60)
        rad3 = Label(self.root, text = "företagets p/s-tal är: " + aktie.get_stock_PS(ticker))
        rad3.place(x=20, y=80)
 
    def teknisk (self, ticker, ticker_Yahoo):
        self.rensa()
        rad1 = Label(self.root, text = "företagets kursutveckling är: " + aktie.get_stock_develop(ticker))
        rad1.place(x=20, y=40)
        rad2 = Label(self.root, text = "betavärdet är: " + str(aktie.get_stock_beta(ticker_Yahoo)))
        rad2.place(x=20, y=60)
        rad3 = Label(self.root, text = "lägsta kurs (senaste 30 dagarna): " + aktie.get_stock_low(ticker))
        rad3.place(x=20, y=80)
        rad4 = Label(self.root, text = "högsta kurs (senaste 30 dagarna): " + aktie.get_stock_high(ticker))
        rad4.place(x=20, y=100)
 
    def beta (self):
        self.rensa()
        tickersYahoo = ["ERIC", "ELUX-B.ST", "AZN", "VOLV-B.ST"]
        beta_list = []
        for i in range(len(tickersYahoo)):
            beta_list.append(aktie.get_stock_beta(tickersYahoo[i]))

        ericsson_stock = Aktie(aktie.get_stock_name(ericsson_AV), beta_list[0])
        electrolux_stock = Aktie(aktie.get_stock_name(electrolux_AV), beta_list[1])
        astra_stock = Aktie(aktie.get_stock_name(astraZeneca_AV), beta_list[2])
        volvo_stock = Aktie(aktie.get_stock_name(volvo_AV), beta_list[3])

        aktieLista = []
        aktieLista.extend((ericsson_stock, electrolux_stock, astra_stock, volvo_stock))

        aktieLista.sort(key=lambda x : x.beta, reverse = True)

        counter = 0
        counter_y = 20
 
        for i in aktieLista:
            counter += 1
            counter_y += 20
            rad = Label(self.root, text = (str(counter) + " " + i.namn + " " + str(i.beta)))
            rad.place(x=160, y=counter_y)
        
            
 
    def hjälp (self):
        self.rensa()
        rad1 = Label(self.root, text = "Välj vilken typ av analys du vill göra genom att klicka på någon av knapparna.")
        rad1.place(x=1, y=40)
        rad2 = Label(self.root, text = "Fundamental analys: värdering baserad på bolagets nyckeltal.")
        rad2.place(x=1, y=60)
        rad3 = Label(self.root, text = "Teknisk analys: värdering baserad på aktiekursens utveckling.")
        rad3.place(x=1, y=80)
 


 
Grafik()
