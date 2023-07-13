import { addPageClassName } from "/static/core/js/PageLayout.js";
import { openSideBar, useInfoSideBar } from "/static/core/js/InfoSideBar.js";

addPageClassName("courses-page");

const dataCourses = document.getElementById("data-courses").textContent;
const JSON_DATA = JSON.parse(dataCourses);

const courses = document.querySelectorAll(".courses-page__course");
const progressBars = document.querySelectorAll(".courses-page__progress-bar");

Array.from(courses).forEach((course, index) => {
  course.onclick = () => openSideBar(index)
});

Array.from(progressBars).forEach((progressBar, index) => {
  const currentProgress = JSON_DATA[index].progress;

  progressBar.style.width = `${currentProgress}%`;
});

useInfoSideBar(JSON_DATA, courses, "courses-page__course");
