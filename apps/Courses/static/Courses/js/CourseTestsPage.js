import { addPageClassName } from "/static/core/js/PageLayout.js";

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

if (JSON_RESULTS) {
  Array.from(tests).forEach((test, index) => {
    test.onclick = () => openResultsSideBar(index, test);
  });

  Array.from(groups).forEach((group, index) => {
    group.onclick = () => openGroup(index, group);
  });
} else {
  Array.from(tests).forEach((test, index) => {
    test.onclick = () => openTestSideBar(index, test);
  });
}

function removeActiveTests() {
  Array.from(tests).forEach((test) => {
    test.classList.remove(ACTIVE_TEST_CLASS);
  });
}

function openTestSideBar(index, currentTest) {
  removeActiveTests();
  currentTest.classList.add(ACTIVE_TEST_CLASS);

  const currentTestInfo = JSON_COURSE_TESTS[index];
  const { test, test_time } = currentTestInfo;
  const { title, description, questions_amount, slug } = test;

  const currentTestResult = Array.from(JSON_TESTS_RESULTS).find(
    (test) => test.test_slug === slug
  );
  const { result, max_result, result_slug } = currentTestResult;

  sideBarImage.style.display = "none";
  sidebarButton.style.display = "flex";
  sideBarContent.style.display = "flex";

  sideBarTitle.textContent = title;
  sideBarDescription.textContent = description;

  sideBarQuestionsAmount.textContent = questions_amount;
  sideBarTestTime.textContent = `${test_time} минут`;
  sideBarTestResult.textContent = result
    ? `${result}/${max_result}`
    : "не начато";

  if (result) {
    sidebarButton.classList.add(DISABLED_BUTTON_CLASS);
    sidebarButton.textContent = "Просмотреть";

    sidebarButton.href = sidebarButton.getAttribute("href") + result_slug;
  } else {
    sidebarButton.classList.remove(DISABLED_BUTTON_CLASS);
    sidebarButton.textContent = "Начать тест";

    sidebarButton.href = sidebarButton.getAttribute("href") + slug;
  }
}

function openResultsSideBar(index, currentTest) {
  removeActiveTests();
  currentTest.classList.add(ACTIVE_TEST_CLASS);

  const currentTestInfo = JSON_COURSE_TESTS[index];
  const { test } = currentTestInfo;
  const { title, description } = test;

  sideBarImage.style.display = "none";
  sideBarContent.style.display = "flex";

  sideBarTitle.textContent = title;
  sideBarDescription.textContent = description;
}

function openGroup(index, currentGroup) {
  const groupContent = Array.from(currentGroup.childNodes).find(
    (element) => element.classList?.contains("test-results-side-bar__group")
  );

  if (groupContent.classList.contains(OPENED_GROUP_CLASS)) {
    groupContent.classList.add(CLOSED_GROUP_CLASS);

    setTimeout(() => {
      groupContent.classList.remove(OPENED_GROUP_CLASS);
      groupContent.classList.remove(CLOSED_GROUP_CLASS);
    }, 300);
  } else {
    groupContent.classList.add(OPENED_GROUP_CLASS);
  }
}
