import frappe

def execute():
    steps = frappe.get_all(
        "Onboarding Step",
        fields=["name"]
    )

    for step in steps:
        doc = frappe.get_doc("Onboarding Step", step.name)

        changed = False

        for field in ["video_url", "youtube_video_id"]:
            if hasattr(doc, field) and doc.get(field):
                doc.set(field, None)
                changed = True

        if changed:
            doc.save(ignore_permissions=True)

    frappe.db.commit()
