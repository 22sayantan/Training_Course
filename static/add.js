var ele = document.querySelectorAll('input[type="radio"]');
var form1 = document.querySelector('.add_course');
var form2 = document.querySelector('.add_course_module');

ele.forEach(rbtn => {
    rbtn.addEventListener('change', event =>{
        course_name = event.target.value;
        if(course_name === 'add_course'){
            if(form2.style.display = 'block'){
                form2.style.display = 'none';
            }
            form1.style.display = 'block';
        }
        else if(course_name === 'add_course_module'){
            if(form1.style.display = 'block'){
                form1.style.display = 'none';
            }
            form2.style.display = 'block';
        }
    });
});
