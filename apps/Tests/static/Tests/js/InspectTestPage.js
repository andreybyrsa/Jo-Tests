addPageClassName("inspect-test-page");

const dataQuestions = document.getElementById("data-questions").textContent;

const JSON_QUESTIONS = JSON.parse(dataQuestions);

const questionsWrapper = document.getElementById("questions");

let currentQuestions = [];

if (JSON_QUESTIONS.length) {
  Array.from(JSON_QUESTIONS).forEach((questionInfo) => {
    const { question, id, qtype, answers } = questionInfo;
    const answersType = qtype == "single" ? "radio" : "checkbox";

    const [newQuestion, answerWrapper] = createQuestion(
      "inspect-test-page__question",
      currentQuestions,
      question,
      id
    );

    Array.from(answers).forEach((answerInfo) => {
      const { answer, is_correct } = answerInfo;

      answerWrapper.appendChild(
        createAnswer(
          "inspect-test-page__question-answer",
          newQuestion,
          answerWrapper,
          answer,
          answersType,
          is_correct
        )
      );
    });

    questionsWrapper.appendChild(newQuestion);
  });
}
