"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function sumTwoArrays(a, b) {
    if (a.length !== b.length)
        throw new Error('Both arrays must be same length.');
    for (var i = 0; i < a.length; i++) {
        a[i] += b[i];
    }
    return a;
}
exports.sumTwoArrays = sumTwoArrays;
//# sourceMappingURL=utils.js.map