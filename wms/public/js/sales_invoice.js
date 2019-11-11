frappe.ui.form.on("Sales Invoice", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(
                __('Pick List'),
                () => frm.trigger('create_pick_list'),
                __('Create')
            );
        }
    },
    create_pick_list: function(frm) {
        frappe.model.open_mapped_doc({
            frm,
            method: "wms.custom.sales_invoice.create_pick_list"
        });
    }
});
