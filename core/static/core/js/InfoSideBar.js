const sideBarContent = document.getElementById("side-bar-content");
const sideBarTitle = document.getElementById("side-bar-title");
const sideBarDescription = document.getElementById("side-bar-description");
const sideBarTimeCreated = document.getElementById("side-bar-time-created");
const sideBarTimeUpdated = document.getElementById("side-bar-time-updated");
const sideBarImage = document.getElementById("side-bar-image");

const sideBarLinks = document.querySelectorAll(
  '[class~="info-side-bar__button"]'
);

let currentJsonData = null;
let currentItems = null;
let currentItemClassName = null;
let activeClassName = null;

let linksURLS = Array.from(sideBarLinks).map((link) =>
  link.getAttribute("href")
);

function useInfoSideBar(data, items, itemClassName) {
  currentJsonData = data;
  currentItems = items;
  currentItemClassName = itemClassName;
  activeClassName = `${itemClassName}--active`;
}

function getCurrentDate(testDate) {
  const date = new Date(testDate);

  const year = date.getFullYear();

  let month = date.getMonth();
  month = month >= 10 ? month : `0${month}`;

  let day = date.getDay();
  day = day >= 10 ? day : `0${day}`;

  return `${day}:${month}:${year}`;
}

function removeActiveClassName(items) {
  Array.from(items).forEach((element) => {
    if (element.classList.contains(activeClassName)) {
      element.classList.remove(activeClassName);
    }
  });
}

function openSideBar(itemId) {
  const currentData = currentJsonData[itemId];
  const { title, description, time_create, time_update, slug } = currentData;

  Array.from(sideBarLinks).forEach((link, index) => {
    link.href = linksURLS[index] + slug
  });

  sideBarImage.style.display = "none";
  sideBarContent.style.display = "flex";

  removeActiveClassName(currentItems);
  const currentItem = currentItems[itemId];
  currentItem.classList.add(activeClassName);

  sideBarTitle.textContent = title;
  sideBarDescription.textContent = description;

  const currentCreateDate = getCurrentDate(time_create);
  const currentUpdateDate = getCurrentDate(time_update);

  if (currentCreateDate == currentUpdateDate) {
    sideBarTimeCreated.textContent = currentCreateDate;
    sideBarTimeUpdated.textContent = "Не изменено";
  } else {
    sideBarTimeCreated.textContent = currentCreateDate;
    sideBarTimeUpdated.textContent = currentUpdateDate;
  }
}
