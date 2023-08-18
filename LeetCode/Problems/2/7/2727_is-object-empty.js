var isEmpty = function (obj) {
    for (const _ in obj) return false;
    return true;
};