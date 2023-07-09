addPageClassName("courses-page");

const dataCourses = document.getElementById("data-courses").textContent;
const JSON_DATA = JSON.parse(dataCourses);

const courses = document.querySelectorAll(".courses-page__course");
const progressBars = document.querySelectorAll(".courses-page__progress-bar");

Array.from(progressBars).forEach((progressBar, index) => {
  const currentProgress = JSON_DATA[index].progress;

  progressBar.style.width = `${currentProgress}%`;
});

useInfoSideBar(JSON_DATA, courses, "courses-page__course");
