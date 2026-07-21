// Target elements using exact IDs from post_detail.html
const editButtons = document.getElementsByClassName('btn-edit');
const deleteButtons = document.getElementsByClassName('btn-delete');
const commentText = document.getElementById('id_body');
const commentForm = document.getElementById('commentForm'); 
const submitButton = document.getElementById('submitButton');

// Modal elements
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    // Fixed attribute name to match data-comment-id in post_detail.html
    let commentId = e.target.getAttribute("data-comment-id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

/**
* Initializes edit functionality for the provided edit buttons.
*/
for (let button of editButtons) {
  button.addEventListener('click', (e) => {
    let commentId = e.target.getAttribute('data-comment-id');
    let commentContent = document.getElementById(`comment${commentId}`).innerText.trim();

    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute('action', `edit_comment/${commentId}`);
  });
}