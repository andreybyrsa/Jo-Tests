let pageLayoutSideBar = document.querySelector(".page-layout__left-side-bar");
let pageLayoutContentWrapper = document.querySelector(
  ".page-layout__content-wrapper"
);

let headerTabs = document.querySelectorAll(".header__tab");

if (pageLayoutSideBar.children.length) {
  pageLayoutContentWrapper.style.gap = "20px";
}

let modalLayout = document.getElementById("modal-layout");

const OPENING_MODAL_LAYOUT_CLASS = "page-layout-modal--opened";
const CLOSING_MODAL_LAYOUT_CLASS = "page-layout-modal--closed";

function setActiveLink() {
  const currentLinks = Array.from(headerTabs);
  const currentURL = window.location.pathname;

  currentLinks.forEach((link) => {
    if (link.getAttribute("href") == currentURL) {
      link.classList.add("header__tab--active");
    }
  });
}
setActiveLink();

function openModal() {
  modalLayout.style.display = "grid";
  modalLayout.classList.add(OPENING_MODAL_LAYOUT_CLASS);
}

function closeModal() {
  modalLayout.classList.add(CLOSING_MODAL_LAYOUT_CLASS);
  setTimeout(() => {
    modalLayout.classList.remove(OPENING_MODAL_LAYOUT_CLASS);
    modalLayout.classList.remove(CLOSING_MODAL_LAYOUT_CLASS);
    modalLayout.style.display = "none";
  }, 300);
}

modalLayout.addEventListener("click", (event) => {
  if (event.target.id === "modal-layout") {
    closeModal();
  }
});

function addPageClassName(className) {
  let pageLayoutElements = Array.from(
    document.querySelectorAll("[class^=page-layout]")
  ).slice(1);

  pageLayoutElements.forEach((element) => {
    let currentClassName = element.className;
    let childClassName = element.className.split("__")[1];

    if (childClassName) {
      element.className = `${className}__${childClassName} ${currentClassName}`;
    } else {
      element.className = `${className} ${currentClassName}`;
    }
  });
}

function getCurrentDate(testDate) {
  let date = testDate ? new Date(testDate) : new Date();

  const year = date.getFullYear();

  let month = date.getMonth() + 1;
  month = month >= 10 ? month : `0${month}`;

  let day = date.getDate();
  day = day >= 10 ? day : `0${day}`;

  let hours = date.getHours();
  hours = hours >= 10 ? hours : `0${hours}`;

  let minutes = date.getMinutes();
  minutes = minutes >= 10 ? minutes : `0${minutes}`;

  return `${day}.${month}.${year} ${hours}:${minutes}`;
}

function searchByChildNodes(event, childNodes, searchedItem) {
  const searchedValue = event.target.value.toLowerCase();

  console.log(childNodes[0].childNodes);
  Array.from(childNodes).forEach((childNode) => {
    const currentNode = Array.from(childNode.childNodes).find(
      (node) => node.className === searchedItem
    );

    const currentValue = currentNode?.textContent.toLowerCase();

    if (currentValue?.includes(searchedValue)) {
      childNode.style.display = "flex";
    } else {
      childNode.style.display = "none";
    }
  });
}
