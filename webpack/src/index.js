import _ from "lodash";
import "./index.css";
import MyImg from "./flower.jpg";

const element = document.createElement("p");
element.innerHTML = _.join(["Hello", "Webpack"], "-");
element.classList.add("hello");

const ele_img = new Image();
ele_img.src = MyImg;

console.log(MyImg);

document.body.appendChild(element);
document.body.appendChild(ele_img);
