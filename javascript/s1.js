

function doSomething() {
  console.log("BEFORE doSomething promise");
  return new Promise(function(resolutionFunc) {
    setTimeout(() => {
      console.log("executed doSomething promise");
      resolutionFunc();
    }, 1000)
  });
}

function doSomethingElse() {
  console.log("BEFORE doSomethingElse promise");
  return new Promise(function(resolutionFunc) {
    setTimeout(() => {
      console.log("executed doSomethingElse promise");
      resolutionFunc();
    }, 3000)
  });
}


function doAll() {
  Promise.all([
    doSomething(),
    doSomethingElse()
  ]).then(() => {
    console.log("FINALLY FINISHED!");
  })
}

doAll();
