var invertObject = function (obj) {
    const resultObj = {};
    for (let key in obj) {
        const val = obj[key].toString();
        if (val in resultObj) {
            resultObj[val] = Array.isArray(resultObj[val]) ? [...resultObj[val], key] :
                [resultObj[val], key.toString()];
        } else {
            resultObj[val] = key.toString();
        }
    }
    return resultObj;
};