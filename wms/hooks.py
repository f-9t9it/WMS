# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "wms"
app_title = "Wms"
app_publisher = "9T9IT"
app_description = "Warehouse Management App for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Pick List-wms_scan_barcode"
                ]
            ]
        ]
    }
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wms/css/wms.css"
# app_include_js = "/assets/wms/js/wms.js"

# include js, css files in header of web template
# web_include_css = "/assets/wms/css/wms.css"
# web_include_js = "/assets/wms/js/wms.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Pick List": "public/js/pick_list.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "wms.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "wms.install.before_install"
# after_install = "wms.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wms.tasks.all"
# 	],
# 	"daily": [
# 		"wms.tasks.daily"
# 	],
# 	"hourly": [
# 		"wms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wms.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wms.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wms.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wms.event.get_events"
# }

