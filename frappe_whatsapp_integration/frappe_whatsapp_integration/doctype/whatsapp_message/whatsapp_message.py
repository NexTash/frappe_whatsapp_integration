# Copyright (c) 2023, NexTash (SMC-PVT) Ltd and contributors
# For license information, please see license.txt

import frappe
import requests

from frappe.model.document import Document

class WhatsAppMessage(Document):
	def validate(self):
		pass

	@frappe.whitelist()
	def send(self):
		if not self.contact_number:
			frappe.throw("Contact Number is required to send message.")

		wa_settings = frappe.get_doc("WhatsApp Settings", "WhatsApp Settings")

		access_token = wa_settings.get_password("access_token")
		
		api_base = "https://graph.facebook.com/v16.0"
		phone_number_id = wa_settings.get("phone_number_id")

		endpoint = f"{api_base}/{phone_number_id}/messages"
		contact_number = frappe.get_value("WhatsApp Contact", self.contact_number, "contact_number")
		contact_number = format_number(contact_number)
		
		response_data = {
			"messaging_product": "whatsapp",
			"recipient_type": "individual",
			"to": contact_number,
			"type": "TEXT",
			"text": {"preview_url": False, "body": self.message}
		}

		response = requests.post(
			endpoint,
			json=response_data,
			headers={
				"Authorization": "Bearer " + access_token,
				"Content-Type": "application/json",
			},
		)

		if response.ok:
			self.message_id = response.json().get("messages")[0]["id"]
			self.status = "Sent"
			self.save(ignore_permissions=True)
			return response.json()
		else:
			# frappe.throw(response.json().get("error").get("message"))
			return response.json()

def format_number(number):
        """Format number."""
        if number.startswith("+"):
            number = number[1:len(number)]

        return number
