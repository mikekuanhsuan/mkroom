
const person2 = require(__dirname + '/person2');

const p1 = new person2.Person('bill', 22);
const p3 = new person2.Person;



console.log( p1.toJSON() );
console.log( '' + p1 );
console.log( person2.f1(8) );

console.log( p3.toJSON() );

