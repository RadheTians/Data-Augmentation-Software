let xmin=0,ymin=0,xmax=0,ymax=0;
let xbox=0,ybox=0;
let flag=0;
let reader = [];
var annotation_list = [];
let a=0;


function setup() {

    var canvas = createCanvas(700, 700);
    canvas.class("center");
    canvas.doubleClicked(setXY);
        

   
}

function draw() {
    // print(reader.length);
    if(reader.length != 0 && 0 <= a && a < reader.length){
        clear();
        // print(a);
        image(reader[a], 0,0);
    }
    if(xmin!=0 && ymin!=0 && xmax!=0 && ymax!=0){
        document.getElementById("xmax").value = xmax;
        document.getElementById("ymax").value = ymax;
        c = color('hsla(200, 100%, 50%, 0)');
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

// function doubleClicked() {

//     if(flag==1){
//         xmax = mouseX;
//         ymax = mouseY;
//         xbox = mouseX-xmin;
//         ybox = mouseY-ymin;
//     }
// }

function setXY(){

    if(flag==0){
        flag =1;
        xmin = mouseX;
        ymin = mouseY;
        document.getElementById("xmin").value = xmin;
        document.getElementById("ymin").value = ymin;
    } else {
        xmax = mouseX;
        ymax = mouseY;
        xbox = mouseX-xmin;
        ybox = mouseY-ymin;
    }

}

function leftChange(){
    if(0 < a){
        var label = document.getElementById("label").value;
        document.getElementById("label").value = "";
        var annot = {"xmin" : xmin, "ymin" : ymin, "xmax" : xmax, "ymax" : ymax, "label" : label, csrfmiddlewaretoken : csrftoken};
        //append(annotation_list,annot);
        a = a-1;
        flag = 0;
        xmin = 0;
        ymin = 0;
        xmax = 0;
        ymax = 0;
        xbox = 0;
        ybox = 0;
        

    }

}

function rightChange(){

    if(a < reader.length){

        var label = document.getElementById("label").value;
        document.getElementById("label").value = "";
        var annot = {"xmin" : xmin, "ymin" : ymin, "xmax" : xmax, "ymax" : ymax, "label" : label, csrfmiddlewaretoken : csrftoken};
        $.post("{% url 'Unread' %}", annot);
        //append(annotation_list,annot);
        a = a+1;
        flag = 0;
        xmin = 0;
        ymin = 0;
        xmax = 0;
        ymax = 0;
        xbox = 0;
        ybox = 0;
    
    }
    
}

function Unread(){

    print(annotation_list);

    var url = "{% url 'Unread' %}";
    var data = {"data" : annotation_list, csrfmiddlewaretoken : csrftoken};
    $.post(url, data);
    print("Thirdnumber");

}