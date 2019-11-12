frappe.treeview_settings['Storage'] = {
    get_tree_nodes: 'wms.wms.doctype.storage.storage.get_children',
    add_tree_node: 'wms.wms.doctype.storage.storage.add_node',
    get_tree_root: false,
    root_label: "Storages",
    filters: [
        {
            label: __('Company'),
            fieldname: 'company',
            fieldtype: 'Select',
            options: erpnext.utils.get_tree_options('company'),
            default: erpnext.utils.get_tree_default('company')
        }
    ],
    fields: [
        {fieldtype: 'Data', fieldname: 'storage_name', label: __('New Storage'), reqd: true},
        {fieldtype: 'Check', fieldname: 'is_group', label: __('Is Group')}
    ],
    ignore_fields: ["parent_storage"],
    onload: function(treeview) {
        treeview.page.add_inner_button(__('Layout'), function() {

        }, __('Create'));
    }
};
