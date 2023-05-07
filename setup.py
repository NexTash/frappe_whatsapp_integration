from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_whatsapp_integration/__init__.py
from frappe_whatsapp_integration import __version__ as version

setup(
	name="frappe_whatsapp_integration",
	version=version,
	description="Open Source Whatsapp integration app for open source framework Frappe",
	author="NexTash (SMC-PVT) Ltd",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
