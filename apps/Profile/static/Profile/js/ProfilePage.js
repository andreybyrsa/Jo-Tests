addPageClassName("profile-page");

const [profileModal, openProfileModal, closeProfileModal] = useModal(
  "profile-modal",
  null,
  null
);

const [editGroupModal, openEditGroupModal, closeEditGroupModal] = useModal(
  "modal-edit-group",
  null,
  null
);

const groups = document.getElementById('data-groups').textContent
const JSON_GROUPS = JSON.parse(groups)
const nameGroup = document.getElementById('group-input')
const nameStudents = document.querySelectorAll('.modal-edit-group__list-checkbox')
const deleteGroup = document.getElementById('delete-group')
const editButton = document.getElementById('edit-button')

function openGroupModal(groupIndex) {
  openEditGroupModal()
  const currentGroup = Array.from(JSON_GROUPS).find( info => info.index == groupIndex )
  const {groupname, index, students} = currentGroup
  nameGroup.value = groupname
  Array.from(nameStudents).forEach( nameStudent => {
    const isExistStudents = students.find( student => student == nameStudent.value )
    if (isExistStudents) {
      nameStudent.checked = true
    } else {
      nameStudent.checked = false
    }
  })
  deleteGroup.href = 'delete-group/' + index
  editButton.value = index
}


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

const createInput = document.getElementById("create-input");
const editInput = document.getElementById("edit-input");
const addStudents = document.querySelectorAll('.profile-page__addgroup-students')
const editStudents = document.querySelectorAll('.modal-edit-group__list-students')

createInput.addEventListener("input", (event) => {
  searchByChildNodes(event, addStudents, "profile-page__addgroup-list-name");
});

editInput.addEventListener("input", (event) => {
  searchByChildNodes(event, editStudents, "modal-edit-group__list-name");
});
