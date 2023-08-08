var compose = function (functions) {
    if (functions.length === 0) {
        return function (x) {
            return x;
        };
    }

    return functions.reduceRight(function (prevFn, nextFn) {
        return function (x) {
            return nextFn(prevFn(x));
        };
    });

};