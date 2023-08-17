var cancellable = function (fn, args, t) {
    var timeout = setTimeout(() => fn(...args), t)
    var cancelFn = () => clearTimeout(timeout);

    return cancelFn;
};