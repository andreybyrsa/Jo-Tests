addPageClassName("auth-page");

const selection = document.querySelectorAll("#selection");

selection.forEach((selection) => {
  selection.addEventListener("change", (event) => {
    if (event.target.value == "student") {
      selection.style.width = "124px";
    }
    if (event.target.value == "teacher") {
      selection.style.width = "186px";
    }
    if (event.target.value == "author") {
      selection.style.width = "106px";
    }
  });
});

const open_modal = document.getElementById("open_modal");
const modal = document.getElementById("modal");
const close_modal = document.getElementById("close modal");

open_modal.addEventListener("click", (event) => {
  modal.classList.remove("reg-page__form--close");
  modal.classList.add("reg-page__form--open");
  open_modal.style.display = "none";
});

function closeRegPageModal() {
  modal.classList.add("reg-page__form--close");
  setTimeout(() => {
    modal.classList.remove("reg-page__form--open");
    open_modal.style.display = "flex";
  }, 250);
}

close_modal.addEventListener("click", (event) => {
  closeRegPageModal();
});

modal.addEventListener("click", (event) => {
  if (event.target.id == "modal") {
    closeRegPageModal();
  }
});
