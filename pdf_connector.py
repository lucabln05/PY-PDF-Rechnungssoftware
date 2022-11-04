from database_connector import *    # get recipient data from database


def load_default_company():
    default_config = open("Config/default_company.txt", "r")
    default_config = default_config.read()
    default_name, default_street, default_city, default_iban, default_bic = default_config.splitlines()

    
    load_default_company.name = default_name        

    load_default_company.street = default_street

    load_default_company.city = default_city

    load_default_company.iban = default_iban

    load_default_company.bic = default_bic




# recipient company data
def recipient_company():

    pdf_input_get()

    recipient_company.company_name = pdf_input_get.company_name

    recipient_company.name = pdf_input_get.name

    recipient_company.street = pdf_input_get.street

    recipient_company.city = pdf_input_get.city




# create the table in the pdf
def table_script(self):
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
        self.cell(15, 3.5, f'{round(round(gesamt_preis, 2) + round(betrag_mwst, 2))}', 'B')
        self.ln(30)


