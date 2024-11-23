let course_form = document.querySelector('#new_course')
let module_form = document.getElementById('new_module')


function getSelectedColor() {
    // Get all radio buttons with the name "color"
    const radios = document.querySelectorAll('input[name="color"]');
  
    // Find the checked radio button
    let selectedRadio;
    for (const radio of radios) {
      if (radio.checked) {
        selectedRadio = radio;
        break;
      }
    }
  
    // If a radio button is selected, display its value
    if (selectedRadio.value === 'course') {
      course_form.style.display = 'block';
      module_form.style.display = 'none';
    } else if(selectedRadio.value === 'module') {
      course_form.style.display = 'none';
      module_form.style.display = 'block';     
    }
  }
  