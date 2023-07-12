addPageClassName("create-course-page");

const dataTests = document.getElementById("data-tests").textContent;
const dataGroups = document.getElementById("data-groups").textContent;

const JSON_TESTS = JSON.parse(dataTests);
const JSON_GROUPS = JSON.parse(dataGroups);

const form = document.getElementById("form");

const courseTitleInput = document.getElementById("input-course-title");
const courseDescriptionInput = document.getElementById(
  "input-course-description"
);

const courseTitle = document.getElementById("course-title");
const courseDescription = document.getElementById("course-description");
const courseTests = document.getElementById("course-tests");
const courseGroups = document.getElementById("course-groups");

const dateCreated = document.getElementById("date-created");

const testsWrapper = document.getElementById("tests");
const groupsWrapper = document.getElementById("groups");

const addTestButton = document.getElementById("add-test-button");
const addGroupButton = document.getElementById("add-group-button");
const submitButton = document.getElementById("submit-button");

const courseModalContent = document.getElementById("course-modal-content");
const modalSearchInput = document.getElementById("search-input");
const saveTestsButton = document.getElementById("save-tests-button");
const saveGroupsButton = document.getElementById("save-groups-button");
const saveTestSettings = document.getElementById("save-test-settings");

dateCreated.textContent = getCurrentDate();
setInterval(() => {
  dateCreated.textContent = getCurrentDate();
}, 10000);

let currentTests = [];
let currentGroups = [];

addTestButton.addEventListener("click", () => {
  saveTestsButton.style.display = "flex";
  saveGroupsButton.style.display = "none";

  addModalElements(JSON_TESTS, currentTests);
});

addGroupButton.addEventListener("click", () => {
  saveGroupsButton.style.display = "flex";
  saveTestsButton.style.display = "none";

  addModalElements(JSON_GROUPS, currentGroups);
});

submitButton.addEventListener("click", () => {
  courseTitle.value = courseTitleInput.value;
  courseDescription.value = courseDescriptionInput.value;

  courseTests.value = currentTests
    .reduce((prevValue, value) => {
      const currentAvailable = value.available
        ? value.available
        : testAvailable.value;

      const currentTestTime = value.test_time
        ? value.test_time
        : testTime.value;

      return (
        `${value.slug}/${currentAvailable}/${currentTestTime} ` + prevValue
      );
    }, "")
    .slice(0, -1);

  courseGroups.value = currentGroups
    .reduce((prevValue, value) => `${value.index} ` + prevValue, "")
    .slice(0, -1);

  form.submit();
});

saveTestsButton.addEventListener("click", () => {
  removeWrapperElements(testsWrapper);

  saveElements(JSON_TESTS, currentTests);
});

saveGroupsButton.addEventListener("click", () => {
  removeWrapperElements(groupsWrapper);

  saveElements(JSON_GROUPS, currentGroups);
});

saveTestSettings.addEventListener("click", () => {
  const testAvailable = document.getElementById("test-available");
  const testTime = document.getElementById("test-time");

  currentTests.forEach((test) => {
    if (test.slug == currentTest.slug) {
      test.available = testAvailable.value;
      test.test_time = testTime.value;
    }
  });

  testAvailable.value = false;
  testTime.value = 60;

  closeTestModal();
  closeModal();
});

function createTest(testTextName, maxPoints, slug) {
  const testWrapper = document.createElement("div");
  testWrapper.className = "create-course-page__test";

  const testContent = document.createElement("div");
  testContent.className = "create-course-page__test-content";

  const openTestIcon = document.createElement("i");
  openTestIcon.className = "bi bi-eye create-course-page__test-open-icon";
  openTestIcon.onclick = () => {
    const currentTest = Array.from(JSON_TESTS).find((test) => test.slug === slug);
    openTestModal(currentTest);
  };
  const testName = document.createElement("span");
  testName.textContent = testTextName;

  testContent.appendChild(openTestIcon);
  testContent.appendChild(testName);

  const testMaxPoints = document.createElement("span");
  testMaxPoints.textContent = `${maxPoints} балл(ов)`;

  const testRemoveButton = createRemoveButton();
  testRemoveButton.onclick = () => {
    testWrapper.remove();
    currentTests = currentTests.filter((test) => test.slug !== slug);
  };

  testWrapper.appendChild(testContent);
  testWrapper.appendChild(testMaxPoints);
  testWrapper.appendChild(testRemoveButton);

  return testWrapper;
}

function createGroup(groupTextName, index) {
  const groupWrapper = document.createElement("div");
  groupWrapper.className = "create-course-page__group";

  const groupName = document.createElement("span");
  groupName.textContent = groupTextName;

  const groupRemoveButton = createRemoveButton();
  groupRemoveButton.onclick = () => {
    groupWrapper.remove();
    currentGroups = currentGroups.filter((group) => group.index !== index);
  };

  groupWrapper.appendChild(groupName);
  groupWrapper.appendChild(groupRemoveButton);

  return groupWrapper;
}

function createRemoveButton() {
  const removeButton = document.createElement("button");
  removeButton.className = "create-course-page__remove-button";
  const removeIcon = document.createElement("i");
  removeIcon.className = "bi bi-x-circle create-course-page__remove-icon";

  removeButton.appendChild(removeIcon);

  return removeButton;
}

function addModalElements(data, currentData) {
  removeModalElements();

  openCreateCourseModal();

  Array.from(data).forEach((dataElem) => {
    const { title, max_result, slug, groupname, index } = dataElem;

    const isExistElement = currentData.find((elem) => elem === dataElem)
      ? true
      : false;

    if (slug) {
      courseModalContent.appendChild(
        createModalTest(title, max_result, slug, isExistElement)
      );

      return;
    }

    courseModalContent.appendChild(
      createModalGroup(groupname, index, isExistElement)
    );
  });
}

function saveElements(data, currentData) {
  modalSearchInput.value = "";

  Array.from(courseModalContent.childNodes).forEach((element) => {
    const checkboxInput = element.childNodes[0].childNodes[0];

    const choosenElement = Array.from(data).find(
      (dataElem) =>
        dataElem.slug === checkboxInput.value ||
        dataElem.index === checkboxInput.value
    );

    if (checkboxInput.checked) {
      const isExistInCurrentData = currentData.find(
        (elem) => elem === choosenElement
      )
        ? true
        : false;

      if (!isExistInCurrentData) {
        currentData.push(choosenElement);
      }

      const { title, max_result, slug, index, groupname } = choosenElement;

      if (slug) {
        testsWrapper.appendChild(createTest(title, max_result, slug));

        return;
      }

      groupsWrapper.appendChild(createGroup(groupname, index));
    } else {
      const currentElementIndex = currentData.findIndex(
        (elem) => elem === choosenElement
      );

      if (currentElementIndex >= 0) {
        currentData.splice(currentElementIndex, 1);
      }
    }
  });

  closeCreateCourseModal();
  closeModal();
}

function removeWrapperElements(elementWrapper) {
  Array.from(elementWrapper.childNodes).forEach((element) => {
    element.remove();
  });
}

function removeModalElements() {
  Array.from(courseModalContent.childNodes).forEach((element) => {
    element.remove();
  });
}
