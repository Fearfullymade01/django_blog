// Comment edit helpers
// Dynamically construct edit URL, populate form, and submit

document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-edit");
  const deleteButtons = document.querySelectorAll(".btn-delete");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  // Try common textarea targets
  let commentText = document.getElementById("id_body");
  if (!commentText && commentForm) commentText = commentForm.querySelector("textarea");

  const basePath = window.location.pathname.replace(/\/$/, "");

  editButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      const commentId = button.getAttribute("comment_id");
      const contentEl = document.getElementById(`comment${commentId}`);
      if (!commentForm || !commentText || !commentId || !contentEl) return;

      // Populate form and update action
      commentText.value = contentEl.innerText.trim();
      if (submitButton) submitButton.innerText = "Update";
      commentForm.setAttribute("action", `${basePath}/edit_comment/${commentId}/`);
      commentForm.scrollIntoView({ behavior: "smooth" });
    });
  });

  // Delete: show confirm modal and submit hidden form
  const deleteModalEl = document.getElementById("deleteModal");
  const deleteForm = document.getElementById("deleteCommentForm");
  const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
  const deleteModal = deleteModalEl && window.bootstrap ? new bootstrap.Modal(deleteModalEl) : null;
  let deleteCommentId = null;

  deleteButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      deleteCommentId = button.getAttribute("comment_id");
      if (deleteModal) deleteModal.show();
    });
  });

  if (confirmDeleteBtn && deleteForm) {
    confirmDeleteBtn.addEventListener("click", () => {
      if (!deleteCommentId) return;
      deleteForm.setAttribute("action", `${basePath}/delete_comment/${deleteCommentId}/`);
      deleteForm.submit();
    });
  }
});
