class User {
    constructor(x, y, name) {
        this.x = x;
        this.y = y;
        this.name = name;
        this.tSize = windowWidth/100;
    }

    draw() {
        noStroke();
        fill(0, 180, 0);
        ellipse(this.x, this.y, userWidth);
        fill(0);
        textAlign(CENTER, CENTER);
        textSize(this.tSize);
        text(this.name, this.x - this.tSize/4, this.y - User.radius);
    }
}

class Car {
    
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.real = true;
    }

    draw() {
        if (this.real) {
            fill(0);
        } else {
            fill(50);
        }
        fill(0, 255, 0);
        image(carImg, this.x, this.y, carWidth, carWidth);
    }
}

