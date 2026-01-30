function removeHelpMenuItems() {
  const removeLabels = [
    "Documentation",
    "User Forum",
    "Frappe School",
    "Report an Issue",
    "About",
    "Keyboard Shortcuts",
    "Frappe Support"
  ];

  document.querySelectorAll(".dropdown-menu a").forEach(el => {
    const text = el.textContent.trim();
    if (removeLabels.includes(text)) {
      el.closest("li")?.remove() || el.remove();
    }
  });
}

// Run after desk loads
frappe.after_ajax(removeHelpMenuItems);

// Run on every route change (important)
frappe.router.on("change", removeHelpMenuItems);

// Safety net (Help menu opens dynamically)
document.addEventListener("click", e => {
  if (e.target.closest(".dropdown-help")) {
    setTimeout(removeHelpMenuItems, 50);
  }
});
