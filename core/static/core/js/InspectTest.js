function createQuestion(className, currentQuestions, question, id, max_points) {
  const currentId = currentQuestions.length + 1;
  const questionId = `question-${currentId}`;

  const newQuestion = document.createElement("div");
  newQuestion.id = questionId;
  newQuestion.className = className;

  const questionHeader = document.createElement("div");
  questionHeader.className = `${className}-header`;

  const questionName = document.createElement("span");
  questionName.textContent = `Вопрос ${currentId}`;

  questionHeader.appendChild(questionName);

  if (max_points) {
    const questionPoints = document.createElement("span");
    questionPoints.id = `points-${id}`
    questionPoints.textContent = `/${max_points} балл`;

    questionHeader.appendChild(questionPoints);
  }

  const questionText = document.createElement("pre");
  questionText.className = `${className}-text`;
  questionText.innerHTML = question ? question : "";

  const questionInput = document.createElement("input");
  questionInput.hidden = true;
  questionInput.name = `question-${currentId}`;
  questionInput.value = id;

  const answersWrapper = document.createElement("div");
  answersWrapper.className = `${className}-answers`;

  newQuestion.appendChild(questionHeader);
  newQuestion.appendChild(questionText);
  newQuestion.appendChild(questionInput);
  newQuestion.appendChild(answersWrapper);

  currentQuestions.push(newQuestion);

  return [newQuestion, answersWrapper];
}

function createAnswer(
  className,
  question,
  answers,
  answer,
  answerType,
  isRightAnswer,
  choice
) {
  const activeClassName = `${className}--active`;
  const successClassName = `${className}--success`;
  const dangerClassName = `${className}--danger`;

  const currentId = question.id.split("-")[1];
  const currentAnswer = getDoubleInsideChild(answers);
  let currentAnswerType = null;

  if (answerType) {
    currentAnswerType = answerType;
  } else {
    currentAnswerType = currentAnswer?.type == "radio" ? "radio" : "checkbox";
  }

  const answerWrapper = document.createElement("button");
  answerWrapper.className = `${className}-wrapper`;
  answerWrapper.type = "button";

  const choosenAnswer = document.createElement("input");
  choosenAnswer.type = currentAnswerType;
  choosenAnswer.name = `choosenAnswer-${currentId}`;
  choosenAnswer.value = answer ? answer : "";

  const answerText = document.createElement("div");
  answerText.textContent = answer ? answer : "";
  answerText.className = className;

  answerWrapper.addEventListener("click", (event) => {
    if (event.target.type !== "checkbox" && event.target.type !== "radio") {
      if (choosenAnswer.checked) {
        choosenAnswer.checked = false;
      } else {
        choosenAnswer.checked = true;
        answerText.classList.add(activeClassName);
      }
    } else {
      answerText.classList.add(activeClassName);
    }

    removeActiveAnswers(answers, activeClassName);
  });

  if (isRightAnswer && choice === undefined) {
    answerText.classList.add(activeClassName);
    answerWrapper.click();
  } else if (isRightAnswer && choice !== undefined) {
    answerText.classList.add(successClassName);
    console.log(1)
  }

  if (choice) {
    answerWrapper.click();

    if (choice !== isRightAnswer) {
      answerText.classList.add(dangerClassName);
    }
  }

  if (isRightAnswer !== undefined) {
    answerWrapper.disabled = true;
    choosenAnswer.disabled = true;
  }

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

function removeActiveAnswers(answers, activeClassName) {
  Array.from(answers.childNodes).forEach((answer) => {
    const currentText = answer.childNodes[1];
    const currentInput = answer.childNodes[0];

    if (currentInput.checked === false) {
      currentText.classList.remove(activeClassName);
    }
  });
}

function getDoubleInsideChild(nodeElement) {
  return nodeElement.childNodes?.[0]?.childNodes[0];
}
