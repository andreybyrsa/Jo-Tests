import { addPageClassName } from "/static/core/js/PageLayout.js";

addPageClassName("course-tests-page");

const dataCourseTests =
  document.getElementById("data-course-tests").textContent;
const dataTestsResults =
  document.getElementById("data-tests-results").textContent;

const JSON_COURSE_TESTS = JSON.parse(dataCourseTests);
const JSON_TESTS_RESULTS = JSON.parse(dataTestsResults);

const sideBarTitle = document.getElementById("side-bar-title");
const sideBarDescription = document.getElementById("side-bar-description");

const sideBarContent = document.getElementById("side-bar-content");
const sideBarQuestionsAmount = document.getElementById("test-question-amount");
const sideBarTestResult = document.getElementById("test-result");
const sideBarTestTime = document.getElementById("test-time");
const sidebarButton = document.getElementById("test-button");

const sideBarImage = document.getElementById("side-bar-image");

const tests = document.querySelectorAll(".course-tests-page__test");

const ACTIVE_TEST_CLASS = "course-tests-page__test--active";
const DISABLED_BUTTON_CLASS = "test-start-side-bar__button--disabled";

Array.from(tests).forEach((test, index) => {
  test.onclick = () => openSideBar(index, test);
});

function removeActiveTests() {
  Array.from(tests).forEach((test) => {
    test.classList.remove(ACTIVE_TEST_CLASS);
  });
}

function openSideBar(index, currentTest) {
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

  console.log(result);
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
