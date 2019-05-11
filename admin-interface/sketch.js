let carWidth;
let userWidth;
let user;
let car = {x: 50, y: 50};
let users = [];
let cars = [];

// If demo this should be true
let demo = true;

function setup() {
    bg = loadImage('map.png');
    carImg = loadImage('car.png');
    createCanvas(windowWidth, windowHeight);
    carWidth = windowWidth / 30;
    User.radius = windowWidth / 60;
    userWidth = User.radius;

    setInterval(setUserWidth, 50);

}

function setUserWidth() {
    userWidth -= 0.5; 
    userWidth = (userWidth < User.radius/2) ? User.radius : userWidth;
}

function draw() {
    background(bg);

    // Draw cars
    for (let i = 0; i < cars.length; i++) {
        cars[i].draw();
    }

    // Draw users
    for (let i = 0; i < users.length; i++) {
        users[i].draw();
    }

}
let i = 0;
function mouseClicked() {
    if (demo) {
        if (cars.length < 2) {
            cars.push(new Car(mouseX, mouseY));
        } else {
            let names = ["James", "Tyler", "Anna", "Jessica"];
            users.push(new User(mouseX, mouseY, names[i]));
            i++;
        }
    }
}

function getUpdate() {
    const url = (demo) ? 'localhost:5000/api' : 'http://carpool.serveo.net/api';
    const xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myArr = JSON.parse(this.responseText);
            console.log(myArr);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}
