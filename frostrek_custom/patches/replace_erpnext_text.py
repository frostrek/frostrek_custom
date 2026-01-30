import frappe

def execute():
    steps = frappe.get_all(
        "Onboarding Step",
        fields=["name", "title", "description"]
    )

    for step in steps:
        doc = frappe.get_doc("Onboarding Step", step.name)
        changed = False

        if doc.title and "ERPNext" in doc.title:
            doc.title = doc.title.replace("ERPNext", "FrostERP")
            changed = True

        if doc.description and "ERPNext" in doc.description:
            doc.description = doc.description.replace("ERPNext", "FrostERP")
            changed = True

        if changed:
            doc.save(ignore_permissions=True)

    frappe.db.commit()
