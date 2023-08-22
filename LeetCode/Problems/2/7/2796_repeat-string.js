String.prototype.replicate = function (times) {
    return times === 1 ? this : this + this.replicate(times - 1)
}