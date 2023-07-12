addPageClassName("tests-page");

const dataTests = document.getElementById("data-tests").textContent;
const JSON_DATA = JSON.parse(dataTests);

const tests = document.querySelectorAll(".tests-page__test");

useInfoSideBar(JSON_DATA, tests, "tests-page__test");

const searchInput = document.getElementById("search-input");
const searchIcon = document.getElementById("search-icon");

const ACTIVE_SEARCH_ICON_COLOR = "#4360F8";
const DISABLED_SEARCH_ICON_COLOR = "#898989";

searchInput.addEventListener("input", (event) => {
  const searchedValue = event.target.value;

  if (searchedValue) {
    searchIcon.style.color = ACTIVE_SEARCH_ICON_COLOR;
  } else {
    searchIcon.style.color = DISABLED_SEARCH_ICON_COLOR;
  }

  searchByChildNodes(event, tests, "tests-page__test-title");
});
