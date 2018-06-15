function A() {
    this.x = 12;
}

A.prototype.getX = function() {
    return this.x;
};

const a = new A();
const b = new A();

b.x = 6;

a.getX = a.getX.bind(b);
delete a.getX;
console.log(a, a.getX());
console.log(b, b.getX());
