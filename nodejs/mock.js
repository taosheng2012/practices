const log = console.log;

// ==================================================
const Mock = require("mockjs");

/*
Mock.js 的语法规范包括两部分：

数据模板定义规范（Data Template Definition，DTD）
数据占位符定义规范（Data Placeholder Definition，DPD）
*/

// name|rule : value
const arr = [
    // typeof value === string
    {
        "name1|0-10": "Hello",
        "name2|3": "Hello"
    },

    // typeof value === number
    {
        "num1|+1": 1,
        "num2|10-100": 1,
        "num3|100-500.1-3": 1,
        "num4|100-500.2": 1
    },

    // typeof vale === boolean
    {
        "num1|1": true,
        "num2|1-3": true
    },

    // object
    {
        "num1|2": { name: "John", age: 24, gender: "male" },
        "num2|1-3": { name: "John", age: 24, gender: "male" }
    },

    // Array
    {
        "num1|1": [1, 2, 3, 4, 5],
        "num2|+1": [1, 2, 3, 4, 5],
        "num3|1-3": [1, 2, 3, 4, 5],
        "num4|2": [1, 2, 3, 4, 5]
    },

    // Function
    {
        num1: () => 3 * 2
    },

    // RegExp
    {
        num1: /hello/,
        num2: /^h(e|o)/,
        num3: /p[a-d]$/
    },

    // Data Placeholder Definition
    {
        num1: "@FIRST",
        num2: "@LAST",
        num3: "@num1 @num2"
    }
];

log(arr.map((item, index) => Mock.mock(item)));
