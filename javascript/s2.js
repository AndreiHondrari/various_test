

class A {

  constructor() {
    this.x = 111;
  }

  async bla(msg) {
    return new Promise(() => {
      console.log(`CEPL ${msg}`);
      console.log(this.x);
    });
  }

  async doSomething(msg) {
    await this.bla(msg);
  }
}

let a1 = new A();
a1.doSomething("elloo");
