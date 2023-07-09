addPageClassName("profile-page");

let cell=document.querySelectorAll('#cell')
let form=document.getElementById('form')
let results=document.getElementById('results')

cell.forEach( cell => 
   cell.addEventListener('click', (event) => {
      if (event.target.innerHTML == 'Настройки профиля') {
         form.style.display = 'flex'
         results.style.display = 'none'
      } 
      if (event.target.innerHTML == 'Пройденные тесты') {
         form.style.display = 'none'
         results.style.display = 'flex'
      }
   }))
