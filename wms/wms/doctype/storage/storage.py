# -*- coding: utf-8 -*-
# Copyright (c) 2019, 9T9IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint
from frappe.utils.nestedset import NestedSet


class Storage(NestedSet):
	nsm_parent_field = 'parent_storage'

	def autoname(self):
		if self.company:
			suffix = ' - ' + frappe.get_cached_value('Company', self.company, 'abbr')
			if not self.storage_name.endswith(suffix):
				self.name = self.storage_name + suffix
		else:
			self.name = self.storage_name


@frappe.whitelist()
def get_children(doctype, parent=None, company=None, is_root=False):
	parent = "" if is_root else parent
	fields = ['name as value', 'is_group as expandable']
	filters = [
		['ifnull(`parent_storage`, "")', '=', parent],
		['company', 'in', (company, None, '')]

	]
	return frappe.get_list(doctype, fields=fields, filters=filters, order_by='name')


@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args
	args = make_tree_args(**frappe.form_dict)

	if cint(args.is_root):
		args.parent_storage = None

	frappe.get_doc(args).insert()
