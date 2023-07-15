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
testTime.textContent = `${test_time}:00`;

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

function createQuestion(question) {
  const currentId = currentQuestions.length + 1;
  const questionId = `question-${currentId}`;

  const newQuestion = document.createElement("div");
  newQuestion.id = questionId;
  newQuestion.className = "pass-test-page__question";

  const questionName = document.createElement("span");
  questionName.className = "pass-test-page__question-name";
  questionName.textContent = `Вопрос ${currentId}`;

  const questionText = document.createElement("div");
  questionText.className = "pass-test-page__question-text";
  questionText.innerText = question ? question : "";

  const questionInput = document.createElement("input");
  questionInput.hidden = true;
  questionInput.name = `question-${currentId}`;
  questionInput.value = question ? question : "";

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

  choosenAnswer.addEventListener("input", () =>
    chooseAnswer(answers, answerText)
  );

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

function chooseAnswer(answers, answerText) {
  Array.from(answers.childNodes).forEach((text) => {
    const currentText = text.childNodes[1];

    if (currentText.classList.contains(ACTIVE_ANSWER_CLASS)) {
      currentText.classList.remove(ACTIVE_ANSWER_CLASS);
    }
  });

  answerText.classList.add(ACTIVE_ANSWER_CLASS);
}

function getDoubleInsideChild(nodeElement) {
  return nodeElement.childNodes?.[0]?.childNodes[0];
}
