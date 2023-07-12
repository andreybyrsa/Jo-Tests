const testModal = document.getElementById("test-settings-modal");

const closeTestModalButton = document.getElementById("close-test-modal-button");

const toggleButton = document.getElementById("toggle-button");
const toggleAvailable = document.getElementById("test-available");

const OPENING_TEST_SETTINGS_MODAL_CLASS = "test-settings-modal--opened";
const CLOSING_TEST_SETTINGS_MODAL_CLASS = "test-settings-modal--closed";

const ACTIVE_TOGGLE_BUTTON_CLASS = "test-settings-modal__toggle-button--active";

const ACTIVE_TOGGLE_CLASS = "test-settings-modal__toggle--active";
const DISABEL_TOGGLE_CLASS = "test-settings-modal__toggle--disable";

toggleButton.addEventListener("click", () => {
  if (toggleAvailable.classList.contains(ACTIVE_TOGGLE_CLASS)) {
    toggleButton.classList.remove(ACTIVE_TOGGLE_BUTTON_CLASS);
    toggleAvailable.classList.add(DISABEL_TOGGLE_CLASS);

    setTimeout(() => {
      toggleAvailable.classList.remove(ACTIVE_TOGGLE_CLASS);
      toggleAvailable.classList.remove(DISABEL_TOGGLE_CLASS);
    }, 300);

    toggleAvailable.value = 'false';
  } else {
    toggleButton.classList.add(ACTIVE_TOGGLE_BUTTON_CLASS);
    toggleAvailable.classList.add(ACTIVE_TOGGLE_CLASS);

    toggleAvailable.value = 'true';
  }
});

function openTestModal(currentTest) {
  const testTime = document.getElementById("test-time");

  testModal.style.display = "flex";
  testModal.classList.add(OPENING_TEST_SETTINGS_MODAL_CLASS);
  openModal();

  removeToggleClassNames();

  toggleAvailable.value = 'false';

  testTime.value = currentTest?.test_time ? currentTest.test_time : 60;
  switchToggle(`${currentTest?.available}`);
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

function switchToggle(available) {
  if (available === 'true') {
    toggleButton.click();
    toggleAvailable.value = 'true';
  }
}

function removeToggleClassNames() {
  toggleButton.classList.remove(ACTIVE_TOGGLE_BUTTON_CLASS);
  toggleAvailable.classList.remove(ACTIVE_TOGGLE_CLASS);
  toggleAvailable.classList.remove(DISABEL_TOGGLE_CLASS);
}
