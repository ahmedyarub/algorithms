var createInfiniteObject = function () {
    return new Proxy({}, {
        get: (_, prop) => () => prop
    });
};