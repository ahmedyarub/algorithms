var chunk = function (arr, size) {
    var chunkedArray = [];
    var index = 0;

    while (index < arr.length) {
        chunkedArray.push(arr.slice(index, index + size));
        index += size;
    }

    return chunkedArray;
}