console.log("Life, The Universe and Everything!");

// Wait for DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteModalElement = document.getElementById("deleteModal");
  const deleteModal = deleteModalElement ? new bootstrap.Modal(deleteModalElement) : null;
  let deleteCommentId = null;
  let editingCommentId = null;

  // Get the current post slug from the URL
  const currentPath = window.location.pathname;

  /**
   * Initializes edit functionality for the provided edit buttons.
   *
   * For each button in the `editButtons` collection:
   * - Retrieves the associated comment's ID upon click.
   * - Fetches the content of the corresponding comment.
   * - Populates the `commentText` input/textarea with the comment's content for editing.
   * - Updates the submit button's text to "Update".
   * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
   */
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      let commentId = e.target.getAttribute("comment_id");
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      editingCommentId = commentId;
      commentForm.setAttribute("action", `${currentPath}edit_comment/${commentId}/`);
      commentForm.scrollIntoView({ behavior: "smooth" });
    });
  }

  /**
   * Handle normal form submission
   */
  if (commentForm) {
    commentForm.addEventListener("submit", function (e) {
      if (!editingCommentId) {
        // Normal new comment submission - let it proceed
        return;
      }
      // For edit - action already set above, just let it submit
    });
  }

  /**
   * Reset form after successful submission
   */
  function resetForm() {
    editingCommentId = null;
    if (submitButton) {
      submitButton.innerText = "Submit Comment";
    }
    if (commentText) {
      commentText.value = "";
    }
    if (commentForm) {
      commentForm.setAttribute("action", "");
    }
  }

  /**
   * Initializes delete functionality for the provided delete buttons.
   *
   * For each button in the `deleteButtons` collection:
   * - Retrieves the associated comment's ID upon click.
   * - Shows a confirmation modal.
   * - Sets up the delete confirmation handler.
   */
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      deleteCommentId = e.target.getAttribute("comment_id");
      if (deleteModal) {
        deleteModal.show();
      }
    });
  }

  /**
   * Handles the delete confirmation.
   * Submits a POST request to the delete_comment endpoint.
   */
  const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
  if (confirmDeleteBtn) {
    confirmDeleteBtn.addEventListener("click", () => {
      if (deleteCommentId) {
        const deleteForm = document.getElementById("deleteCommentForm");
        deleteForm.setAttribute("action", `${currentPath}delete_comment/${deleteCommentId}/`);
        deleteForm.submit();
      }
    });
  }
});
