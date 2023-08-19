Date.prototype.nextDay = function () {
    const next = this.getTime() + 86400000;
    return new Date(next).toISOString().split("T")[0];
}