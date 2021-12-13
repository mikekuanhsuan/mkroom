class Person {
    constructor(name='noname', age=0) {
        this.name = name;
        this.age = age;
    }

    toJSON() {
        return {
            name: this.name,
            age: this.age,
        };
    }
    toString(){
        return JSON.stringify(this.toJSON());
    }
}

const f1 = a =>a*a;
console.log(f1(6));

module.exports = {Person, f1 };
