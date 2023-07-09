addPageClassName("profile-page");

const form = document.getElementById('form')
const results = document.getElementById('results')
const cell = document.querySelectorAll('.profile-page__cell')
const active = 'profile-page__cell--active'
const disabled = 'profile-page__cell--disabled'

Array.from(cell)[0].classList.add(active)
Array.from(cell)[1].classList.add(disabled)

function activeCell(id) {
   Array.from(cell)[id].classList.add(active)
   Array.from(cell)[id].classList.remove(disabled)
}

function disabledCell(id) {
   Array.from(cell)[id].classList.add(disabled)
   Array.from(cell)[id].classList.remove(active)
}

function toggleContent(id) {
   if (id == 0) {
      activeCell(0)
      disabledCell(1)
   } else {
      activeCell(1)
      disabledCell(0)
   }
}

function changeContent(itemId) {

   if (itemId == '0') {
      toggleContent(itemId)
      form.style.display = 'flex'
      results.style.display = 'none'
   } else {
      toggleContent(itemId)
      form.style.display = 'none'
      results.style.display = 'flex'
   }
}