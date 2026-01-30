import frappe

def execute():
    steps = frappe.get_all(
        "Onboarding Step",
        fields=["name", "video_url", "intro_video_url"]
    )

    for step in steps:
        doc = frappe.get_doc("Onboarding Step", step.name)
        changed = False

        if doc.video_url:
            doc.video_url = None
            changed = True

        if hasattr(doc, "intro_video_url") and doc.intro_video_url:
            doc.intro_video_url = None
            changed = True

        if changed:
            doc.save(ignore_permissions=True)

    frappe.db.commit()
