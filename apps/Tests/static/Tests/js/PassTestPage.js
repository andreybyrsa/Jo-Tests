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
const { title, description, questions_amount } = test;

testTitle.textContent = title;
testDescription.textContent = description;
testDate.textContent = getCurrentDate().slice(0, -6);
testQuestionsAmount.textContent = questions_amount;
startTimer(1);

const questionsWrapper = document.getElementById("questions");

const submitButton = document.getElementById("submit-button");

const ACTIVE_ANSWER_CLASS = "pass-test-page__question-answer--active";

let currentQuestions = [];
let currentAnswers = [];

if (JSON_QUESTIONS.length) {
  Array.from(JSON_QUESTIONS).forEach((questionInfo) => {
    const { question, qtype, answers } = questionInfo;
    const answersType = qtype == "single" ? "radio" : "checkbox";

    const [newQuestion, answerWrapper] = createQuestion(question);

    Array.from(answers).forEach((answerInfo) => {
      const { answer } = answerInfo;

      answerWrapper.appendChild(
        createAnswer(newQuestion, answerWrapper, answer, answersType)
      );
    });

    questionsWrapper.appendChild(newQuestion);
    currentQuestions.push(newQuestion);
  });
}

submitButton.addEventListener("click", () => {
  questionsWrapper.submit();
});

function startTimer(minutes) {
  testTime.textContent =
    String(minutes).length > 1 ? `${minutes}:00` : `0${minutes}:00`;

  let seconds = minutes * 60;

  let currentMinutes = null;
  let currentSeconds = null;

  const timerId = setInterval(() => {
    seconds--;

    currentMinutes = Math.floor(seconds / 60);
    currentSeconds = Math.abs(currentMinutes * 60 - seconds);

    currentMinutes =
      String(currentMinutes).length > 1 ? currentMinutes : `0${currentMinutes}`;
    currentSeconds =
      String(currentSeconds).length > 1 ? currentSeconds : `0${currentSeconds}`;

    testTime.textContent = `${currentMinutes}:${currentSeconds}`;

    if (seconds === 0) {
      clearInterval(timerId);
    }
  }, 1000);
}

function createQuestion(question) {
  const currentId = currentQuestions.length + 1;
  const questionId = `question-${currentId}`;

  const newQuestion = document.createElement("div");
  newQuestion.id = questionId;
  newQuestion.className = "pass-test-page__question";

  const questionName = document.createElement("span");
  questionName.className = "pass-test-page__question-name";
  questionName.textContent = `Вопрос ${currentId}`;

  const questionText = document.createElement("pre");
  questionText.className = "pass-test-page__question-text";
  questionText.innerHTML = question ? question : "";

  const questionInput = document.createElement("input");
  questionInput.hidden = true;
  questionInput.name = `question-${currentId}`;
  questionInput.value = currentId;

  const answersWrapper = document.createElement("div");
  answersWrapper.className = "pass-test-page__question-answers";

  newQuestion.appendChild(questionName);
  newQuestion.appendChild(questionText);
  newQuestion.appendChild(questionInput);
  newQuestion.appendChild(answersWrapper);

  return [newQuestion, answersWrapper];
}

function createAnswer(question, answers, answer, answerType) {
  const currentId = question.id.split("-")[1];
  const currentAnswer = getDoubleInsideChild(answers);
  let currentAnswerType = null;

  if (answerType) {
    currentAnswerType = answerType;
  } else {
    currentAnswerType = currentAnswer?.type == "radio" ? "radio" : "checkbox";
  }

  const answerWrapper = document.createElement("div");
  answerWrapper.className = "pass-test-page__question-answer-wrapper";

  const choosenAnswer = document.createElement("input");
  choosenAnswer.type = currentAnswerType;
  choosenAnswer.name = `choosenAnswer-${currentId}`;
  choosenAnswer.value = answer ? answer : "";

  const answerText = document.createElement("div");
  answerText.textContent = answer ? answer : "";
  answerText.className = "pass-test-page__question-answer";

  answerWrapper.addEventListener("click", (event) => {
    if (event.target.type !== "checkbox" && event.target.type !== "radio") {
      if (choosenAnswer.checked) {
        choosenAnswer.checked = false;
      } else {
        choosenAnswer.checked = true;
        answerText.classList.add(ACTIVE_ANSWER_CLASS);
      }
    } else {
      answerText.classList.add(ACTIVE_ANSWER_CLASS);
    }

    removeActiveAnswers(answers, answerText);
  });

  const answerInput = document.createElement("input");
  answerInput.hidden = true;
  answerInput.type = "text";
  answerInput.name = `answers-${currentId}`;
  answerInput.value = answer ? answer : "";

  answerWrapper.appendChild(choosenAnswer);
  answerWrapper.appendChild(answerText);
  answerWrapper.appendChild(answerInput);

  return answerWrapper;
}

function removeActiveAnswers(answers) {
  Array.from(answers.childNodes).forEach((answer) => {
    const currentText = answer.childNodes[1];
    const currentInput = answer.childNodes[0];

    if (currentInput.checked === false) {
      currentText.classList.remove(ACTIVE_ANSWER_CLASS);
    }
  });
}

function getDoubleInsideChild(nodeElement) {
  return nodeElement.childNodes?.[0]?.childNodes[0];
}
