addPageClassName('auth-page')

const selection = document.querySelectorAll('#selection')

selection.forEach( selection => {
   selection.addEventListener('change', (event) => {
      if (event.target.value == 'student') {
         selection.style.width = '124px'
       }
       if (event.target.value == 'teacher') {
         selection.style.width = '186px'
       }
       if (event.target.value == "author") {
         selection.style.width = "106px";
       }
   })
})


const open_modal = document.getElementById('open_modal')
const modal = document.getElementById('modal')
const close_modal = document.getElementById('pidaras pidarasina')

open_modal.addEventListener('click', (event) => {
   modal.classList.remove('reg-page__form--close')
   modal.classList.add('reg-page__form--open')
   open_modal.style.display = 'none'
})

close_modal.addEventListener('click', (event) => {
   function close(){  
      modal.classList.remove('reg-page__form--open') 
      open_modal.style.display = 'flex'
   }  
   modal.classList.add('reg-page__form--close')
   setTimeout(close, 250)
})
