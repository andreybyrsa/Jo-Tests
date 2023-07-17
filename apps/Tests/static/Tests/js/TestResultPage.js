addPageClassName("test-result-page");

const dataQuestions = document.getElementById("data-questions").textContent;
const dataChoices = document.getElementById("data-choices").textContent;

const JSON_QUESTIONS = JSON.parse(dataQuestions);
const JSON_CHOICES = JSON.parse(dataChoices);

const questionsWrapper = document.getElementById("questions");

let currentQuestions = [];

if (JSON_QUESTIONS.length) {
  Array.from(JSON_QUESTIONS).forEach((questionInfo) => {
    const { id, question, qtype, answers } = questionInfo;
    const answerType = qtype === "single" ? "radio" : "checkbox";

    const [newQuestion, answersWrapper] = createQuestion(
      "test-result-page__question",
      currentQuestions,
      question,
      id
    );

    const currentChoices = JSON_CHOICES ? JSON_CHOICES[id] : [];

    Array.from(answers).forEach((answerInfo, index) => {
      const { is_selected } = currentChoices[index]
      const { answer, is_correct } = answerInfo;

      answersWrapper.appendChild(
        createAnswer(
          "test-result-page__question-answer",
          newQuestion,
          answersWrapper,
          answer,
          answerType,
          is_correct,
          is_selected
        )
      );
    });

    questionsWrapper.appendChild(newQuestion);
  });
}
