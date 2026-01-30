import frappe

def execute():
    step = frappe.get_all(
        "Onboarding Step",
        filters={"name": "Chart of Accounts"},
        pluck="name"
    )

    if not step:
        return

    doc = frappe.get_doc("Onboarding Step", step[0])
    doc.description = (
        "# Chart of Accounts\n\n"
        "A default chart of accounts is created for each company. "
        "You can customize it to match your business structure "
        "and local compliance requirements."
    )
    doc.save(ignore_permissions=True)
