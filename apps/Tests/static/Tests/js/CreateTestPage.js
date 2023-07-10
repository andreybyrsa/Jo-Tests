addPageClassName("create-test-page");

const inputTestTitle = document.getElementById("input-test-title");
const inputTestDescription = document.getElementById("input-test-description");
const testTitle = document.getElementById("test-title");
const testDescription = document.getElementById("test-descriprion");

const questionsWrapper = document.getElementById("questions");
const addQuestionButton = document.getElementById("add-question-button");
const addAnswerButton = document.getElementById("add-answer-button");
const toggleAnswerTypeButton = document.getElementById(
  "toggle-answer-type-button"
);
const deleteQuestionButton = document.getElementById("delete-question-button");

const dateCreated = document.getElementById("date-created");
const dateChanged = document.getElementById("date-changed");

const questionsAmount = document.getElementById("questions-amount");

const submitButton = document.getElementById("submit-button");

const QUESTION_ACTIVE_CLASS = "create-test-page__question--active";
const ANSWER_BUTTON_DISABLED_CLASS = "create-test-side-bar__button--disabled";
const TOGGLE_BUTTON_DISABLED_CLASS =
  "create-test-side-bar__toggle-button--disabled";

let currentQuestions = [];
let currentQuestion = null;
let currentAnswers = null;

function getCurrentDate() {
  const date = new Date();

  const year = date.getFullYear();

  let month = date.getMonth() + 1;
  month = month >= 10 ? month : `0${month}`;

  let day = date.getDate();
  day = day >= 10 ? day : `0${day}`;

  return `${day}:${month}:${year}`;
}

dateCreated.textContent = getCurrentDate();

submitButton.addEventListener("click", () => {
  testTitle.value = inputTestTitle.value;
  testDescription.value = inputTestDescription.value;

  questionsWrapper.submit();
});

function disableQuestions() {
  currentQuestions.forEach((question) => {
    if (question.classList.contains(QUESTION_ACTIVE_CLASS))
      question.classList.remove(QUESTION_ACTIVE_CLASS);
  });
}

addQuestionButton.addEventListener("click", () => {
  if (addAnswerButton.classList.contains(ANSWER_BUTTON_DISABLED_CLASS)) {
    addAnswerButton.classList.remove(ANSWER_BUTTON_DISABLED_CLASS);
    addAnswerButton.disabled = false;
  }
  if (toggleAnswerTypeButton.classList.contains(TOGGLE_BUTTON_DISABLED_CLASS)) {
    toggleAnswerTypeButton.classList.remove(TOGGLE_BUTTON_DISABLED_CLASS);
    toggleAnswerTypeButton.disabled = false;
  }
  deleteQuestionButton.style.display = "flex";
  disableQuestions();

  questionsWrapper.appendChild(createNewQuestion());
  questionsAmount.value = currentQuestions.length;
});

addAnswerButton.addEventListener("click", () => {
  currentAnswers.appendChild(createNewAnswer());
});

toggleAnswerTypeButton.addEventListener("click", () => {
  const currentAnswer = currentAnswers.childNodes?.[0]?.childNodes[0];
  const answerType = currentAnswer?.type == "radio" ? "radio" : "checkbox";

  if (currentAnswers.childNodes.length) {
    Array.from(currentAnswers.childNodes).forEach((answerWrapper) => {
      const currentAnswer = answerWrapper.childNodes[0];
      if (answerType == "checkbox") {
        currentAnswer.type = "radio";
      } else {
        currentAnswer.type = "checkbox";
      }
    });
  }
});

deleteQuestionButton.addEventListener("click", () => {
  currentQuestion.remove();
  currentQuestions = currentQuestions.filter(
    (question) => question !== currentQuestion
  );
  questionsAmount.value = currentQuestions.length;

  if (currentQuestions.length == 0) {
    deleteQuestionButton.style.display = "none";

    addAnswerButton.classList.add(ANSWER_BUTTON_DISABLED_CLASS);
    addAnswerButton.disabled = true;

    toggleAnswerTypeButton.classList.add(TOGGLE_BUTTON_DISABLED_CLASS);
    toggleAnswerTypeButton.disabled = true;

    return;
  }

  currentQuestions.forEach((question, index) => {
    const questionName = question.childNodes[0].childNodes[0];
    questionName.textContent = `Вопрос ${index + 1}`;
  });
});

function createNewQuestion() {
  const currentId = currentQuestions.length + 1;
  const questionId = `question-${currentId}`;

  const newQuestion = document.createElement("div");
  newQuestion.id = questionId;
  newQuestion.className = `create-test-page__question ${QUESTION_ACTIVE_CLASS}`;
  newQuestion.onclick = () => focusQuestion(questionId);

  const questionHeader = document.createElement("div");
  questionHeader.className = "create-test-page__question-header";

  const questionName = document.createElement("span");
  questionName.textContent = `Вопрос ${currentQuestions.length + 1}`;

  const questionPointsWrapper = document.createElement("div");
  questionPointsWrapper.className = "create-test-page__question-points";

  const questionPointsText = document.createElement("span");
  questionPointsText.textContent = "Балл(ы)";

  const questionPointsInput = document.createElement("input");
  questionPointsInput.className = "create-test-page__question-points-input";
  questionPointsInput.type = "number";
  questionPointsInput.name = `points-${currentId}`;
  questionPointsInput.defaultValue = 1;
  questionPointsInput.min = 1
  
  questionPointsInput.addEventListener("input", (event) => {
    const currentValue = event.target.value;
    if (!currentValue || currentValue == "e") {
      questionPointsInput.value = "";
    }
    if (+currentValue <= 0) {
      questionPointsInput.value = "";
    }
  });

  questionPointsWrapper.appendChild(questionPointsText);
  questionPointsWrapper.appendChild(questionPointsInput);
  questionHeader.appendChild(questionName);
  questionHeader.appendChild(questionPointsWrapper);

  const questionTextArea = document.createElement("textarea");
  questionTextArea.className = "create-test-page__question-textarea";
  questionTextArea.name = `question-${currentId}`;

  const answersWrapper = document.createElement("div");
  answersWrapper.className = "create-test-page__question-answers";

  newQuestion.appendChild(questionHeader);
  newQuestion.appendChild(questionTextArea);
  newQuestion.appendChild(answersWrapper);

  currentQuestion = newQuestion;
  currentAnswers = answersWrapper;

  currentQuestions.push(newQuestion);

  return newQuestion;
}

function createNewAnswer() {
  const currentId = currentQuestion.id.split("-")[1];
  const currentAnswer = currentAnswers.childNodes?.[0]?.childNodes[0];
  const answerType = currentAnswer?.type == "radio" ? "radio" : "checkbox";

  const answerWrapper = document.createElement("div");
  answerWrapper.className = "create-test-page__question-answer-wrapper";

  const rightAnswer = document.createElement("input");
  rightAnswer.type = answerType;
  rightAnswer.name = `rightAnswers-${currentId}`;

  const answerInput = document.createElement("input");
  answerInput.className = "create-test-page__question-answer";
  answerInput.type = "text";
  answerInput.name = `answers-${currentId}`;

  const answerDeleteButton = document.createElement("i");
  answerDeleteButton.className =
    "bi bi-trash create-test-page__delete-answer-button";

  answerDeleteButton.addEventListener("click", () => {
    answerWrapper.remove();
  });

  answerWrapper.appendChild(rightAnswer);
  answerWrapper.appendChild(answerInput);
  answerWrapper.appendChild(answerDeleteButton);

  answerInput.addEventListener("input", (event) => {
    rightAnswer.value = event.target.value;
  });

  return answerWrapper;
}

function focusQuestion(id) {
  const activeQuestion = currentQuestions.find((question) => question.id == id);

  disableQuestions();
  activeQuestion.classList.add(QUESTION_ACTIVE_CLASS);

  currentQuestion = activeQuestion;
  currentAnswers = Array.from(currentQuestion.childNodes).find(
    (element) => element.className == "create-test-page__question-answers"
  );
}
