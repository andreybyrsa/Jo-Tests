addPageClassName("tests-page");

const dataTests = document.getElementById("data-tests").textContent;
const JSON_DATA = JSON.parse(dataTests);

const tests = document.querySelectorAll(".tests-page__test");

useInfoSideBar(JSON_DATA, tests, "tests-page__test");

const searchInput = document.getElementById("search-input");
const searchIcon = document.getElementById("search-icon");

const ACTIVE_ICON_COLOR = "#4360F8";
const DISABLED_ICON_COLOR = "#898989";

searchInput.addEventListener("input", (event) => {
  const searchedValue = event.target.value.toLowerCase();

  if (searchedValue) {
    searchIcon.style.color = ACTIVE_ICON_COLOR;
  } else {
    searchIcon.style.color = DISABLED_ICON_COLOR;
  }

  Array.from(tests).forEach((test) => {
    const currentTestTitle = test.childNodes[1].textContent.toLowerCase();

    if (currentTestTitle.includes(searchedValue)) {
      test.style.display = "flex";
    } else {
      test.style.display = "none";
    }
  });
});
