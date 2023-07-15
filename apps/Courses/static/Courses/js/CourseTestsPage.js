addPageClassName("course-tests-page");

const dataCourseTests =
  document.getElementById("data-course-tests").textContent;
const dataTestsResults =
  document.getElementById("data-tests-results").textContent;
const dataGroups = document.getElementById("data-groups").textContent;
const dataResults = document.getElementById("data-results").textContent;

const JSON_COURSE_TESTS = JSON.parse(dataCourseTests);
const JSON_TESTS_RESULTS = JSON.parse(dataTestsResults);
const JSON_GROUPS = JSON.parse(dataGroups);
const JSON_RESULTS = JSON.parse(dataResults);

const sideBarTitle = document.getElementById("side-bar-title");
const sideBarDescription = document.getElementById("side-bar-description");

const sideBarContent = document.getElementById("side-bar-content");
const sideBarQuestionsAmount = document.getElementById("test-question-amount");
const sideBarTestResult = document.getElementById("test-result");
const sideBarTestTime = document.getElementById("test-time");
const sidebarButton = document.getElementById("test-button");

const sideBarImage = document.getElementById("side-bar-image");

const tests = document.querySelectorAll(".course-tests-page__test");
const groups = document.querySelectorAll(
  ".test-results-side-bar__group-wrapper"
);

const ACTIVE_TEST_CLASS = "course-tests-page__test--active";
const DISABLED_BUTTON_CLASS = "test-start-side-bar__button--disabled";

const OPENED_GROUP_CLASS = "test-results-side-bar__group--opened";
const CLOSED_GROUP_CLASS = "test-results-side-bar__group--closed";

const ACTIVE_ICON_GROUP_CLASS = "test-results-side-bar__group-icon--active";

if (JSON_RESULTS) {
  Array.from(tests).forEach((test, index) => {
    test.onclick = () => openResultsSideBar(index, test);
  });

  Array.from(groups).forEach((group, index) => {
    group.onclick = () => openGroup(index);
  });
} else {
  Array.from(tests).forEach((test, index) => {
    test.onclick = () => openTestSideBar(index, test);
  });
}

let currentOpenedTest = null;

function removeActiveTests() {
  Array.from(tests).forEach((test) => {
    test.classList.remove(ACTIVE_TEST_CLASS);
  });
}

function openTestSideBar(itemId, currentTest) {
  removeActiveTests();
  currentTest.classList.add(ACTIVE_TEST_CLASS);

  const currentTestInfo = JSON_COURSE_TESTS[itemId];
  const { test, test_time } = currentTestInfo;
  const { title, description, questions_amount, max_result, slug } = test;

  const currentTestResult = JSON_TESTS_RESULTS
    ? Array.from(JSON_TESTS_RESULTS).find((test) => test.test_slug === slug)
    : null;

  let studentResult = null;
  let resultSlug = null;

  if (currentTestResult) {
    const { result, result_slug } = currentTestResult;
    studentResult = result;
    resultSlug = result_slug;
  }

  sideBarImage.style.display = "none";
  sidebarButton.style.display = "flex";
  sideBarContent.style.display = "flex";

  sideBarTitle.textContent = title;
  sideBarDescription.textContent = description;

  sideBarQuestionsAmount.textContent = questions_amount;
  sideBarTestTime.textContent = `${test_time} минут`;
  sideBarTestResult.textContent = studentResult
    ? `${studentResult}/${max_result}`
    : "не начато";

  if (studentResult) {
    sidebarButton.classList.add(DISABLED_BUTTON_CLASS);
    sidebarButton.textContent = "Просмотреть";

    sidebarButton.href = sidebarButton.getAttribute("href") + resultSlug;
  } else {
    sidebarButton.classList.remove(DISABLED_BUTTON_CLASS);
    sidebarButton.textContent = "Начать тест";

    sidebarButton.href = sidebarButton.getAttribute("href") + slug;
  }
}

function openResultsSideBar(itemId, currentTest) {
  closeOpenedGroups();

  removeActiveTests();
  currentTest.classList.add(ACTIVE_TEST_CLASS);

  const currentTestInfo = JSON_COURSE_TESTS[itemId];
  currentOpenedTest = currentTestInfo;

  const { test } = currentTestInfo;
  const { title, description } = test;

  sideBarImage.style.display = "none";
  sideBarContent.style.display = "flex";

  sideBarTitle.textContent = title;
  sideBarDescription.textContent = description;
}

function openGroup(itemId) {
  const currentGroupInfo = JSON_GROUPS[itemId];
  const { index } = currentGroupInfo;

  const { slug } = currentOpenedTest.test;
  const currentResults = Array.from(JSON_RESULTS).filter(
    (result) => result.test_slug === slug && result.group_index === index
  );

  const groupResults = document.getElementById(`${index}-results`);
  const groupIcon = document.getElementById(`${index}-icon`);

  groupIcon.classList.toggle(ACTIVE_ICON_GROUP_CLASS);

  if (groupResults.classList.contains(OPENED_GROUP_CLASS)) {
    groupResults.classList.add(CLOSED_GROUP_CLASS);

    removeGroupResults(groupResults);

    setTimeout(() => {
      groupResults.classList.remove(OPENED_GROUP_CLASS);
      groupResults.classList.remove(CLOSED_GROUP_CLASS);

      groupResults.style.display = "none";
    }, 300);
  } else {
    groupResults.style.display = "flex";
    groupResults.classList.add(OPENED_GROUP_CLASS);

    currentResults.forEach((studentResult) => {
      const { result, max_result, student, result_slug } = studentResult;
      const { first_name, last_name } = student;
      const currentStudent = `${first_name} ${last_name}`;

      groupResults.appendChild(
        createGroupResult(currentStudent, result, max_result, result_slug)
      );
    });
  }
}

function createGroupResult(studentName, testResult, testMaxPoints, resultSlug) {
  const resultWrapper = document.createElement("a");
  resultWrapper.className = "test-results-side-bar__result-wrapper";
  resultWrapper.href = "/test/" + resultSlug;

  const studentWrapper = document.createElement("div");
  studentWrapper.className = "test-results-side-bar__result-student";

  const student = document.createElement("span");
  student.textContent = studentName;

  const studentResult = document.createElement("span");
  studentResult.textContent = `${testResult}/${testMaxPoints}`;

  studentWrapper.appendChild(student);
  studentWrapper.appendChild(studentResult);

  const progressBar = document.createElement("div");
  progressBar.className = "test-results-side-bar__result-progressbar";

  const progress = document.createElement("div");
  progress.className = "test-results-side-bar__result-progress";
  progress.style.width = `${(testResult / testMaxPoints) * 100}%`;

  const percents = document.createElement("div");
  percents.className = "test-results-side-bar__result-percents";

  progress.appendChild(percents);
  progressBar.appendChild(progress);

  resultWrapper.appendChild(studentWrapper);
  resultWrapper.appendChild(progressBar);

  return resultWrapper;
}

function closeOpenedGroups() {
  const groupIcons = document.querySelectorAll(
    "[class~='test-results-side-bar__group-icon']"
  );
  const groupResults = document.querySelectorAll(
    "[class~='test-results-side-bar__group']"
  );

  groupIcons.forEach((groupIcon) => {
    if (groupIcon.classList.contains(ACTIVE_ICON_GROUP_CLASS)) {
      groupIcon.classList.remove(ACTIVE_ICON_GROUP_CLASS);
    }
  });

  groupResults.forEach((groupResult) => {
    if (groupResult.classList.contains(OPENED_GROUP_CLASS)) {
      groupResult.classList.remove(OPENED_GROUP_CLASS);

      removeGroupResults(groupResult);

      groupResult.style.display = "none";
    }
  });
}

function removeGroupResults(resultsWrapper) {
  Array.from(resultsWrapper.childNodes).forEach((result) => result.remove());
}
