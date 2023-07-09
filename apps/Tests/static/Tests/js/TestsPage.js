addPageClassName("tests-page");

const dataTests = document.getElementById("data-tests").textContent;
const JSON_DATA = JSON.parse(dataTests);

const tests = document.querySelectorAll(".tests-page__test");

useInfoSideBar(JSON_DATA, tests, "tests-page__test");
