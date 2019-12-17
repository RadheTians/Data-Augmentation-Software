let img;
let xmin=0,ymin=0,xmax=0,ymax=0;
let xbox,ybox;
let flag=0;

function setup() {
    var canvas = createCanvas(1000, 1000);
    canvas.doubleClicked(setXY);
    img = createImg('', '');
    img.id('img');
    img.hide();
}

function draw() {

    if (img) {
        image(img, 0, 0);
    }

    if(xmin!=0 && ymin!=0 && xmax!=0 && ymax!=0){
        document.getElementById("xmax").value = xmax;
        document.getElementById("ymax").value = ymax;
        noStroke();
        c = color('hsla(160, 100%, 50%, 0.5)');
        fill(c);
        rect(xmin,ymin,xbox,ybox);
        
    }
}

function readImageURL(input) {

  	if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#img').attr('src', e.target.result); 
            };
            reader.readAsDataURL(input.files[0]);
        }
}

function readBackgroundImageURL(file) {

 	if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#img').attr('src', e.target.result); 
            };
            reader.readAsDataURL(input.files[0]);
            
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
