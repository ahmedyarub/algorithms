var createObject = function (keysArr, valuesArr) {
    const obj = {};
    for (const keyIndex in keysArr) {
        const key = keysArr[keyIndex];
        if (key in obj) {
            continue;
        }
        obj[key] = valuesArr[keyIndex];
    }
    return obj;
};