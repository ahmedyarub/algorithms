var delayAll = function (functions, ms) {
    var delayedFunctions = [];

    for (var i = 0; i < functions.length; i++) {
        (function (index) {
            delayedFunctions.push(function () {
                return new Promise(function (resolve) {
                    setTimeout(function () {
                        resolve(functions[index]());
                    }, ms);
                });
            });
        })(i);
    }

    return delayedFunctions;
};