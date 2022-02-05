import os

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

from settings import client_name, provider_name, provider_note, provider_city, provider_zip, provider_file_logo, provider_bkaccount, provider_country, creator_name, title, descriptions

# choose english as language
os.environ["INVOICE_LANG"] = "en"

client = Client(client_name)
provider = Provider(provider_name, note=provider_note, city=provider_city, zip_code=provider_zip, logo_filename=provider_file_logo, country=provider_country, bank_account=provider_bkaccount)
creator = Creator(creator_name)
invoice_title = title + '-' + client_name + '.pdf'

invoice = Invoice(client, provider, creator)
invoice.paytype= None
invoice.currency = u'$'
invoice.title= title
invoice.currency_locale = 'en_US.UTF-8'

#CREATE BILLABLE ITEMS
for x in descriptions:
    invoice.add_item(Item(x[1], x[2], description=x[0]))
pdf = SimpleInvoice(invoice)
pdf.gen(invoice_title, generate_qr_code=True)