addPageClassName("courses-page");

const dataCourses = document.getElementById("data-courses").textContent;
const JSON_DATA = JSON.parse(dataCourses);

const courses = document.querySelectorAll(".courses-page__course");
const progressBars = document.querySelectorAll(".courses-page__progress-bar");

console.log(JSON_DATA)

Array.from(courses).forEach((course, index) => {
  course.onclick = () => openSideBar(index)
});

Array.from(progressBars).forEach((progressBar, index) => {
  const {progress, max_course_progress} = JSON_DATA[index]
  const currentProgress = (progress / max_course_progress) * 100

  progressBar.style.width = `${currentProgress}%`;
});

useInfoSideBar(JSON_DATA, courses, "courses-page__course");
