Array.prototype.upperBound = function (target) {
    let left = 0, right = this.length - 1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        if (this[mid] <= target) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return --left >= 0 && this[left] === target ? left : -1;
};