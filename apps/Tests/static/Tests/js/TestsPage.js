addPageClassName("tests-page");

const dataTests = document.getElementById("data-tests").textContent;
const JSON_DATA = JSON.parse(dataTests);

const tests = document.querySelectorAll(".tests-page__test");

const sideBarContent = document.getElementById("side-bar-content");
const sideBarTitle = document.getElementById("side-bar-title");
const sideBarDescription = document.getElementById("side-bar-description");
const sideBarTimeCreated = document.getElementById("side-bar-time-created");
const sideBarTimeUpdated = document.getElementById("side-bar-time-updated");
const sideBarImage = document.getElementById("side-bar-image");

function getCurrentDate(testDate) {
  const date = new Date(testDate);

  const year = date.getFullYear();

  let month = date.getMonth();
  month = month >= 10 ? month : `0${month}`;

  let day = date.getDay();
  day = day >= 10 ? day : `0${day}`;

  return `${day}:${month}:${year}`;
}

function removeAcriveClassNames() {
  Array.from(tests).forEach((element) => {
    if (element.classList.contains("tests-page__test--active")) {
      element.classList.remove("tests-page__test--active");
    }
  });
}

function openSideBar(testId) {
  const currentTestData = JSON_DATA[testId];
  const { title, description, time_create, time_update } = currentTestData;

  sideBarImage.style.display = "none";
  sideBarContent.style.display = "flex";

  removeAcriveClassNames();
  const currentTest = tests[testId];
  currentTest.classList.add("tests-page__test--active");

  sideBarTitle.textContent = title;
  sideBarDescription.textContent = description;

  const currentCreateDate = getCurrentDate(time_create);
  const currentUpdateDate = getCurrentDate(time_update);

  if (currentCreateDate == currentUpdateDate) {
    sideBarTimeCreated.textContent = currentCreateDate;
    sideBarTimeUpdated.textContent = "Не изменено";
  } else {
    sideBarTimeCreated.textContent = currentCreateDate;
    sideBarTimeUpdated.textContent = currentUpdateDate;
  }
}
