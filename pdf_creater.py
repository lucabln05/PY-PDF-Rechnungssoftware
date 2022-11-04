#https://www.youtube.com/watch?v=q70xzDG6nls
from fpdf import FPDF   # import FPDF module from fpdf library

class PDF(FPDF):        # create a class PDF which inherits from FPDF
    def header(self):   # create a method header
        self.image('logo.png', 10, 5, 21)    # add an image to the header

        self.set_font('helvetica', '', 21)     # set the font, style and size
        self.cell(80)   # create a cell
        self.cell(0, 14, 'Firma GmbH', 'C')   # add a title to the cell
        self.ln(20)     # move the cursor to the next line

        self.set_font('helvetica', '', 10)   # set the font, style and size
        self.set_text_color(80,80,80)  # set the text color to gray
        self.cell(10, 10, 'Firma GmbH -- Haydnstrasse 15 -- 87236 Erbedingen', ln=True)  # add a cell with a company address, name and street

        self.set_font('helvetica', '', 11)   # set the font, style and size
        self.set_text_color(0,0,0)  # set the text color to black
        self.cell(10, 5, 'Translotico GmbH', ln=True)  # company name
        self.cell(10, 5, 'Frau Bergmann', ln=True)  # person name
        self.cell(10, 5, 'Rosenstrasse 95', ln=True)  # street name
        self.cell(10, 5, '81318 Muenchen', ln=True)  # zip code and city
        self.ln(20)     # move the cursor to the next line
        
        self.set_font('helvetica', '', 8)   # set the font, style and size
        self.set_text_color(80,80,80)  # set the text color to blue
        self.cell(10, 3.5, 'Rechnungsnummer: 123456', ln=True)   # add a cell with the invoice number
        self.cell(10, 3.5, 'Rechnungsdatum: 12.02.2019', ln=True)   # add a cell with the invoice date
        self.cell(10, 3.5, 'Kundennummer: 123456', ln=True)   # add a cell with the customer number
        self.ln(15)

        self.set_font('helvetica', 'B', 20)     # set the font, style and size
        self.set_text_color(0,0,0)  # set the text color to black
        self.cell(10, 10, 'Rechnung', ln=True)   # add a cell with the title


        self.set_font('helvetica', '', 10)   # set the font, style and size
        self.set_text_color(0,0,0)  # set the text color to black
        self.cell(10, 5, 'Vielen Danke fuer Ihren Auftrag. Wir berechnen Ihnen folgende Lieferung bzw. Leistung:', ln=True)   # add a cell with the title
        self.ln(10)

        #tabellen ueberschrift
        self.set_font('helvetica', '', 10)
        self.set_text_color(0,0,0)
        self.cell(58, 5, 'Artikel')
        self.cell(58, 5, 'Menge')
        self.cell(58, 5, 'Preis')
        self.cell(58, 5, 'Gesamt')
        self.ln(10)

        # userabfrage fuer artikel anzahl und artikel bezeichnung und preis

        row_number = int(input("Wie viele Artikel?: "))  
        gesamt_preis = 0   
        for i in range(row_number):
                # tabellen spalten
                artikel_name = input("Artikelname: ")
                artikel_menge = int(input("Artikelmenge: "))
                artikel_einzelpreis = float(input("Artikelpreis: "))
                artikel_gesamtpreis = artikel_menge * artikel_einzelpreis
                self.set_font('helvetica', '', 8)
                self.set_text_color(80,80,80)
                self.cell(58, 3.5, f'{artikel_name}' )
                self.cell(58, 3.5, f'{artikel_menge}')
                self.cell(58, 3.5, f'{artikel_einzelpreis}')
                self.cell(58, 3.5, f'{round(artikel_gesamtpreis, 2)}')    # round the price to 2 decimal places
                self.ln(10)
                gesamt_preis += artikel_gesamtpreis 
    
        # rechnungsbetrag mit 19% MwSt
        self.set_text_color(0,0,0)
        self.cell(58, 3.5, '')
        self.cell(58, 3.5, '')
        self.cell(58, 3.5, 'Summe netto')
        self.cell(15, 3.5, f'{round(gesamt_preis,2)}')  # round the price to 2 decimal places
        self.ln(5)

        betrag_mwst = gesamt_preis * 0.19       # calculate the amount of VAT

        self.cell(58, 3.5, '')
        self.cell(58, 3.5, '')
        self.cell(58, 3.5, 'MwSt. 19%')
        self.cell(15, 3.5, f'{round(betrag_mwst, 2)}')  # round the price to 2 decimal places
        self.ln(5)


        self.set_font('helvetica', 'B', 10)
        self.set_text_color(0,0,0)
        self.cell(58, 3.5, '')
        self.cell(58, 3.5, '')
        self.cell(58, 3.5, 'Gesamtsumme', 'B')
        self.cell(15, 3.5, f'{round(gesamt_preis, 2) + round(betrag_mwst, 2)}', 'B')
        self.ln(30)




        
        self.set_font('helvetica', '', 10)
        self.cell(58, 5, 'Bankverbindung', 'B', ln=True)
        self.ln(2)
        self.cell(58, 4.5, 'IBAN: ', ln=True)
        self.cell(58, 4.5, 'BIC: ', ln=True)
        self.ln(10)
        
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(0,0,0)
        self.cell(10, 5, 'Zahlbar nach Erhalt der Rechnung, innerhalb von 30 Tagen.', ln=True)
        self.cell(10, 5, 'Wir bedanken uns für Ihren Auftrag und freuen uns auf die weitere Zusammenarbeit,')


    

    def footer(self):   # create a method footer
        # company address, name and street in the footer
        self.set_y(-15)     # set the cursor to the bottom of the page
        self.set_font('helvetica', '', 8)   # set the font, style and size
        self.set_text_color(80,80,80)  # set the text color to blue
        self.cell(10, 3.5, 'Firma GmbH', ln=True)  # add a cell with a company address, name and street
        self.cell(10, 3.5, 'Haydnstrasse 15', ln=True)  # add a cell with a company address, name and street
        self.cell(10, 3.5, '87236 Erbedingen', ln=True)  # add a cell with a company address, name and street

    




            



#create FPDF object
pdf = PDF('P','mm', 'A4')  # P = Portrait, mm = millimeter, A4 = size of the page

        


#Add a page
pdf.add_page()

# save the pdf with name .pdf
pdf.output('tuto1.pdf', 'F')  # F = save the file in the current directory

