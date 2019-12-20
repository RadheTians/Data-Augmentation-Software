let img;
let xmin=0,ymin=0,xmax=0,ymax=0;
let xbox,ybox;
let flag=0;
let reader = [];
let abc;
let a=0;
function setup() {
    var canvas = createCanvas(1000, 1000);
    canvas.doubleClicked(setXY);
    img = createImg('', '');
    img.id('img');
    img.hide();
    
}

function draw() {
    
    if(reader.length!=0){
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
   
  	// if (input.files) {
    //     for(var i=0;i<input.files.length;i++){
    //         reader[i] = new FileReader();
    //         reader[i].onload = function (e) {
    //             $('#img').attr('src', e.target.result);
    //         };
    //         reader[i].readAsDataURL(input.files[i]);
    //         print(input.files[i]);
    //         var k = loadImage(input.files[i].src);
    //     }
    //     image(k, 0,0);
        
    // }
//   var files   = document.querySelector('#image').files;
//   print(files[8]);
//   function readAndPreview(file) {

//     // Make sure `file.name` matches our extensions criteria
//     if ( /\.(jpe?g|png|gif)$/i.test(file.name) ) {
//       var reader = new FileReader();

//       reader.addEventListener("load", function () {
//             abc =loadImage(this.result);
            
//       }, false);
//       input[i]=abc;
//       print(i);
//       i++;
//       reader.readAsDataURL(file);
//     }

//   }

//   if (files) {
//     [].forEach.call(files, readAndPreview);
//   }
}

function doubleClicked() {

    if(flag==1){
        a++;
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
