var nextBtn = document.querySelector('.next');
var endBtn = document.querySelector('.endBtn');
var TheQues = document.getElementById('QuizQues');
var timer = document.getElementById('timer');
var topic = document.getElementById('topic')

count = 0;
console.log((quesList));
console.log((topicsList));

TheQues.innerText = "Q"+ (count+1) + ". " +quesList[count];
topic.innerText = topicsList[count];

nextBtn.addEventListener('click',(e)=>{
    if (count<quesList.length-1){
        count += 1;
        TheQues.innerText = "Q"+ (count+1) + ". " +quesList[count];
        topic.innerText = topicsList[count];
        console.log(count+1);
    }
    if(count === quesList.length-1){
        nextBtn.style.display = 'none';
        endBtn.style.display = 'block';
        endBtn.style.color = 'white';
        endBtn.style.backgroundColor = 'green';
    }
});

endBtn.addEventListener('click',()=>{
    window.location.href = 'http://127.0.0.1:5000/submited';
});