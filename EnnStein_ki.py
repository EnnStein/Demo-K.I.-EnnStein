import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit) #verschiedene Klassen für Oberfläche (Managementsysem, Fenster, Textfelder, Knöpfe, Schreibzeile)
from PyQt6.QtGui import QFont, QPixmap, QTransform, QIcon #Schriftarten, für Bild
from PyQt6.QtCore import Qt, QSize #Klassen für Optik
#oben notwendige Module

#Klassen für GUI

#Erklärungs-/Startfenster
class Startfenster(QWidget):
    #Fenster, welches kurz die Funktion des Programms zusammenfasst
    #und einen manuellen Start durch den Anwender ermöglicht
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fensters
        self.setWindowTitle("Startfenster") #Bezeichnung
        self.setUpStartfenster() #siehe unten
        self.show() #zeigt sich selbst
    def setUpStartfenster(self):
        #unten stehen Texte zur Erklärung
        self.Text_a_Label = QLabel(self)
        self.Text_a_Label.setText("Dies ist ein Computerprogramm, welches das maschinelle überwachte Lernen demonstrieren soll.")
        self.Text_a_Label.setFont(QFont("Arial", 15))
        self.Text_a_Label.setWordWrap(True)
        self.Text_a_Label.move(20, 15)
        self.Text_b_Label = QLabel(self)
        self.Text_b_Label.setText("Man kann ein Modell anlernen, sich die Daten ausgeben lassen oder die Informationen zurücksetzen.")
        self.Text_b_Label.setFont(QFont("Arial", 15))
        self.Text_b_Label.setWordWrap(True)
        self.Text_b_Label.move(20,90)
        self.Text_c_Label = QLabel(self)
        self.Text_c_Label.setText("Spiel etwas mit der Technik rum und finde mind. zwei große Schwachstellen vieler K.I.'s.")
        self.Text_c_Label.setFont(QFont("Arial", 15))
        self.Text_c_Label.setWordWrap(True)
        self.Text_c_Label.move(20, 165)
        self.Start_Knopf_Bild() #Knopf, der Menu öffnet
    #Methode, die bebilderten Knopf zum Starten erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Start_Knopf_Bild(self):
        image = "Start.PNG"
        try:
            with open(image):
                Start_Knopf = QPushButton(self)
                Start_Knopf.clicked.connect(self.start)
                Start_Knopf.move(200, 300)
                Bild = QIcon(image)
                Start_Knopf.setIcon(Bild)
                Start_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Start_Knopf = QPushButton("Start", self)
            Start_Knopf.setFont(QFont("Arial", 16))
            Start_Knopf.clicked.connect(self.start)
            Start_Knopf.move(200, 300)
    #zeigt Menu und versteckt sich selbst
    def start(self):
        MenuFenster.show() #zeigt Fenster offen an
        self.hide() #versteckt sich selbst

#Menufenster
class Menufenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fesnters
        self.setWindowTitle("Hauptmenü") #Bezeichnung
        self.setUpMenu() #siehe unten
    def setUpMenu(self):
        #Knopf, der Anlernen startet und Fenster erstellt
        self.Lern_Knopf = QPushButton("Anlernen", self)
        self.Lern_Knopf.setFont(QFont("Arial", 16))
        self.Lern_Knopf.clicked.connect(self.startLernen)
        self.Lern_Knopf.move(75, 25)
        self.Tafel_Bild()
        #Knopf, der Ausgabe mit Super Surface Language Model SSLM startet
        self.Ausgabe_Knopf = QPushButton("Ausgabe", self)
        self.Ausgabe_Knopf.setFont(QFont("Arial", 16))
        self.Ausgabe_Knopf.clicked.connect(self.startAusgabe)
        self.Ausgabe_Knopf.move(390, 25)
        self.Suchen_Bild()
        #Knopf, der Ausgabe der reinen startet und Fenster erstellt
        self.Ausgabe_Daten_Knopf = QPushButton("Datenbank", self)
        self.Ausgabe_Daten_Knopf.setFont(QFont("Arial", 16))
        self.Ausgabe_Daten_Knopf.clicked.connect(self.startAusgabeDaten)
        self.Ausgabe_Daten_Knopf.move(390, 250)
        self.Daten_Bild()
        #Knopf, der Daten zurücksetzt
        self.Zuruecksetzen_Knopf = QPushButton("Daten zurücksetzen", self)
        self.Zuruecksetzen_Knopf.setFont(QFont("Arial", 16))
        self.Zuruecksetzen_Knopf.clicked.connect(self.datenZuruecksetzen)
        self.Zuruecksetzen_Knopf.move(60, 250)
        self.Loeschen_Bild()
        #Knopf, um das Programm ganz zu beenden
        self.Beenden_Knopf_Bild()
        #Knopf, um Mitwirkende anzugeigen
        self.MitWirk_Knopf = QPushButton("Mitwirkende", self)
        self.MitWirk_Knopf.setFont(QFont("Arial", 16))
        self.MitWirk_Knopf.clicked.connect(self.startCredits)
        self.MitWirk_Knopf.move(690, 25)
        self.MitWirk_Bild()
        #Knopf, um Erklärungsfenster zu öffnen
        self.Erklaer_Knopf = QPushButton("Algorithmus", self)
        self.Erklaer_Knopf.setFont(QFont("Arial", 16))
        self.Erklaer_Knopf.clicked.connect(self.startErklaerung)
        self.Erklaer_Knopf.move(700, 250)
        self.Erklaer_Bild()
    #Methode, die Bild erstellt
    def Tafel_Bild(self):
        image = "Tafel.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(180,120)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(40, 60)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die Bild erstellt
    def Suchen_Bild(self):
        image = "Lupe.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(120,120)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(390, 60)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die Bild erstellt
    def Loeschen_Bild(self):
        image = "Mülleimer.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(120,130)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(90, 300)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die Bild erstellt
    def Daten_Bild(self):
        image = "Daten.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(180,120)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(340, 300)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die Bild erstellt
    def MitWirk_Bild(self):
        image = "Mitwirkende.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(100,80)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(700, 60)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die Bild erstellt
    def Erklaer_Bild(self):
        image = "Kopf.JPG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(176, 99)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(670, 290)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Beenden_Knopf_Bild(self):
        image = "Ende.PNG"
        try:
            with open(image):
                Beenden_Knopf = QPushButton(self)
                Beenden_Knopf.clicked.connect(self.beenden)
                Beenden_Knopf.move(425, 510)
                Bild = QIcon(image)
                Beenden_Knopf.setIcon(Bild)
                Beenden_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Beenden_Knopf = QPushButton("Beenden", self)
            Beenden_Knopf.setFont(QFont("Arial", 16))
            Beenden_Knopf.clicked.connect(self.beenden)
            Beenden_Knopf.move(425, 510)
    #startet Lernen
    def startLernen(self):
        AnlernFenster.show() #zeigt Fenster, um Modell anzulernen
        InfoFensterA.show()
        self.hide() #versteckt sich selbst
    def startAusgabe(self):
        AusgabeFenster.show()
        self.hide() #versteckt sich selbst
    def startAusgabeDaten(self):
        DatenFenster.show() #zeigt Fenster für Ausgabe
        self.hide() #versteckt sich selbst
    def datenZuruecksetzen(self):
        #die Eigenschaften, die das Verhältnis des Objekts zum Thema speichern, werden auf 0 zurückgesetzt
        self.löschen(Sammlung) #siehe unten
        AnlernFenster.lernen_gestartet = False
        AnlernFenster.zaehler = 0
        AnlernFenster.Text_Label.setText("                                                                                                                                     ")
        AnlernFenster.Kennung_Label.setText("   ")
        InfoFensterC.show()
    def löschen(self, Sammlung): #eigentliches Löschverfahren
        for text in Sammlung:
            text.Katze = 0
            text.Hund = 0
            text.Auto = 0
            #'0' == 'unbekannt'
    def startCredits (self): #zeigt Mitwirkende an
        MitWirkFenster.show() #zeigt Fenster mit Mitwirkenden an
        self.hide() #versteckt sich selbst
    def startErklaerung(self):
        ErklaerFenster.show()
        self.hide()
    def beenden(self): #beendet ganzes Programm
        print("Programm beendet") #schreibt in Konsole
        self.close() #schließt Fenster und beendet Programm

#Lernfenster
class Lernfenster(QWidget):
    lernen_gestartet = False #mechanisch/logisch notwendige Variable
    zaehler = 0 #wird verwendet, um Nachricht auszugeben, wenn jedem Text ein Thema zugeordnet wurde
    def __init__(self): #wird beim Initialisieren des Objektes (hier Fensters) ausgeführt
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position
        self.setWindowTitle("Anlern-Fenster")
        self.setUpLernfenster() #siehe unten
    def setUpLernfenster(self): #enthält Layout
        #unten Labels
        #unten Label für Text
        self.Text_Label = QLabel("                                                                                                                                     ", self)
        self.Text_Label.setFont(QFont("Arial", 15))
        self.Text_Label.move(60, 15)
        #unten Label, das 'Text' anzeigt
        self.Anzeige_Text_Label = QLabel("Text: ", self)
        self.Anzeige_Text_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Text_Label.move(15, 15)
        #unten Label für Kennung/Nummer
        self.Kennung_Label = QLabel("   ", self)
        self.Kennung_Label.setFont(QFont("Arial", 15))
        self.Kennung_Label.move(100, 45)
        #unten Label, das 'Nummer' anzeigt
        self.Anzeige_Kennung_Label = QLabel("Nummer: ", self)
        self.Anzeige_Kennung_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Kennung_Label.move(15, 45)
        #unten Initialisierung Knöpfe & Verbindung mit Funktionen
        #Knopf, der dem Text das Thema 'Katze' zuordnet
        self.Katze_Knopf = QPushButton("Katze", self)
        self.Katze_Knopf.setFont(QFont("Arial", 16))
        self.Katze_Knopf.clicked.connect(self.Katze)
        self.Katze_Knopf.move(50, 100)
        #Knopf, der dem Text das Thema 'Hund' zuordnet
        self.Hund_Knopf = QPushButton("Hund", self)
        self.Hund_Knopf.setFont(QFont("Arial", 16))
        self.Hund_Knopf.clicked.connect(self.Hund)
        self.Hund_Knopf.move(200, 100)
        #Knopf, der dem Text das Thema 'Auto' zuordnet
        self.Auto_Knopf = QPushButton("Auto", self)
        self.Auto_Knopf.setFont(QFont("Arial", 16))
        self.Auto_Knopf.clicked.connect(self.Auto)
        self.Auto_Knopf.move(350, 100)
        #Knopf für Start
        self.Start_Knopf_Bild()
        #Knopf für manuelles Ende des Anlernens
        self.Beenden_Knopf_Bild()
    #Funktion, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Start_Knopf_Bild(self):
        image = "Start.PNG"
        try:
            with open(image):
                Start_Knopf = QPushButton(self)
                Start_Knopf.clicked.connect(self.start)
                Start_Knopf.move(400, 200)
                Bild = QIcon(image)
                Start_Knopf.setIcon(Bild)
                Start_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Start_Knopf = QPushButton("Start", self)
            Start_Knopf.setFont(QFont("Arial", 16))
            Start_Knopf.clicked.connect(self.start)
            Start_Knopf.move(400, 200)
    #Funktion, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Beenden_Knopf_Bild(self):
        image = "Menü.PNG"
        try:
            with open(image):
                Beenden_Knopf = QPushButton(self)
                Beenden_Knopf.clicked.connect(self.beenden)
                Beenden_Knopf.move(400, 525)
                Bild = QIcon(image)
                Beenden_Knopf.setIcon(Bild)
                Beenden_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Beenden_Knopf = QPushButton("Menü", self)
            Beenden_Knopf.setFont(QFont("Arial", 16))
            Beenden_Knopf.clicked.connect(self.beenden)
            Beenden_Knopf.move(400, 525)
    #unten stehen die Methoden
    def start(self): #startet das Lernen
        if self.lernen_gestartet == False:
            self.naechstesThema(Sammlung)
        self.lernen_gestartet = True
    #zeigt neuen Text; wird von anderen Methoden gestartet
    def naechstesThema(self, Sammlung):
        self.Text_Label.setText(Sammlung[self.zaehler].Text) #passt Text in Label an
        self.Kennung_Label.setText(Sammlung[self.zaehler].Kennung)
        if self.zaehler == len(Sammlung)-1:
            InfoFensterB.show()
            self.Text_Label.setText("                                                                                                       ")
            self.Kennung_Label.setText("   ")
    def Katze(self):
        if self.lernen_gestartet == True:
            Sammlung[self.zaehler].Katze = 1
            Sammlung[self.zaehler].Hund = 2
            Sammlung[self.zaehler].Auto = 2
            self.zaehler += 1
            self.naechstesThema(Sammlung)
    def Hund(self):
        if self.lernen_gestartet == True:
            Sammlung[self.zaehler].Hund = 1
            Sammlung[self.zaehler].Katze = 2
            Sammlung[self.zaehler].Auto = 2
            self.zaehler += 1
            self.naechstesThema(Sammlung)
    def Auto(self):
        if self.lernen_gestartet == True:
            Sammlung[self.zaehler].Auto = 1
            Sammlung[self.zaehler].Katze = 2
            Sammlung[self.zaehler].Hund = 2
            self.zaehler += 1 #Zähler wird um 1 vergrößert
            self.naechstesThema(Sammlung)
    def beenden(self): #beendet das Anlernen und versteckt dieses Fenster
        MenuFenster.show() #zeigt Menu
        self.hide() #versteckt sich selbst

#Ausgabefenster; verwendet Super Surface Language Model SSLM
class Ausgabefenster(QWidget):
    def __init__(self): #wird bei Initialisierung des Objekts (hier Fensters) ausgeführt
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fensters
        self.setWindowTitle("Ausgabefenster") #Bezeichnung
        self.setUpAusgabefenster() #siehe unten
    def setUpAusgabefenster(self):
        #Label, das 'Frag EnnStein' anzeigt
        self.EnnStein_Label = QLabel("Frag EnnStein", self)
        self.EnnStein_Label.setFont(QFont("Arial", 32))
        self.EnnStein_Label.move(320, 15)
        #Label zur Erklärung
        self.Text_Label = QLabel("Gib unten einen Suchbegriff ein.", self)
        self.Text_Label.setFont(QFont("Arial", 15))
        self.Text_Label.move(320, 100)
        #Label als Ausgabefläche
        self.Antwort_Label = QLabel("                                                                                                                              ", self)
        self.Antwort_Label.setFont(QFont("Arial", 15))
        self.Antwort_Label.move(100, 200)
        #Label, das 'Antwort' anzeigt
        self.Anzeige_Antwort_Label = QLabel("Antwort:", self)
        self.Anzeige_Antwort_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Antwort_Label.move(25, 200)
        #Suchzeile; hier kann man etwas eingeben
        self.Anfrage_Edit = QLineEdit(self)
        self.Anfrage_Edit.resize(530, 30)
        self.Anfrage_Edit.setFont(QFont("Arial", 15))
        self.Anfrage_Edit.move(160, 130)
        #Knopf, mit dem man die Suche startet
        self.Suchen_Knopf_Bild()
        #Knopf, der Eingabezeile reinigt
        self.Loeschen_Knopf_Bild()
        #Knopf, mit dem man zum Menu zurückkehrt
        self.Beenden_Knopf_Bild()
    #Funktion, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Suchen_Knopf_Bild(self):
        image = "Lupe.PNG"
        try:
            with open(image):
                Suchen_Knopf = QPushButton(self)
                Suchen_Knopf.clicked.connect(self.startSuchen)
                Suchen_Knopf.move(120, 128)
                Bild = QIcon(image)
                Suchen_Knopf.setIcon(Bild)
                Suchen_Knopf.setIconSize(QSize(23, 23))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Suchen_Knopf = QPushButton("Suchen", self)
            Suchen_Knopf.setFont(QFont("Arial", 16))
            Suchen_Knopf.clicked.connect(self.startSuchen)
            Suchen_Knopf.move(15, 130)
    #Funktion, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Loeschen_Knopf_Bild(self):
        image = "Kreuz.PNG"
        try:
            with open(image):
                Loeschen_Knopf = QPushButton(self)
                Loeschen_Knopf.clicked.connect(self.loeschen)
                Loeschen_Knopf.move(687, 128)
                Bild = QIcon(image)
                Loeschen_Knopf.setIcon(Bild)
                Loeschen_Knopf.setIconSize(QSize(23, 23))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Loeschen_Knopf = QPushButton("Leeren", self)
            Loeschen_Knopf.setFont(QFont("Arial", 16))
            Loeschen_Knopf.clicked.connect(self.loeschen)
            Loeschen_Knopf.move(550, 130)
    #Funktion, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Beenden_Knopf_Bild(self):
        image = "Menü.PNG"
        try:
            with open(image):
                Beenden_Knopf = QPushButton(self)
                Beenden_Knopf.clicked.connect(self.beenden)
                Beenden_Knopf.move(400, 525)
                Bild = QIcon(image)
                Beenden_Knopf.setIcon(Bild)
                Beenden_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Beenden_Knopf = QPushButton("Menü", self)
            Beenden_Knopf.setFont(QFont("Arial", 16))
            Beenden_Knopf.clicked.connect(self.beenden)
            Beenden_Knopf.move(400, 525)
    #Methode, die das Suchen einleitet
    def startSuchen(self):
        self.suchen(Sammlung)
    #Methode für die eigentliche Suche
    def suchen(self, Sammlung):
        Anfrage = grossKlein(self.Anfrage_Edit.text())
        laenge_anfrage = len(Anfrage)
        zaehler = 0
        katze_zaehler = 0
        hund_zaehler = 0
        auto_zaehler = 0
        for text in Sammlung:
            anfang = 0
            ende = laenge_anfrage
            laenge_text = len(text.Text) -1
            while ende < laenge_text:
                auszug = ""
                for y in range(anfang,ende):
                    auszug = auszug + grossKlein(text.Text[y])
                if auszug == Anfrage:
                    if text.Katze == 1:
                        katze_zaehler += 1
                        zaehler += 1
                    elif text.Hund == 1:
                        hund_zaehler += 1
                        zaehler += 1
                    elif text.Auto == 1:
                        auto_zaehler += 1
                        zaehler += 1
                anfang += 1
                ende += 1
        Themen_Zaehler = [katze_zaehler, hund_zaehler, auto_zaehler]
        Themen_Zaehler.sort(reverse = True)
        if zaehler == 0 or len(Anfrage) == 0:
            self.Antwort_Label.setText("Ich weiß es nicht!                                                                                                                 ")
        elif katze_zaehler == Themen_Zaehler[0]:
            self.Antwort_Label.setText("Der Text hat etwas mit Katzen zu tun.")
        elif hund_zaehler == Themen_Zaehler[0]:
            self.Antwort_Label.setText("Der Text hat etwas mit Hunden zu tun.")
        elif auto_zaehler == Themen_Zaehler[0]:
            self.Antwort_Label.setText("Der Text hat etwas mit Autos zu tun.")
    #Methode, die Zeile für Suche und Bereich für Antworten säubert/leert
    def loeschen(self):
        self.Anfrage_Edit.clear()
        self.Antwort_Label.setText("                                                                                                                               ")
    #Methode, die Fenster versteckt und auf Ausgangssetting zurücksetzt
    def beenden(self):
        self.loeschen()
        MenuFenster.show()
        self.hide()

#Ausgabefenster
class Datenfenster(QWidget):
    def __init__(self): #wird bei Initialisierung des Objekts (hier Fensters) ausgeführt
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fensters
        self.setWindowTitle("Ausgabe Datenbank") #Bezeichnung
        self.setUpDatenfenster() #siehe unten
    def setUpDatenfenster(self):
        #unten Initialisierung Textfelder
        #zuerst Anzeigen, dann variable Felder
        #Label, das 'Text' anzeigt
        self.Anzeige_Text_Label = QLabel("Text:", self)
        self.Anzeige_Text_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Text_Label.move(20, 70)
        #Label, das den Text des Objektes anzeigt
        self.Text_Label = QLabel("                                                                                                                                     ", self)
        self.Text_Label.setFont(QFont("Arial", 15))
        self.Text_Label.move(65, 70)
        #Label zeigt 'Katze' an
        self.Anzeige_Katze_Label = QLabel("Katze: ", self)
        self.Anzeige_Katze_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Katze_Label.move(20, 130)
        #Label zeigt 'Hund' an
        self.Anzeige_Hund_Label = QLabel("Hund: ", self)
        self.Anzeige_Hund_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Hund_Label.move(20, 180)
        #Label zeigt 'Auto' an
        self.Anzeige_Auto_Label = QLabel("Auto: ", self)
        self.Anzeige_Auto_Label.setFont(QFont("Arial", 15))
        self.Anzeige_Auto_Label.move(20, 230)
        #unten Labels, die Status anzeigen
        #für Katze
        self.Katze_Label = QLabel("                                                                                                             ", self)
        self.Katze_Label.setFont(QFont("Arial", 15))
        self.Katze_Label.move(80, 130)
        #für Hund
        self.Hund_Label = QLabel("                                                                                                             ", self)
        self.Hund_Label.setFont(QFont("Arial", 15))
        self.Hund_Label.move(80, 180)
        #für Auto
        self.Auto_Label = QLabel("                                                                                                             ", self)
        self.Auto_Label.setFont(QFont("Arial", 15))
        self.Auto_Label.move(75, 230)
        #Knöpfe zum Aufrufen der einzelnen Artikel nach Kennung
        #für Text A
        self.A_Knopf = QPushButton("A", self)
        self.A_Knopf.setFont(QFont("Arial", 16))
        self.A_Knopf.clicked.connect(self.startAusgabeA)
        self.A_Knopf.move(20, 20)
        #für Text B
        self.B_Knopf = QPushButton("B", self)
        self.B_Knopf.setFont(QFont("Arial", 16))
        self.B_Knopf.clicked.connect(self.startAusgabeB)
        self.B_Knopf.move(95, 20)
        #für Text C
        self.C_Knopf = QPushButton("C", self)
        self.C_Knopf.setFont(QFont("Arial", 16))
        self.C_Knopf.clicked.connect(self.startAusgabeC)
        self.C_Knopf.move(170, 20)
        #für Text D
        self.D_Knopf = QPushButton("D", self)
        self.D_Knopf.setFont(QFont("Arial", 16))
        self.D_Knopf.clicked.connect(self.startAusgabeD)
        self.D_Knopf.move(245, 20)
        #für Text E
        self.E_Knopf = QPushButton("E", self)
        self.E_Knopf.setFont(QFont("Arial", 16))
        self.E_Knopf.clicked.connect(self.startAusgabeE)
        self.E_Knopf.move(320, 20)
        #für Text F
        self.F_Knopf = QPushButton("F", self)
        self.F_Knopf.setFont(QFont("Arial", 16))
        self.F_Knopf.clicked.connect(self.startAusgabeF)
        self.F_Knopf.move(395, 20)
        #Knopf, um zum Menu zurückzukehren (mit Bild), bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
        self.Beenden_Knopf_Bild()
    #Funktion, die bebilderten Knopf erstellt
    def Beenden_Knopf_Bild(self):
        image = "Menü.PNG"
        try:
            with open(image):
                Beenden_Knopf = QPushButton(self)
                Beenden_Knopf.clicked.connect(self.beenden)
                Beenden_Knopf.move(400, 525)
                Bild = QIcon(image)
                Beenden_Knopf.setIcon(Bild)
                Beenden_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Beenden_Knopf = QPushButton("Menü", self)
            Beenden_Knopf.setFont(QFont("Arial", 16))
            Beenden_Knopf.clicked.connect(self.beenden)
            Beenden_Knopf.move(400, 525)
    #Funktion zum Beenden der Ausgabe
    def beenden(self):
        MenuFenster.show() #zeigt Menu
        #unten werden Texte aus Labels auf 'Leerstand' gesetzt
        self.Text_Label.setText("                                                                                                               ")
        self.Katze_Label.setText("                                                                                                             ")
        self.Hund_Label.setText("                                                                                                             ")
        self.Auto_Label.setText("                                                                                                             ")
        self.hide() #versteckt sich selbst
    #Funktionen für Ausgabe
    #unten sind 'Anwahlen' für die Ausgabe; je nachdem, von welchem Knopf aus die Anwahl erfolgt, wird ein anderer Text ausgegeben
    def startAusgabeA(self):
        self.ausgeben("A")
    def startAusgabeB(self):
        self.ausgeben("B")
    def startAusgabeC(self):
        self.ausgeben("C")
    def startAusgabeD(self):
        self.ausgeben("D")
    def startAusgabeE(self):
        self.ausgeben("E")
    def startAusgabeF(self):
        self.ausgeben("F")
    #unten erfolgt eigentliche Ausgabe der Informationen, nachdem indem andere Methode genutzt wird
    def ausgeben(self, ursprung):
        if ursprung == "A":
            self.pruefen(Text_a)
        elif ursprung == "B":
            self.pruefen(Text_b)
        elif ursprung == "C":
            self.pruefen(Text_c)
        elif ursprung == "D":
            self.pruefen(Text_d)
        elif ursprung == "E":
            self.pruefen(Text_e)
        elif ursprung == "F":
            self.pruefen(Text_f)
    def pruefen(self, Text): #verarbeitet Daten für Ausgabe
        unbekannt = "Es ist nicht bekannt, ob dieser Text zu diesem Thema gehört."
        richtig = "Der Text gehört zu diesem Thema."
        falsch = "Der Text gehört nicht zu diesem Thema."
        self.Text_Label.setText(Text.Text)
        if Text.Katze == 0:
            self.Katze_Label.setText(unbekannt)
        elif Text.Katze == 1:
            self.Katze_Label.setText(richtig)
        elif Text.Katze == 2:
            self.Katze_Label.setText(falsch)
        if Text.Hund == 0:
            self.Hund_Label.setText(unbekannt)
        elif Text.Hund == 1:
            self.Hund_Label.setText(richtig)
        elif Text.Hund == 2:
            self.Hund_Label.setText(falsch)
        if Text.Auto == 0:
            self.Auto_Label.setText(unbekannt)
        elif Text.Auto == 1:
            self.Auto_Label.setText(richtig)
        elif Text.Auto == 2:
            self.Auto_Label.setText(falsch)

#Informationsfenster
#Informationen vor Anlernen
class Informationsfenster_A(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(350,200,300,200) #Position & Größe
        self.setWindowTitle("Informationsfenster") #Bezeichnung
        self.setUpInfoFenster() #sieh unten
    def setUpInfoFenster(self):
        #Texte, die Aufgabe erklären
        self.Info_Label_a = QLabel("Drücke auf den Knopf mit dem ", self)
        self.Info_Label_a.setFont(QFont("Arial", 15))
        self.Info_Label_a.move(15, 15)
        self.Info_Label_b = QLabel("Thema, das zum angezeigtem", self)
        self.Info_Label_b.setFont(QFont("Arial", 15))
        self.Info_Label_b.move(15, 40)
        self.Info_Label_c = QLabel("Text gehört. Um Anzufangen, ", self)
        self.Info_Label_c.setFont(QFont("Arial", 15))
        self.Info_Label_c.move(15, 65)
        self.Info_Label_d = QLabel("drücke auf 'Start'.", self)
        self.Info_Label_d.setFont(QFont("Arial", 15))
        self.Info_Label_d.move(15, 90)
        #Knopf, der Fenster schließt
        self.Beenden_Knopf = QPushButton("Schließen", self)
        self.Beenden_Knopf.setFont(QFont("Arial", 16))
        self.Beenden_Knopf.clicked.connect(self.beenden)
        self.Beenden_Knopf.move(100,125)
    #Methode, die Fenster versteckt
    def beenden(self):
        self.hide()
#Benachrichtigung, die angezeigt wird, nachdem alle Texte ein Thema bekommen haben
class Informationsfenster_B(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(350, 200, 300, 200) #Größe & Position des Fensters
        self.setWindowTitle("Informationsfenster")
        self.setUpInfoFenster() #siehe unten
    def setUpInfoFenster(self):
        self.Info_Label_a = QLabel("Jedem Text wurde ein ", self)
        self.Info_Label_a.setFont(QFont("Arial", 15))
        self.Info_Label_a.move(15, 15)
        self.Info_Label_b = QLabel("Thema zugeordnet.", self)
        self.Info_Label_b.setFont(QFont("Arial", 15))
        self.Info_Label_b.move(15, 40)
        #Knopf, der Fenster schließt
        self.Beenden_Knopf = QPushButton("Schließen", self)
        self.Beenden_Knopf.setFont(QFont("Arial", 16))
        self.Beenden_Knopf.clicked.connect(self.beenden)
        self.Beenden_Knopf.move(100, 125)
    #Methode, die Fenster versteckt
    def beenden(self):
        self.hide()
#Benachrichtung nach Löschen/Zurücksetzen der Daten
class Informationsfenster_C(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(350, 200, 300, 200) #Größe & Position des Fensters
        self.setWindowTitle("Informationsfenster")
        self.setUpInfoFenster() #siehe unten
    def setUpInfoFenster(self):
        self.Info_Label_a = QLabel("Die Daten sind zurückgesetzt", self)
        self.Info_Label_a.setFont(QFont("Arial", 15))
        self.Info_Label_a.move(15, 15)
        self.Info_Label_b = QLabel("worden.", self)
        self.Info_Label_b.setFont(QFont("Arial", 15))
        self.Info_Label_b.move(15, 40)
        #Knopf, der Fesnter schließt
        self.Beenden_Knopf = QPushButton("Schließen", self)
        self.Beenden_Knopf.setFont(QFont("Arial", 16))
        self.Beenden_Knopf.clicked.connect(self.beenden)
        self.Beenden_Knopf.move(100, 125)
    #Methode, die Fenster versteckt
    def beenden(self):
        self.hide()

#Fenster für Mitwirkende an der Entwicklung
class Mitwirkendenfenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position
        self.setWindowTitle("Mitwirkende") #Bezeichnung
        self.setUpMitWirkFenster() #siehe unten
    def setUpMitWirkFenster(self):
        #unten Labels
        #zeigt 'Mitwirkende' an
        self.Anzeige_MitWirk_Label = QLabel("Mitwirkende", self)
        self.Anzeige_MitWirk_Label.setFont(QFont("Arial", 32))
        self.Anzeige_MitWirk_Label.move(325, 30)
        #zeigt Projektleiter an
        self.Projekt_Leiter_Label = QLabel("Mein herzlicher Dank an alle Mitwirkenden,\n die aus Datenschutzgründen nicht genannt werden.", self)
        self.Projekt_Leiter_Label.setFont(QFont("Arial", 16))
        self.Projekt_Leiter_Label.move(20, 100)
        #zeigt Ausführer an
        self.Ausfuehrung_Label = QLabel("Ausführung mit: Python 3.12.10", self)
        self.Ausfuehrung_Label.setFont(QFont("Arial", 16))
        self.Ausfuehrung_Label.move(20, 280)
        #zeigt GUI Biblitothek an
        self.GUI_Label =QLabel("GUI erstellt mit: PyQt6", self)
        self.GUI_Label.setFont(QFont("Arial", 16))
        self.GUI_Label.move(20, 310)
        #Bild
        self.MitWirk_Bild()
        #Bild
        self.Python_Bild()
        #Knopf, um zum Menu zurückzukehren
        self.Beenden_Knopf_Bild()
    #Methode, die Bild erstellt
    def MitWirk_Bild(self):
        image = "Mitwirkende.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(55, 44)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(565, 25)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die Bild erstellt
    def Python_Bild(self):
        image = "Python-Logo.PNG"
        try:
            with open(image):
                image_Label = QLabel(self)
                pixmap = QPixmap(image).scaled(150, 150)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                image_Label.setPixmap(rotated_pixmap)
                image_Label.move(400, 325)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
    #Methode, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Beenden_Knopf_Bild(self):
        image = "Menü.PNG"
        try:
            with open(image):
                Beenden_Knopf = QPushButton(self)
                Beenden_Knopf.clicked.connect(self.beenden)
                Beenden_Knopf.move(400, 525)
                Bild = QIcon(image)
                Beenden_Knopf.setIcon(Bild)
                Beenden_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Beenden_Knopf = QPushButton("Menü", self)
            Beenden_Knopf.setFont(QFont("Arial", 16))
            Beenden_Knopf.clicked.connect(self.beenden)
            Beenden_Knopf.move(400, 525)
    #Methode, die Fenster versteckt
    def beenden(self):
        MenuFenster.show()
        self.hide()

#Fenster, das das System erklärt
class Erklaerfenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fesnters
        self.setWindowTitle("Erklärung") #Bezeichnung
        self.setUpErklaerungMenu() #siehe unten
    def setUpErklaerungMenu(self):
        self.Text_Label = QLabel("Wähle ein Thema aus, über das du etwas erfahren willst.", self)
        self.Text_Label.setFont(QFont("Arial", 18))
        self.Text_Label.move(150, 15)
        self.SLM_Knopf = QPushButton("SSLM", self)
        self.SLM_Knopf.setFont(QFont("Arial", 16))
        self.SLM_Knopf.clicked.connect(self.SSLM)
        self.SLM_Knopf.move(100, 250)
        self.Gedaechtnis_Knopf = QPushButton("Gedächtnis", self)
        self.Gedaechtnis_Knopf.setFont(QFont("Arial", 16))
        self.Gedaechtnis_Knopf.clicked.connect(self.Gedaechtnis)
        self.Gedaechtnis_Knopf.move(350, 250)
        self.PyQt6_Knopf = QPushButton("GUI", self)
        self.PyQt6_Knopf.setFont(QFont("Arial", 16))
        self.PyQt6_Knopf.clicked.connect(self.GUI)
        self.PyQt6_Knopf.move(600, 250)
        self.Beenden_Knopf_Bild()
    #Methode, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Beenden_Knopf_Bild(self):
        image = "Menü.PNG"
        try:
            with open(image):
                Beenden_Knopf = QPushButton(self)
                Beenden_Knopf.clicked.connect(self.beenden)
                Beenden_Knopf.move(400, 525)
                Bild = QIcon(image)
                Beenden_Knopf.setIcon(Bild)
                Beenden_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            Beenden_Knopf = QPushButton("Menü", self)
            Beenden_Knopf.setFont(QFont("Arial", 16))
            Beenden_Knopf.clicked.connect(self.beenden)
            Beenden_Knopf.move(400, 525)
    def SSLM(self):
        SLM_Fenster.show()
        self.hide()
    def GUI(self):
        PyQt6Fenster.show()
        self.hide()
    def Gedaechtnis(self):
        GedaechtnisFenster.show()
        self.hide()
    #Methode, die Fenster versteckt
    def beenden(self):
        MenuFenster.show()
        self.hide()

class SLM_Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 920, 600) #Größe & Position des Fesnters
        self.setWindowTitle("Super Surface Language Model") #Bezeichnung
        self.setUpErklaerungSLM() #siehe unten
    def setUpErklaerungSLM(self):
        self.Titel_Label = QLabel("Erklärung Algorithmus", self)
        self.Titel_Label.setFont(QFont("Arial", 32))
        self.Titel_Label.move(250, 15)
        self.Titel_SLM_Label = QLabel("Super Surface Language Model", self)
        self.Titel_SLM_Label.setFont(QFont("Arial", 18))
        self.Titel_SLM_Label.move(15, 85)
        text = "Die Bezeichnung & das Verfahren des Super Surface Language Models SSLM wurde 2025/2026 von "
        text += "'EnnStein' entwickelt. Allgemein funktioniert das SSLM als Suchmaschine, die einen Begriff "
        text += "vom Nutzer anfordert und anschließend in der Datenbank nach Elementen sucht, in denen "
        text += "dieser Suchbegriff ebenfalls vorkommt. Dies geschieht über die 'for'-Schleife, die ihre Anweisungen "
        text += "für jedes Element x einer Liste durchführt. In diesem Fall sind die Elemente Objekte der Klasse "
        text += "'Text' und die Prüfung bezieht sich auf die Eigenschaft 'Text' der einzelnen Objekte. Um einen "
        text += "Suchbegriff, der i.d.R. kürzer ist als der 'Text', mit diesem zu vergleichen, erstellt das Programm "
        text += "intern Ausszüge. Das Verfahren kann man sich so vorstellen, als würde man sich eine Schablone "
        text += "basteln, durch die man genauso viele Buchstaben sehen kann, wie der Suchbegriff lang ist. Dann "
        text += "geht man den ganzen Text durch und anschließend nimmt man sich den nächsten vor. Für jeden "
        text += "Auszug führt der Ordinateur einen Vergleich durch. Sollte es einen Treffer geben, so wird ein "
        text += "Zähler vergrößert, der verwendet wird, um bei keinem Treffer Meldung zu machen, dass es keinen "
        text += "Treffer gibt, außerdem wird geprüft, zu welchem Thema der Text zugeordnet wurde. Abhängig "
        text += "davon erfolgt die Antwort. \n"
        text += "Das ganze Kunstwerk besteht also nur aus Objekten, Schleifen und Bedingungen."
        self.Erklaerung_Label = QLabel(text, self)
        self.Erklaerung_Label.setFont(QFont("Arial", 15))
        self.Erklaerung_Label.setWordWrap(True)
        self.Erklaerung_Label.move(15, 120)
        #Knopf, um zurück zu gehen
        self.Zurueck_Knopf_Bild()
    #Methode, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Zurueck_Knopf_Bild(self):
        image = "Zurück.PNG"
        try:
            with open(image):
                Zurueck_Knopf = QPushButton(self)
                Zurueck_Knopf.clicked.connect(self.zurueck)
                Zurueck_Knopf.move(400, 525)
                Bild = QIcon(image)
                Zurueck_Knopf.setIcon(Bild)
                Zurueck_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            self.Zurueck_Knopf = QPushButton("zurück", self)
            self.Zurueck_Knopf.setFont(QFont("Arial", 16))
            self.Zurueck_Knopf.clicked.connect(self.zurueck)
            self.Zurueck_Knopf.move(400, 500)
    def zurueck(self):
        ErklaerFenster.show()
        self.hide()

class Gedaechtnisfenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fesnters
        self.setWindowTitle("Gedächtnis") #Bezeichnung
        self.setUpErklaerungGedaechtnis() #siehe unten
    def setUpErklaerungGedaechtnis(self):
        self.Titel_Label = QLabel("Erklärung Algorithmus", self)
        self.Titel_Label.setFont(QFont("Arial", 32))
        self.Titel_Label.move(250, 15)
        self.Titel_Gedaechtnis_Label = QLabel("Das Gedächtnis", self)
        self.Titel_Gedaechtnis_Label.setFont(QFont("Arial", 18))
        self.Titel_Gedaechtnis_Label.move(15, 85)
        self.Text_Label_a = QLabel("Das Gedächtnis wird über Eigenschaften der Objekte erzeugt. Alle Objekte, die hierfür verwendet", self)
        self.Text_Label_a.setFont(QFont("Arial", 15))
        self.Text_Label_a.move(15, 120)
        self.Text_Label_b = QLabel("werden, gehören zur Klasse 'Text'. Sie haben für jedes Thema eine Eigenschaft, die drei Werte", self)
        self.Text_Label_b.setFont(QFont("Arial", 15))
        self.Text_Label_b.move(15, 145)
        self.Text_Label_c = QLabel("haben kann (unbekannt, trifft zu & trifft nicht zu). Das Setzen dieser Werte, wobei 'unbekannt'", self)
        self.Text_Label_c.setFont(QFont("Arial", 15))
        self.Text_Label_c.move(15, 170)
        self.Text_Label_d = QLabel("der Standard ist, erfolgt im Anlernen. Auf diese Eigenschaften wird in der Suche durch das SSLM", self)
        self.Text_Label_d.setFont(QFont("Arial", 15))
        self.Text_Label_d.move(15, 195)
        self.Text_Label_e = QLabel("zugegriffen & sind letztlich für das Ergebnis verantwortlich.", self)
        self.Text_Label_e.setFont(QFont("Arial", 15))
        self.Text_Label_e.move(15, 220)
        #Knopf, mit dem man zur Übersicht der Erklärungen zurückkehrt
        self.Zurueck_Knopf_Bild()
    #Methode, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Zurueck_Knopf_Bild(self):
        image = "Zurück.PNG"
        try:
            with open(image):
                Zurueck_Knopf = QPushButton(self)
                Zurueck_Knopf.clicked.connect(self.zurueck)
                Zurueck_Knopf.move(400, 525)
                Bild = QIcon(image)
                Zurueck_Knopf.setIcon(Bild)
                Zurueck_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            self.Zurueck_Knopf = QPushButton("zurück", self)
            self.Zurueck_Knopf.setFont(QFont("Arial", 16))
            self.Zurueck_Knopf.clicked.connect(self.zurueck)
            self.Zurueck_Knopf.move(400, 500)
    def zurueck(self):
        ErklaerFenster.show()
        self.hide()

class PyQt6fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(100, 100, 900, 600) #Größe & Position des Fesnters
        self.setWindowTitle("Graphical User Interface") #Bezeichnung
        self.setUpErklaerungGUI() #siehe unten
    def setUpErklaerungGUI(self):
        self.Titel_Label = QLabel("Erklärung Algorithmus", self)
        self.Titel_Label.setFont(QFont("Arial", 32))
        self.Titel_Label.move(250, 15)
        self.Titel_GUI_Label = QLabel("Das Graphical User Interface", self)
        self.Titel_GUI_Label.setFont(QFont("Arial", 18))
        self.Titel_GUI_Label.move(15, 85)
        self.Text_Label_a = QLabel("Um die Benutzeroberfläche dieses Programms zu erstellen, habe ich PyQt6 verwendet. Diese", self)
        self.Text_Label_a.setFont(QFont("Arial", 15))
        self.Text_Label_a.move(15, 120)
        self.Text_Label_b = QLabel("Bibliothek enthält eine große Sammlung an Klassen. Die hier am häufigsten verwendeten sind", self)
        self.Text_Label_b.setFont(QFont("Arial", 15))
        self.Text_Label_b.move(15, 145)
        self.Text_Label_c = QLabel("QWidget, QLabel, QPushButton, QPixmap, QIcon und QFont. Alle Fenster sind Erben der", self)
        self.Text_Label_c.setFont(QFont("Arial", 15))
        self.Text_Label_c.move(15, 170)
        self.Text_Label_d = QLabel("QWidget-Klasse. Per QLabel werden Flächen in den Fenstern platizert, die Texte oder Bilder", self)
        self.Text_Label_d.setFont(QFont("Arial", 15))
        self.Text_Label_d.move(15, 195)
        self.Text_Label_e = QLabel("enthaltenkönnen. Bilder werden durch eine Pixmap eingesetzt. QPushButtons sind Elemente,", self)
        self.Text_Label_e.setFont(QFont("Arial", 15))
        self.Text_Label_e.move(15, 220)
        self.Text_Label_f = QLabel("die eine Funktion/Methode ausführen, falls man mit der Maus auf sie drückt. Auch hier", self)
        self.Text_Label_f.setFont(QFont("Arial", 15))
        self.Text_Label_f.move(15, 245)
        self.Text_Label_g = QLabel("können Bilder verwendet werden; aber diese werden über QIcon eingesetzt. Über QFont kann", self)
        self.Text_Label_g.setFont(QFont("Arial", 15))
        self.Text_Label_g.move(15, 270)
        self.Text_Label_h = QLabel("die Schriftart & Schriftgröße angepasst werden. Einmal wird auch die Klasse QLineEdit", self)
        self.Text_Label_h.setFont(QFont("Arial", 15))
        self.Text_Label_h.move(15, 295)
        self.Text_Label_i = QLabel("(in der Ausgabe/Suchmaschine) verwendet. Es bildet eine Zeile, in der der Benutzer frei", self)
        self.Text_Label_i.setFont(QFont("Arial", 15))
        self.Text_Label_i.move(15, 320)
        self.Text_Label_j = QLabel("Eingaben tätigen kann. Über eine Methode kann die Eingabe abgerufen werden.", self)
        self.Text_Label_j.setFont(QFont("Arial", 15))
        self.Text_Label_j.move(15, 345)
        #Knopf, mit dem man zur Übersicht der Erklärungen zurückkehrt
        self.Zurueck_Knopf_Bild()
    #Methode, die bebilderten Knopf erstellt, bzw. falls das Bild nicht gefunden wird, einen beschrifteten Knopf
    def Zurueck_Knopf_Bild(self):
        image = "Zurück.PNG"
        try:
            with open(image):
                Zurueck_Knopf = QPushButton(self)
                Zurueck_Knopf.clicked.connect(self.zurueck)
                Zurueck_Knopf.move(400, 525)
                Bild = QIcon(image)
                Zurueck_Knopf.setIcon(Bild)
                Zurueck_Knopf.setIconSize(QSize(50, 50))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            self.Zurueck_Knopf = QPushButton("zurück", self)
            self.Zurueck_Knopf.setFont(QFont("Arial", 16))
            self.Zurueck_Knopf.clicked.connect(self.zurueck)
            self.Zurueck_Knopf.move(400, 500)
    def zurueck(self):
        ErklaerFenster.show()
        self.hide()

#Klassen für Lern-Mechanik (aus Original)
class Text:
    def __init__(self):
        self.Kennung = ""
        self.Text = ""
        self.Katze = 0
        self.Hund = 0
        self.Auto = 0
        #die Eigenschaften self.Katze/Hund/Auto speichern, was bereits über der Beziehung des Objekts zum Thema bekannt ist
        #Codierung:
        #0 = unbekannt ; immer zu Beginn
        #1 = richtig
        #2 = falsch
        Sammlung.append(self)
    def setText(self, text):
        self.Text = text
    def setKennung(self, kennung):
        self.Kennung = kennung

#Funktion, die Großbuchstaben in Kleinbuchstaben umwandelt
def grossKlein(Text):
    Grossbuchstaben = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Kleinbuchstaben = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Ausgabe = ""
    for x in Text:
        if x in Grossbuchstaben:
            Ausgabe += Kleinbuchstaben[Grossbuchstaben.index(x)]
        else:
            Ausgabe += x
    return Ausgabe

#notwendige Liste
Sammlung = [] #enthält alle Texte

#Erstellung Text-Instanzen
#erst Erstellung der Instanz, dass Anpassung der Eigenschaft Text
Text_a = Text()
Text_a.setText("Katzen sind putzig; sie tun es sehr oft.")
Text_a.setKennung("A")
Text_b = Text()
Text_b.setText("Hunde sind die besten Freunde des Menschen.")
Text_b.setKennung("B")
Text_c = Text()
Text_c.setText("Die Boliden der Auto Union und von Daimler-Benz wurden Silberpfeile genannt.")
Text_c.setKennung("C")
Text_d = Text()
Text_d.setText("Bei vielen Katzen kann man ein 'M' auf der Stirn erkennen.")
Text_d.setKennung("D")
Text_e = Text()
Text_e.setText("Das Buch 'Mein liebes Frauchen' wird aus Sicht eines Hundes erzählt.")
Text_e.setKennung("E")
Text_f = Text()
Text_f.setText("Shelby modifizierte AC Cobras und wurde dadurch bekannt.")
Text_f.setKennung("F")
Füller = Text()
Füller.setText("")

#eigentliche Anwendung/Ausführung
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #unten Erstellung von Instanzen der oben definierten Fenster
    StartFenster = Startfenster()
    MenuFenster = Menufenster()
    InfoFensterA = Informationsfenster_A()
    InfoFensterB = Informationsfenster_B()
    InfoFensterC = Informationsfenster_C()
    AnlernFenster = Lernfenster()
    AusgabeFenster = Ausgabefenster()
    DatenFenster = Datenfenster()
    MitWirkFenster = Mitwirkendenfenster()
    ErklaerFenster = Erklaerfenster()
    SLM_Fenster = SLM_Fenster()
    GedaechtnisFenster = Gedaechtnisfenster()
    PyQt6Fenster = PyQt6fenster()
    sys.exit(app.exec()) #regelt das Schließen von Fenstern