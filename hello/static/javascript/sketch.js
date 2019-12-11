let input;
let img;
let xmin=0,ymin=0,xmax=0,ymax=0;
let flag=0;
function setup() {
    var canvas = createCanvas(400, 400);
    canvas.mouseClicked(setXY);
    canvas.id('blah');
    input = createFileInput(readImageURL);
    input.id('image');
    input.class('content');
}
function draw() {
    background(255);
    //image(image,0,0);
    //image(background,100,100);
    if (img) {
        image(img, 0, 0);
    }
    if(xmin!=0 && ymin!=0 && xmax!=0 && ymax!=0){
        document.getElementById("xmax").value = xmax;
        document.getElementById("ymax").value = ymax;
        noStroke();
        c = color('hsla(160, 100%, 50%, 0.5)');
        fill(c);
        rect(xmin,ymin,xmax,ymax);
        print("X min: "+xmin);
        print("Y min: "+ymin);
        print("X max: "+xmax);
        print("Y max: "+ymax);
    }
}

function readImageURL(file) {
  print(file);
  if (file.type === 'image') {
    img = createImg(file.data, '');
    img.hide();
  } else {
    //img = null;
  }
    
   
}
function readBackgroundImageURL(file) {
    //background = loadImage(input.files[0]);
}

function mousePressed() {
    if(flag==1){
        xmax = mouseX-xmin;
        ymax = mouseY-ymin;

    }
    
}
function setXY(){

    if(flag==0){
        flag =1;
        xmin = mouseX;
        ymin = mouseY;
        document.getElementById("xmin").value = xmin;
        document.getElementById("ymin").value = ymin;
    }

}