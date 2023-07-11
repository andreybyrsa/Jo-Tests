const testModal = document.getElementById("test-settings-modal");

const closeTestModalButton = document.getElementById("close-test-modal-button");
const toggleButton = document.getElementById("toggle-button");

const testSlug = document.getElementById("test-slug");

const toggle = document.getElementById("toggle");
const availableInput = document.getElementById("test-available");

const OPENING_TEST_SETTINGS_MODAL_CLASS = "test-settings-modal--opened";
const CLOSING_TEST_SETTINGS_MODAL_CLASS = "test-settings-modal--closed";

const ACTIVE_TOGGLE_CLASS = "test-settings-modal__toggle--active";

toggleButton.addEventListener("click", () => {
  if (toggle.classList.contains(ACTIVE_TOGGLE_CLASS)) {
    toggle.classList.remove(ACTIVE_TOGGLE_CLASS);
    availableInput.value = false;
  } else {
    toggle.classList.add(ACTIVE_TOGGLE_CLASS);
    availableInput.value = true;
  }
});

function openTestModal(slug) {
  testModal.style.display = "flex";

  testSlug.value = slug;

  testModal.classList.add(OPENING_TEST_SETTINGS_MODAL_CLASS);
  openModal();
}

function closeTestModal() {
  testModal.classList.add(CLOSING_TEST_SETTINGS_MODAL_CLASS);
  setTimeout(() => {
    testModal.style.display = "none";

    testModal.classList.remove(OPENING_TEST_SETTINGS_MODAL_CLASS);
    testModal.classList.remove(CLOSING_TEST_SETTINGS_MODAL_CLASS);
  }, 300);
}

modalLayout.addEventListener("click", (event) => {
  if (event.target.id === "modal-layout") {
    closeTestModal();
  }
});

closeTestModalButton.addEventListener("click", () => {
  closeTestModal();
  closeModal();
});
