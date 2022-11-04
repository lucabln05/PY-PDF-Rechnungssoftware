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
    recipient_company.company_name = "Translotico GmbH"

    recipient_company.name = "Frau Bergmann"

    recipient_company.street = "Hauptstrasse 1"

    recipient_company.city = "82377 Murnau"