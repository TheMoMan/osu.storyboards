"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var utils_1 = require("./utils");
var Osbject = /** @class */ (function () {
    function Osbject(osbjs) {
        var _a, _b, _c, _d, _e, _f, _g;
        if (!osbjs.fileName)
            throw new Error('File name not given.');
        var startTime = osbjs.startTime ? osbjs.startTime : 0;
        this._x = {
            value: (_a = osbjs.x, (_a !== null && _a !== void 0 ? _a : 320)),
            time: startTime,
        };
        this._y = {
            value: (_b = osbjs.y, (_b !== null && _b !== void 0 ? _b : 240)),
            time: startTime,
        };
        this._scale = {
            value: (_c = osbjs.scale, (_c !== null && _c !== void 0 ? _c : 1)),
            time: startTime,
        };
        this._fade = {
            value: (_d = osbjs.fade, (_d !== null && _d !== void 0 ? _d : 1)),
            time: startTime,
        };
        this._rotation = {
            value: (_e = osbjs.rotation, (_e !== null && _e !== void 0 ? _e : 0)),
            time: startTime,
        };
        this._colour = {
            value: (_f = osbjs.colour, (_f !== null && _f !== void 0 ? _f : [255, 255, 255])),
            time: startTime,
        };
        this._vector = {
            value: (_g = osbjs.vector, (_g !== null && _g !== void 0 ? _g : [1, 1])),
            time: startTime,
        };
        var fileName = osbjs.fileName;
        var layer = osbjs.layer ? osbjs.layer : 'Background';
        var anchor = osbjs.anchor ? osbjs.anchor : 'Centre';
        this.osbCode = [
            "Sprite," + layer + "," + anchor + ",\"" + fileName + "\"," + this._x.value + "," + this._y.value
        ];
        if (osbjs.scale != null)
            this.osbCode.push(" S,0," + startTime + ",," + osbjs.scale);
        if (osbjs.fade != null)
            this.osbCode.push(" F,0," + startTime + ",," + osbjs.fade);
        if (osbjs.rotation != null)
            this.osbCode.push(" R,0," + startTime + ",," + osbjs.rotation);
        if (osbjs.colour != null)
            this.osbCode.push(" C,0," + startTime + ",," + osbjs.colour.join(','));
        if (osbjs.vector != null)
            this.osbCode.push(" V,0," + startTime + ",," + osbjs.vector.join(','));
    }
    Osbject.prototype.getX = function () {
        return this._x;
    };
    Osbject.prototype.moveX = function (x) {
        this.sbFunction(x, 'MX');
    };
    Osbject.prototype.getY = function () {
        return this._y;
    };
    Osbject.prototype.moveY = function (y) {
        this.sbFunction(y, 'MY');
    };
    Osbject.prototype.getScale = function () {
        return this._scale;
    };
    Osbject.prototype.scale = function (scale) {
        this.sbFunction(scale, 'S');
    };
    Osbject.prototype.getFade = function () {
        return this._fade;
    };
    Osbject.prototype.fade = function (f) {
        this.sbFunction(f, 'F');
    };
    Osbject.prototype.getRotation = function () {
        return this._rotation;
    };
    Osbject.prototype.rotate = function (r) {
        this.sbFunction(r, 'R');
    };
    Osbject.prototype.getColour = function () {
        return this._colour;
    };
    Osbject.prototype.colour = function (c) {
        this.sbFunction(c, 'C');
    };
    Osbject.prototype.getVectorScale = function () {
        return this._vector;
    };
    Osbject.prototype.vector = function (v) {
        this.sbFunction(v, 'V');
    };
    Osbject.prototype.setParameter = function (param, time) {
        if (!time)
            time = this._fade.time;
        this.osbCode.push(" P,0," + time + ",," + param);
    };
    Osbject.prototype.toString = function () {
        return this.osbCode.join('\n');
    };
    Osbject.prototype.sbFunction = function (dF, func) {
        var _a, _b, _c, _d, _e;
        if ((dF.endTime != null) && (dF.changeTime != null))
            throw new Error('Can only do either endTime or changeTime (not both).');
        var sbParameter;
        switch (func) {
            case 'MX':
                sbParameter = this._x;
                break;
            case 'MY':
                sbParameter = this._y;
                break;
            case 'F':
                sbParameter = this._fade;
                break;
            case 'S':
                sbParameter = this._scale;
                break;
            case 'R':
                sbParameter = this._rotation;
                break;
            case 'C':
                sbParameter = this._colour;
                break;
            case 'V':
                sbParameter = this._vector;
                break;
            default:
                throw new Error('Invalid function.');
        }
        var time = sbParameter.time, value = sbParameter.value;
        if (!time || !value)
            throw new Error();
        var easing = (_a = dF.easing, (_a !== null && _a !== void 0 ? _a : 0));
        var startTime = (_b = dF.startTime, (_b !== null && _b !== void 0 ? _b : time));
        var endTime = (_c = dF.endTime, (_c !== null && _c !== void 0 ? _c : startTime + dF.changeTime));
        if (!Number.isInteger(startTime) || !Number.isInteger(endTime))
            throw new Error("Non-integer _time. " + startTime + ", " + endTime);
        var start;
        var end;
        var startAsString = '';
        var endAsString = '';
        if (['MX', 'MY', 'F', 'S', 'R'].includes(func)) {
            start = (_d = dF.start, (_d !== null && _d !== void 0 ? _d : value));
            startAsString = String(start);
            value = value;
            dF.change = dF.change;
            end = (_e = dF.end, (_e !== null && _e !== void 0 ? _e : dF.change)) ? value + dF.change : undefined;
            if (end != null)
                endAsString = String(end);
        }
        if (['C', 'V'].includes(func)) {
            start = dF.start ? dF.start : value;
            startAsString = start.join(',');
            value = value;
            dF.change = dF.change;
            if (dF.end != null)
                end = dF.end;
            if (dF.change != null)
                end = utils_1.sumTwoArrays(dF.change, value);
            end = end;
            if (func === 'C') {
                end.forEach(function (c) {
                    if (c > 255 || !Number.isInteger(c))
                        throw new Error("Invalid RGB value: " + end);
                });
            }
            if (end != null)
                endAsString = end.join(',');
        }
        var code = " " + func + "," + easing + "," + startTime + "," + endTime + "," + startAsString;
        if (end != null)
            code += "," + endAsString;
        this.osbCode.push(code);
        if (end != null)
            sbParameter.value = end;
        sbParameter.time = endTime ? endTime : startTime;
    };
    return Osbject;
}());
exports.Osbject = Osbject;
//# sourceMappingURL=osbject.js.map