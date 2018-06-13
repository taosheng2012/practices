const log = console.log;

// ==================================================
const Mock = require("mockjs");

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
    }
];

log(arr.map((item, index) => Mock.mock(item)));
