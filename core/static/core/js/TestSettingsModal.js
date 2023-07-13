import { useModal } from "/static/core/js/PageLayout.js";

const [testSettingsModal, openTestSettingsModal, closeTestSettingsModal] =
  useModal("test-settings-modal", null, "close-test-modal-button");

const toggleButton = document.getElementById("toggle-button");
const toggleAvailable = document.getElementById("test-available");

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

    toggleAvailable.value = "false";
  } else {
    toggleButton.classList.add(ACTIVE_TOGGLE_BUTTON_CLASS);
    toggleAvailable.classList.add(ACTIVE_TOGGLE_CLASS);

    toggleAvailable.value = "true";
  }
});

function openTestModal(currentTest) {
  const testTime = document.getElementById("test-time");

  openTestSettingsModal();

  removeToggleClassNames();

  toggleAvailable.value = "false";

  testTime.value = currentTest?.test_time ? currentTest.test_time : 60;
  switchToggle(`${currentTest?.available}`);
}

function switchToggle(available) {
  if (available === "true") {
    toggleButton.click();
    toggleAvailable.value = "true";
  }
}

function removeToggleClassNames() {
  toggleButton.classList.remove(ACTIVE_TOGGLE_BUTTON_CLASS);
  toggleAvailable.classList.remove(ACTIVE_TOGGLE_CLASS);
  toggleAvailable.classList.remove(DISABEL_TOGGLE_CLASS);
}

export { openTestModal, closeTestSettingsModal };
