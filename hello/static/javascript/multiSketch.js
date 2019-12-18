let img;
let xmin=0,ymin=0,xmax=0,ymax=0;
let xbox,ybox;
let flag=0;
let reader = [];
let x=0;
function setup() {
    var canvas = createCanvas(1000, 1000);
    canvas.doubleClicked(setXY);
    img = createImg('', '');
    img.id('img');
    img.hide();
    
}

function draw() {

    if(reader.length!=0){
        print(reader);
        reader[x].onload = function (e) {
            createImg(e.target.result,'');
            $('#img').attr('src', e.target.result); 
        };
        image(img, 0, 0);
        
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
            reader[i] = new FileReader();
            reader[i].readAsDataURL(input.files[i]);
        }
        
    }
}

function doubleClicked() {
    x++;
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
