# -*- coding: utf-8 -*-
# Your code goes below this line

from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
from odoo import api, fields, models, _
import datetime
from odoo.exceptions import UserError


class NSMDeliveryListReport(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, proofLines):

        #customer.parent.zip
        def _kix_code(customer):
            nonkix = customer.zip or customer.parent.zip or ''
            kix = nonkix.replace(" ", "")
            return kix

        def _prepare_data(customer, pLine):
            records = []
            parent = customer.parent_id or customer

            initial = ''
            firstname = ''
            infix = ''
            blank_details = ''
            tital = ''
            last_name = ''
            
            if parent.title:
                tital = parent.title.name.encode('ascii', 'ignore') + " "
            if parent.initials:
                initial = parent.initials.encode('ascii', 'ignore') + " "
            else:
                if parent.firstname:
                    firstname = customer.firstname.encode('ascii', 'ignore') + " "
            if parent.infix:
                infix = customer.infix.encode('ascii', 'ignore') + " "
            if parent.lastname:
                last_name = parent.lastname.encode('ascii', 'ignore') or ''
            blank_details = str(tital) + str(initial) + str(firstname) + str(infix) + str(last_name)

            amount = 0
            if customer.id in pLine.line_id.proof_number_adv_customer.ids:
                amount += pLine.line_id.proof_number_amt_adv_customer
            if pLine.line_id.proof_number_payer_id and pLine.line_id.proof_number_payer_id.id == customer.id:
                amount += pLine.line_id.proof_number_amt_payer

            records.append(str(blank_details)) #customer.parent full name
            records.append(str(customer.gender and customer.gender.encode('ascii', 'ignore') or ''))
            records.append(str(customer.initials and customer.initials.encode('ascii', 'ignore') or ''))
            records.append(str(customer.infix and customer.infix.encode('ascii', 'ignore') or ''))
            records.append(str(customer.lastname and customer.lastname.encode('ascii', 'ignore') or ''))
            records.append(str(customer.street_name and customer.street_name.encode('ascii', 'ignore') or''))
            records.append(str(customer.street2 and customer.street2.encode('ascii', 'ignore') or ''))
            records.append(str(customer.street_number or ''))
            records.append(str(customer.street_number_extension or ''))
            records.append(str(_kix_code(customer) or ''))
            records.append(str(customer.city and customer.city.encode('ascii', 'ignore') or parent.city and parent.city.encode('ascii', 'ignore') or ''))
            records.append(str(customer.country_id and customer.country_id.name.encode('ascii', 'ignore') or parent.country_id and parent.country_id.name.encode('ascii', 'ignore') or ''))
            records.append(amount) #line amount
            records.append(str(pLine.title.name))

            return records

        def _form_data(proofLines):
            row_datas = []
            for pLine in proofLines:
                row_datas.append(_prepare_data(pLine.proof_number_payer, pLine))

            return row_datas

        header = ['Bedrijf', 'Gesl', 'Voorletters', 'Tussenvoegsel', 'Achternaam', 'Straat', 'Straat Extra',
                  'Huisnummer', 'Huisnummer toevoeging', 'Postcode', 'Plaats', 'Land', 'Exemp', 'TITEL']

        row_datas = _form_data(proofLines)

        if row_datas:
            bold_format = workbook.add_format({'bold': True})
            report_name = 'PNDL_{date:%Y-%m-%d %H:%M:%S}'.format(date=datetime.datetime.now())
            sheet = workbook.add_worksheet(report_name[:31])
            for i, title in enumerate(header):
                sheet.write(0, i, title, bold_format)
            for row_index, row in enumerate(row_datas):
                for cell_index, cell_value in enumerate(row):
                    sheet.write(row_index + 1, cell_index, cell_value)
            workbook.close()
        else:
            raise UserError(_('No record found to print!'))

NSMDeliveryListReport('report.report_pndl_delivery_list1.xlsx', 'proof.number.delivery.list')