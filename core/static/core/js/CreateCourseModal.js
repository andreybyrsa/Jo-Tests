const [createCourseModal, openCreateCourseModal, closeCreateCourseModal] =
  useModal("create-course-modal", null, "close-course-modal-button");

const searchInput = document.getElementById("search-input");

searchInput.addEventListener("input", (event) => {
  const searchedItem =
    courseModalContent.childNodes[0].className ===
    "create-course-modal__test-wrapper"
      ? "create-course-modal__test"
      : "create-course-modal__group-content";

  searchByChildNodes(event, courseModalContent.childNodes, searchedItem);
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
