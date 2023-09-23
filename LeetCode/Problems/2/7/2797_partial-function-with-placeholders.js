var partial = function (F, A) {
    return (...R) => F(...A.map(x => x == '_' ? R.shift() : x).concat(R))
};