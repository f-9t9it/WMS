import frappe
from frappe.utils import flt
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def create_pick_list(source_name, target_doc=None):
    def update_item_quantity(source, target, source_parent):
        target.qty = flt(source.qty) - flt(source.delivered_qty)
        target.stock_qty = (flt(source.qty) - flt(source.delivered_qty)) * flt(source.conversion_factor)

    doc = get_mapped_doc('Sales Invoice', source_name, {
        'Sales Invoice': {
            'doctype': 'Pick List',
            'validation': {
                'docstatus': ['=', 1]
            }
        },
        'Sales Invoice Item': {
            'doctype': 'Pick List Item',
            'field_map': {
                'parent': 'wms_sales_invoice',
                'name': 'wms_sales_invoice_item'
            },
            'postprocess': update_item_quantity
        }
    }, target_doc)

    doc.purpose = 'Delivery against Sales Invoice'

    return doc
