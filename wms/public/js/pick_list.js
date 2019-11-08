const _picked = [];

frappe.ui.form.on("Pick List", {
    wms_scan_barcode: async function(frm) {
        if (!frm.doc.wms_scan_barcode) {
            return;
        }

        function set_description(msg) {
            frm.fields_dict['wms_scan_barcode'].set_new_description(__(msg));
        }

        function set_value(value) {
            frm.set_value('wms_scan_barcode', value);
        }

        const { wms_scan_barcode: search_value, locations: items } = frm.doc;
        const { message: data } = await frappe.call({
            method: "erpnext.selling.page.point_of_sale.point_of_sale.search_serial_or_batch_or_barcode_number",
            args: { search_value }
        });

        if (!data || Object.keys(data).length === 0) {
            set_description('Cannot find Item with this barcode');
            return;
        }

        const row = items.find(({ item_code, batch_no }) => {
            if (batch_no) {
                return item_code == data.item_code && batch_no == data.batch_no;
            }
            return item_code === data.item_code;
        });

        set_value('');
        set_description('');

        if (!row.item_code) {
            frappe.throw(__("Item not found for Pick List"));
        }

        const { qty } = await _confirm_dialog(row.qty);
        frappe.model.set_value(row.doctype, row.name, 'picked_qty', qty);
        frm.fields_dict['wms_scan_barcode'].$input.focus();

        if (!_picked.includes(row.name)) {
            _picked.push(row.name);
        }

        if (_check_all_picked(frm.doc.locations)) {
            const save = await _submit_dialog();
            save && frm.savesubmit();
        }
    }
});

function _confirm_dialog(qty) {
    return new Promise((resolve, reject) => {
        const dialog = new frappe.ui.Dialog({
            title: 'Modify Item Picked',
            fields: [
                {fieldname: 'qty', fieldtype: 'Float', label: 'Qty', default: qty || 0},
            ],
            primary_action_label: 'Confirm',
            primary_action: function (values) {
                resolve(values);
                dialog.hide();
            }
        });
        dialog.show();
    });
}

function _submit_dialog() {
    return new Promise((resolve, reject) => {
        frappe.confirm(
            __('All Items are picked. Would you like to submit the document?'),
            () => resolve(true),
            () => resolve(false)
        );
    });
}

function _check_all_picked(locations) {
    return locations.every(location => _picked.includes(location.name));
}
