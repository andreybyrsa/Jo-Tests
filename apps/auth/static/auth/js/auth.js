addPageClassName('auth-page')

const selection = document.getElementById('selection')

selection.addEventListener('change', (event) => {
   if (event.target.value == 'student') {
      selection.style.width = '124px'
    }
    if (event.target.value == 'teacher') {
      selection.style.width = '185px'
    }
    if (event.target.value == "author") {
      selection.style.width = "105px";
    }
})