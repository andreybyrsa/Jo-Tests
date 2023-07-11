const createCourseModal = document.getElementById("create-course-modal");

const closeCourseModalButton = document.getElementById("close-modal-button");

const OPENING_CREATE_COURSE_MODAL_CLASS = "create-course-modal--opened";
const CLOSING_CREATE_COURSE_MODAL_CLASS = "create-course-modal--closed";

function openCreateCourseModal() {
  createCourseModal.classList.add(OPENING_CREATE_COURSE_MODAL_CLASS);
  openModal();
}

function closeCreateCourseModal() {
  createCourseModal.classList.add(CLOSING_CREATE_COURSE_MODAL_CLASS);
  setTimeout(() => {
    createCourseModal.classList.remove(OPENING_CREATE_COURSE_MODAL_CLASS);
    createCourseModal.classList.remove(CLOSING_CREATE_COURSE_MODAL_CLASS);
  }, 300);
}

modalLayout.addEventListener("click", (event) => {
  if (event.target.id === "modal-layout") {
    closeCreateCourseModal();
  }
});

closeCourseModalButton.addEventListener("click", () => {
  closeCreateCourseModal();
  closeModal();
});

function createModalTest(testText, testMaxPoints, testSlug, isExistTest) {
  const testWrapper = document.createElement("div");
  testWrapper.className = "create-course-modal__test-wrapper";

  const test = document.createElement("div");
  test.className = "create-course-modal__test";

  const testName = document.createElement("span");
  testName.textContent = testText;

  const testCheckboxInput = document.createElement("input");
  testCheckboxInput.type = "checkbox";
  testCheckboxInput.value = testSlug;
  testCheckboxInput.checked = isExistTest ? true : false;

  test.appendChild(testCheckboxInput);
  test.appendChild(testName);

  const testPoints = document.createElement("span");
  testPoints.textContent = `балл ${testMaxPoints}`;

  testWrapper.appendChild(test);
  testWrapper.appendChild(testPoints);

  testWrapper.addEventListener("click", (event) => {
    if (event.target.type !== "checkbox") {
      checkData(testCheckboxInput);
    }
  });

  return testWrapper;
}

function createModalGroup(groupText, index, isExistGroup) {
  const group = document.createElement("div");
  group.className = "create-course-modal__group";

  const groupContent = document.createElement("div");
  groupContent.className = "create-course-modal__group-content";

  const groupName = document.createElement("span");
  groupName.textContent = groupText;

  const groupCheckboxInput = document.createElement("input");
  groupCheckboxInput.type = "checkbox";
  groupCheckboxInput.value = index;
  groupCheckboxInput.checked = isExistGroup ? true : false;

  groupContent.appendChild(groupCheckboxInput);
  groupContent.appendChild(groupName);

  group.appendChild(groupContent);

  group.addEventListener("click", (event) => {
    if (event.target.type !== "checkbox") {
      checkData(groupCheckboxInput);
    }
  });

  return group;
}

function checkData(currentCheckbox) {
  if (currentCheckbox.checked) {
    currentCheckbox.checked = false;
  } else {
    currentCheckbox.checked = true;
  }
}
