def pdf_creator(): 
    from fpdf import FPDF   # import FPDF module from fpdf library
    from Connectors.pdf_connector import load_default_company, recipient_company, table_script
    from datetime import date



    load_default_company()  # load default company data 
    recipient_company()     # set recipient data

    class PDF(FPDF):        # create a class PDF which inherits from FPDF
        def header(self):   # create a method header
            self.image('Config/logo.png', 10, 5, 21)    # add an image to the header

            self.set_font('helvetica', '', 21)     # set the font, style and size
            self.cell(80)   # create a cell
            self.cell(0, 14, load_default_company.name, 'C')   # add a title to the cell
            self.ln(20)     # move the cursor to the next line

            self.set_font('helvetica', '', 10)   # set the font, style and size
            self.set_text_color(80,80,80)  # set the text color to gray
            self.cell(10, 10, f'{load_default_company.name} -- {load_default_company.street} -- {load_default_company.city }', ln=True)  # add a cell with a company address, name and street

            self.set_font('helvetica', '', 11)   # set the font, style and size
            self.set_text_color(0,0,0)  # set the text color to black
            self.cell(10, 5, f'{recipient_company.company_name}', ln=True)  # company name
            self.cell(10, 5, f'{recipient_company.name}', ln=True)  # person name
            self.cell(10, 5, f'{recipient_company.street}', ln=True)  # street name
            self.cell(10, 5, f'{recipient_company.city}', ln=True)  # zip code and city
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

            
            table_script(self)  # call the table_script function# Path: pdf_creater.py # this script create the tabe in the pdf file
            
            self.set_font('helvetica', '', 10)
            self.cell(58, 5, 'Bankverbindung', 'B', ln=True)
            self.ln(2)
            self.cell(58, 4.5, f'IBAN: {load_default_company.iban} ', ln=True)
            self.cell(58, 4.5, f'BIC: {load_default_company.bic}', ln=True)
            self.ln(10)
            
            self.set_font('helvetica', 'B', 10)
            self.set_text_color(0,0,0)
            self.cell(10, 5, 'Zahlbar nach Erhalt der Rechnung, innerhalb von 30 Tagen.', ln=True)
            self.cell(10, 5, 'Wir bedanken uns für Ihren Auftrag und freuen uns auf die weitere Zusammenarbeit.')


        

        def footer(self):   # create a method footer
            # company address, name and street in the footer
            self.set_y(-15)     # set the cursor to the bottom of the page
            self.set_font('helvetica', '', 8)   # set the font, style and size
            self.set_text_color(80,80,80)  # set the text color to blue
            self.cell(10, 3.5, load_default_company.name, ln=True)  # add a cell with a company address, name and street
            self.cell(10, 3.5, load_default_company.street, ln=True)  # add a cell with a company address, name and street
            self.cell(10, 3.5, load_default_company.city, ln=True)  # add a cell with a company address, name and street
            self.cell(10, 3.5, f'Datum: {date.today()}', ln=True)  # add a cell with the current date

        

    #create FPDF object
    pdf = PDF('P','mm', 'A4')  # P = Portrait, mm = millimeter, A4 = size of the page

            


    #Add a page
    pdf.add_page() 

    # save the pdf with name .pdf
    pdf.output(f'{date.today()}{recipient_company.company_name}.pdf', 'F')  # F = save the file in the current directory
