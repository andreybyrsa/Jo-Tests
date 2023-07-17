addPageClassName("test-result-page");

const dataQuestions = document.getElementById("data-questions").textContent;
const dataChoices = document.getElementById("data-choices").textContent;

const JSON_QUESTIONS = JSON.parse(dataQuestions);
const JSON_CHOICES = JSON.parse(dataChoices);

const questionsWrapper = document.getElementById("questions");

const testPoints = document.getElementById("test-points");
testPoints.textContent = "0/" + testPoints.textContent;

let currentQuestions = [];

if (JSON_QUESTIONS.length) {
  Array.from(JSON_QUESTIONS).forEach((questionInfo) => {
    const { id, question, qtype, max_points, answers } = questionInfo;
    const answerType = qtype === "single" ? "radio" : "checkbox";

    const [newQuestion, answersWrapper] = createQuestion(
      "test-result-page__question",
      currentQuestions,
      question,
      id,
      max_points
    );

    const currentChoices = JSON_CHOICES ? JSON_CHOICES[id] : [];
    let achivedPoints = null;

    Array.from(answers).forEach((answerInfo, index) => {
      const { is_selected } = currentChoices[index];
      achivedPoints = currentChoices[answers.length];
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

    const questionPoints = document.getElementById(`points-${id}`);
    questionPoints.textContent =
      String(achivedPoints) + questionPoints.textContent;

    const currentPoints = testPoints.textContent.split("/");
    testPoints.textContent =
      `${+currentPoints[0] + achivedPoints}/` + currentPoints[1];
  });
}
