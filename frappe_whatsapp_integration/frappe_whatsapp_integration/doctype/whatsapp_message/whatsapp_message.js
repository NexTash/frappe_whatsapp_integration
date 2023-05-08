// Copyright (c) 2023, NexTash (SMC-PVT) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('WhatsApp Message', {
	refresh: function(frm) {
		if (!frm.doc.message_id) {
			frm.add_custom_button("Send Message", () => {
				frm.call("send").then((m) => frm.refresh())
			});
		  }
	}
});
