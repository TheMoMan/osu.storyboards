"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function normaliseValue(value, array) {
    return (value - Math.min.apply(Math, array)) / (Math.max.apply(Math, array) - Math.min.apply(Math, array));
}
exports.normaliseValue = normaliseValue;
function normaliseIndex(index, array) {
    return normaliseValue(array[index], array);
}
exports.normaliseIndex = normaliseIndex;
//# sourceMappingURL=utils.js.map