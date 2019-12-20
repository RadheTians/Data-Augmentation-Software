let xmin=0,ymin=0,xmax=0,ymax=0;
let xbox,ybox;
let flag=0;
let reader = [];
let a=0;
let left;
let right;
function setup() {
    var canvas = createCanvas(1000, 1000);
    canvas.doubleClicked(setXY);
    left = createButton('Left');
    left.position(300, 290);
    left.mousePressed(leftChange);
    right = createButton('Right');
    right.position(500, 319);
    right.mousePressed(rightChange);
}

function draw() {
    
    if(reader.length != 0 && 0 <= a < reader.length){
        clear();
        image(reader[a], 0,0);
    }
    if(xmin!=0 && ymin!=0 && xmax!=0 && ymax!=0){
        document.getElementById("xmax").value = xmax;
        document.getElementById("ymax").value = ymax;
        c = color('hsla(160, 100%, 50%, 0)');
        fill(c);
        rect(xmin,ymin,xbox,ybox);
        
    }
}

function readImageURL(input) {

    if (input.files) {
        for(var i=0;i<input.files.length;i++){
            reader[i] = loadImage(URL.createObjectURL(input.files[i]));
        }
    }
  
}

function doubleClicked() {

    if(flag==1){
        xmax = mouseX;
        ymax = mouseY;
        xbox = mouseX-xmin;
        ybox = mouseY-ymin;
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

function leftChange(){
    a--;
}

function rightChange(){
    a++;
}