const selection = document.getElementById('selection')

selection.addEventListener('change', (event) => {
   if (event.target.value == 'student') {
      selection.style.width = '97px'
    }
    if (event.target.value == 'teacher') {
      selection.style.width = '147px'
    }
    if (event.target.value == "author") {
      selection.style.width = "85px";
    }
})