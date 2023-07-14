addPageClassName("profile-page");

const [profileModal, openProfileModal, closeProfileModal] = useModal(
  "profile-modal",
  null,
  null
);

const [editGroupModal, openEditGroupModal, closeEditGroupModal] = useModal(
  "profile-page__addgroup",
  null,
  null
);

// const groups = document.querySelectorAll('.profile-page__listgroup-group')

// function openEditGroupModal(itemId) {
//   console.log(itemId)
// }



const form = document.getElementById("form");
const results = document.getElementById("tests");
const addgroup = document.getElementById("addgroup");
const listgroup = document.getElementById("listgroup");

const cell = document.querySelectorAll(".profile-page__cell");

const active = "profile-page__cell--active";
const disabled = "profile-page__cell--disabled";

Array.from(cell)[0]?.classList.add(active);
Array.from(cell)[1]?.classList.add(disabled);
Array.from(cell)[2]?.classList.add(disabled);

function activeCell(id) {
  Array.from(cell)[id].classList.add(active);
  Array.from(cell)[id].classList.remove(disabled);
}

function disabledCell(id) {
  Array.from(cell)[id].classList.add(disabled);
  Array.from(cell)[id].classList.remove(active);
}

function toggleContent(id) {
  if (cell.length == 2) {
    if (id == 0) {
      activeCell(0);
      disabledCell(1);
    }
    if (id == 1) {
      activeCell(1);
      disabledCell(0);
    }
  }
  if (cell.length == 3) {
    if (id == 0) {
      activeCell(0);
      disabledCell(1);
      disabledCell(2);
    }
    if (id == 1) {
      activeCell(1);
      disabledCell(0);
      disabledCell(2);
    }
    if (id == 2) {
      activeCell(2);
      disabledCell(1);
      disabledCell(0);
    }
  }
}

function changeContent(itemId) {
  if (Array.from(cell)[itemId].innerText == "Настройки профиля") {
    toggleContent(itemId);
    form.style.display = "flex";
    results.style.display = "none";
    addgroup.style.display = "none";
    listgroup.style.display = "none";
  }
  if (Array.from(cell)[itemId].innerText == "Пройденные тесты") {
    toggleContent(itemId);
    form.style.display = "none";
    results.style.display = "flex";
    addgroup.style.display = "none";
    listgroup.style.display = "none";
  }
  if (Array.from(cell)[itemId].innerText == "Добавить группу") {
    toggleContent(itemId);
    form.style.display = "none";
    results.style.display = "none";
    addgroup.style.display = "flex";
    listgroup.style.display = "none";
  }
  if (Array.from(cell)[itemId].innerText == "Список групп") {
    toggleContent(itemId);
    form.style.display = "none";
    results.style.display = "none";
    addgroup.style.display = "none";
    listgroup.style.display = "flex";
  }
}

const profilePicture = document.getElementById("profile-picture");

const fileInput = document.getElementById("image-input");

profilePicture.addEventListener("click", function () {
  fileInput.click();
});

fileInput.addEventListener("change", function (event) {
  const selectedFile = URL.createObjectURL(event.target.files[0]);

  if (selectedFile) {
    profilePicture.src = selectedFile;
  }
});

const searchInput = document.getElementById("login-input");
const students = document.querySelectorAll('.profile-page__addgroup-students')

searchInput.addEventListener("input", (event) => {
  searchByChildNodes(event, students, "profile-page__addgroup-list-name");
});
