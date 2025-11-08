// === ICONS ===
lucide.createIcons();

// === MODAL HANDLING ===
function openModal(id) {
    document.getElementById(id).classList.add("active");
}

function closeModal(id) {
    document.getElementById(id).classList.remove("active");
}

function closeAllModals() {
    document.querySelectorAll(".modal").forEach(m => m.classList.remove("active"));
}

// === LOGIN & SIGNUP TABS ===
document.querySelectorAll(".tab-trigger").forEach(button => {
    button.addEventListener("click", () => {
        const tab = button.dataset.tab;

        // deactivate all tabs
        document.querySelectorAll(".tab-trigger").forEach(b => b.classList.remove("active"));
        document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

        // activate clicked one
        button.classList.add("active");
        document.getElementById(tab).classList.add("active");
    });
});

// === QUICK DEMO LOGIN ===
function quickLogin(name, email) {
    showToast(`Logged in as ${name}`);
    closeModal("loginModal");
}

// === TOASTS ===
function showToast(message, type = "success") {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.className = `toast active ${type}`;
    setTimeout(() => toast.classList.remove("active"), 3000);
}

// === SHARE LINK COPY ===
function copyShareLink() {
    const input = document.getElementById("shareLink");
    input.select();
    document.execCommand("copy");
    showToast("Link copied!");
}

// === INVITE COLLABORATOR ===
function inviteCollaborator() {
    const email = document.getElementById("inviteEmail").value;
    if (!email) {
        showToast("Please enter an email", "error");
        return;
    }
    showToast(`Invitation sent to ${email}`);
    document.getElementById("inviteEmail").value = "";
}

// === MODAL BUTTON SHORTCUTS ===
function closeCreateModal() { closeModal("createModal"); }
function closeActivityModal() { closeModal("activityModal"); }
function closeEditActivityModal() { closeModal("editActivityModal"); }
function closeDeleteModal() { closeModal("deleteModal"); }
function closeShareModal() { closeModal("shareModal"); }

// === EXAMPLE FORM SUBMISSION ===
document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", e => {
        e.preventDefault();
        showToast("Form submitted!");
    });
});