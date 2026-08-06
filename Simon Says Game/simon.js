let gameSeq = [];
let userSeq = [];
let started = false;
let level = 0;
let levelText = document.querySelector("h2");

document.addEventListener("keypress" , function(){
    if(!started){
        console.log("The game has started!");
        started = true;

        levelUp();
    }

});

function levelUp(){
    userSeq = [];
    level++;
    levelText.innerText = "Level " + level;

    let btns = ["black", "pink", "purple", "gray"];
    let idx = Math.floor(Math.random() * 4);
    console.log(idx);

    let randomColor = btns[idx];
    console.log(randomColor);
    gameSeq.push(randomColor);

    let randomBtn = document.querySelector(`.${randomColor}`);
    randomBtn.classList.add("flash");

    setTimeout(function() {
    randomBtn.classList.remove("flash");
    }, 250);


};

let container = document.querySelector(".container");
container.addEventListener("click", function(event){
    let userClick = event.target.classList[1];
    userSeq.push(userClick);

    let clickedBtn = event.target;
    clickedBtn.classList.add("flash");

    setTimeout(function() {
        clickedBtn.classList.remove("flash");
    }, 250);

    checkAnswer(userSeq.length - 1);
});

function checkAnswer(idx) {
    if (userSeq[idx] === gameSeq[idx]) {
        if (userSeq.length === gameSeq.length) {
            setTimeout(levelUp, 1000);
        }
        
    } else {
        gameOver();
    }
};

function gameOver() {
    levelText.innerText = "Game Over! Press any key to restart.";
    console.log("Game Over!");

    let body = document.querySelector("body");
    body.classList.add("game-over-flash");

    setTimeout(function() {
        body.classList.remove("game-over-flash");
    }, 250);

    started = false;
    level = 0;
    gameSeq = [];
}













