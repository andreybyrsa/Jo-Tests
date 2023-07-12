let profileModal = document.getElementById("profile-modal");

const OPENING_PROFILE_MODAL_CLASS = "profile-modal--opened";
const CLOSING_PROFILE_MODAL_CLASS = "profile-modal--closed";

function openProfileModal() {
  profileModal.classList.add(OPENING_PROFILE_MODAL_CLASS);
  openModal();
}

function closeProfileModal() {
  profileModal.classList.add(CLOSING_PROFILE_MODAL_CLASS);

  setTimeout(() => {
    profileModal.classList.remove(OPENING_PROFILE_MODAL_CLASS);
    profileModal.classList.remove(CLOSING_PROFILE_MODAL_CLASS);
  }, 300);
}

modalLayout.addEventListener("click", (event) => {
  if (event.target.id === "modal-layout") {
    closeProfileModal();
  }
});
