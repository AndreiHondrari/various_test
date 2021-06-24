

class InputBox extends HTMLInputElement {

  constructor() {
    super();

    let initialText = this.getAttribute("data-initial-text");
    console.log(`Init: ${initialText}`);
  }
}


export {
  InputBox,
}
