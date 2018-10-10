var xoff = 0.0;
var xincrement = 0.01;

function setup() {
  createCanvas(710, 400);
  background(0);
  noStroke();
}

function draw() {
  fill(0, 10);
  rect(0,0,width,height);
	
	if (mouseIsPressed){
  var n = noise(xoff)*height;
  xoff -= xincrement;
	}
	else {
		var n = random(0,width);
	}
	

  fill(300);
  ellipse(n,height/2, 2, 230);
}
