addPageClassName("pass-test-page");

const dataTest = document.getElementById("data-test").textContent;
const dataQuestions = document.getElementById("data-questions").textContent;

const JSON_TEST = JSON.parse(dataTest);
const JSON_QUESTIONS = JSON.parse(dataQuestions);

const testTitle = document.getElementById("side-bar-title");
const testDescription = document.getElementById("side-bar-description");
const testDate = document.getElementById("test-date");
const testQuestionsAmount = document.getElementById("test-questions-amount");
const testTime = document.getElementById("test-time");

const { test, test_time } = JSON_TEST;
const { title, description, questions_amount, slug } = test;

testTitle.textContent = title;
testDescription.textContent = description;
testDate.textContent = getCurrentDate().slice(0, -6);
testQuestionsAmount.textContent = questions_amount;

const questionsWrapper = document.getElementById("questions");

const submitButton = document.getElementById("submit-button");

const ACTIVE_ANSWER_CLASS = "pass-test-page__question-answer--active";

let currentQuestions = [];
let currentAnswers = [];

if (JSON_QUESTIONS.length) {
  Array.from(JSON_QUESTIONS).forEach((questionInfo) => {
    const { question, id, qtype, answers } = questionInfo;
    const answersType = qtype == "single" ? "radio" : "checkbox";

    const [newQuestion, answerWrapper] = createQuestion(
      "pass-test-page__question",
      currentQuestions,
      question,
      id
    );

    Array.from(answers).forEach((answerInfo) => {
      const { answer } = answerInfo;

      answerWrapper.appendChild(
        createAnswer(
          "pass-test-page__question-answer",
          newQuestion,
          answerWrapper,
          answer,
          answersType
        )
      );
    });

    questionsWrapper.appendChild(newQuestion);
    currentQuestions.push(newQuestion);
  });
}

submitButton.addEventListener("click", () => {
  localStorage.removeItem(slug);

  questionsWrapper.submit();
});

startTimer(test_time, slug);

function startTimer(minutes, slug) {
  const currentTime = new Date().getTime();
  const startedTime = localStorage.getItem(slug);

  let seconds = null;

  if (startedTime) {
    const timeInProcess = Math.floor((currentTime - startedTime) / 1000);

    seconds = minutes * 60 - timeInProcess;

    if (seconds <= 0) {
      localStorage.removeItem(slug);

      submitButton.click();

      return;
    }
  } else {
    localStorage.setItem(slug, currentTime);

    seconds = minutes * 60;
  }

  const { time } = getCurrentTime(seconds);
  testTime.textContent = time;

  const timerId = setInterval(() => {
    seconds--;

    const { currentMinutes, currentSeconds } = getCurrentTime(seconds);

    testTime.textContent = `${currentMinutes}:${currentSeconds}`;

    if (seconds <= 0) {
      clearInterval(timerId);

      localStorage.removeItem(slug);

      submitButton.click();
    }
  }, 1000);
}

function getCurrentTime(seconds) {
  let currentMinutes = Math.floor(seconds / 60);
  let currentSeconds = Math.abs(currentMinutes * 60 - seconds);

  currentMinutes =
    String(currentMinutes).length > 1 ? currentMinutes : `0${currentMinutes}`;
  currentSeconds =
    String(currentSeconds).length > 1 ? currentSeconds : `0${currentSeconds}`;

  return {
    currentMinutes,
    currentSeconds,
    time: `${currentMinutes}:${currentSeconds}`,
  };
}
