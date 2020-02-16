"use strict";
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
var fs = __importStar(require("fs"));
var TStoryboard = /** @class */ (function () {
    function TStoryboard(location) {
        this.location = location;
        this.background = [];
        this.foreground = [];
    }
    ;
    TStoryboard.prototype.osbject = function (fileName, x, y, layer, anchor, startTime) {
        if (x === void 0) { x = 320; }
        if (y === void 0) { y = 240; }
        if (layer === void 0) { layer = 'Background'; }
        if (anchor === void 0) { anchor = 'Centre'; }
        if (startTime === void 0) { startTime = 0; }
        var osbject = new Osbject(fileName, x, y, layer, anchor, startTime);
        switch (layer) {
            case 'Background':
            case 'bg':
                this.background.push(osbject);
                break;
            case 'Foreground':
            case 'fg':
                this.foreground.push(osbject);
                break;
            default:
                throw new Error("Cannot assign layer " + layer);
        }
        return osbject;
    };
    ;
    TStoryboard.prototype.export = function () {
        var _this = this;
        var osbAsString = '[Events]\n' +
            '//Background and Video events\n' +
            '//Storyboard Layer 0 (Background)\n' +
            this.osbjectsToString(this.background) +
            '//Storyboard Layer 1 (Fail)\n' +
            '//Storyboard Layer 2 (Pass)\n' +
            '//Storyboard Layer 3 (Foreground)\n' +
            this.osbjectsToString(this.foreground) +
            '//Storyboard Sound Samples\n';
        fs.writeFile(this.location, osbAsString, function (err) {
            if (err)
                throw err;
            console.log("Writing to " + _this.location + "...");
            console.log('Done!');
        });
    };
    TStoryboard.prototype.osbjectsToString = function (osbjects) {
        var out = '';
        osbjects.forEach(function (osbject) {
            out += osbject.toString() + '\n';
        });
        return out;
    };
    return TStoryboard;
}());
exports.TStoryboard = TStoryboard;
var Osbject = /** @class */ (function () {
    // private parameter: string;
    // private parameterTime: number;
    function Osbject(fileName, startX, startY, layer, anchor, startTime) {
        if (startX === void 0) { startX = 320; }
        if (startY === void 0) { startY = 240; }
        if (layer === void 0) { layer = 'Background'; }
        if (anchor === void 0) { anchor = 'Centre'; }
        if (startTime === void 0) { startTime = 0; }
        this.fileName = fileName;
        this.startX = startX;
        this.startY = startY;
        this.layer = layer;
        this.anchor = anchor;
        this.startTime = startTime;
        this.osbCode = [
            "Sprite," + layer + "," + anchor + ",\"" + fileName + "\"," + startX + "," + startY
        ];
        this.x = startX;
        this.y = startY;
        this.scale = 1;
        this.fade = 1;
        this.rotation = 0;
        this.colour = [255, 255, 255];
        this.vector = [1, 1];
        // this.parameter = '';
        this.xTime = startTime;
        this.yTime = startTime;
        this.scaleTime = startTime;
        this.fadeTime = startTime;
        this.rotationTime = startTime;
        this.colourTime = startTime;
        this.vectorTime = startTime;
        // this.parameterTime = startTime;
    }
    Osbject.prototype.getX = function () {
        return [this.x, this.xTime];
    };
    Osbject.prototype.setX = function (x, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.xTime)
            throw new Error('Cannot go backwards in time.');
        this.x = x;
        this.xTime = time;
        if (write) {
            this.osbCode.push(" F,0," + time + ",," + x);
        }
    };
    Osbject.prototype.moveXBy = function (x, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        var newX = this.x + x;
        var newTime = this.xTime + time;
        var newTimeS = newTime !== this.xTime ? newTime.toString() : '';
        this.osbCode.push(" MX," + easing + "," + this.xTime + "," + newTimeS + "," + this.x + "," + newX);
        this.x = newX;
        this.xTime = newTime;
    };
    Osbject.prototype.getY = function () {
        return [this.y, this.yTime];
    };
    Osbject.prototype.setY = function (y, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.yTime)
            throw new Error('Cannot go backwards in time.');
        this.y = y;
        this.yTime = time;
        if (write) {
            this.osbCode.push(" F,0," + time + ",," + y);
        }
    };
    Osbject.prototype.moveYBy = function (y, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        var newY = this.y + y;
        var newTime = this.yTime + time;
        var newTimeS = newTime !== this.yTime ? newTime.toString() : '';
        this.osbCode.push(" MY," + easing + "," + this.yTime + "," + newTimeS + "," + this.y + "," + newY);
        this.y = newY;
        this.yTime = newTime;
    };
    Osbject.prototype.getFade = function () {
        return [this.fade, this.fadeTime];
    };
    Osbject.prototype.setFade = function (fade, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.fadeTime)
            throw new Error('Cannot go backwards in time.');
        this.fade = fade;
        this.fadeTime = time;
        if (write) {
            this.osbCode.push(" F,0," + time + ",," + fade);
        }
    };
    Osbject.prototype.fadeBy = function (fade, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        var newFade = this.fade + fade;
        var newTime = this.fadeTime + time;
        var newTimeS = newTime !== this.fadeTime ? newTime.toString() : '';
        this.osbCode.push(" F," + easing + "," + this.fadeTime + "," + newTimeS + "," + this.fade + "," + newFade);
        this.fade = newFade;
        this.fadeTime = newTime;
    };
    Osbject.prototype.getScale = function () {
        return [this.scale, this.scaleTime];
    };
    Osbject.prototype.setScale = function (scale, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.scaleTime)
            throw new Error('Cannot go backwards in time.');
        this.scale = scale;
        this.scaleTime = time;
        if (write) {
            this.osbCode.push(" S,0," + time + ",," + scale);
        }
    };
    Osbject.prototype.scaleBy = function (scale, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        var newScale = this.scale + scale;
        var newTime = this.scaleTime + time;
        var newTimeS = newTime !== this.scaleTime ? newTime.toString() : '';
        this.osbCode.push(" S," + easing + "," + this.scaleTime + "," + newTimeS + "," + this.scale + "," + newScale);
        this.scale = newScale;
        this.scaleTime = newTime;
    };
    Osbject.prototype.getRotation = function () {
        return [this.rotation, this.rotationTime];
    };
    Osbject.prototype.setRotation = function (rotation, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.rotationTime)
            throw new Error('Cannot go backwards in time.');
        this.rotation = rotation;
        this.rotationTime = time;
        if (write) {
            this.osbCode.push(" F,0," + time + ",," + rotation);
        }
    };
    Osbject.prototype.rotateBy = function (rotation, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        var newRotation = this.rotation + rotation;
        var newTime = this.rotationTime + time;
        var newTimeS = newTime !== this.rotationTime ? newTime.toString() : '';
        this.osbCode.push(" R," + easing + "," + this.rotationTime + "," + newTimeS + "," + this.rotation + "," + newRotation);
        this.rotation = newRotation;
        this.rotationTime = newTime;
    };
    Osbject.prototype.getColour = function () {
        return [this.colour, this.colourTime];
    };
    Osbject.prototype.setColour = function (colour, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.colourTime)
            throw new Error('Cannot go backwards in time.');
        this.colour = colour;
        this.colourTime = time;
        if (write) {
            this.osbCode.push(" F,0," + time + ",," + this.tupleToString(colour));
        }
    };
    Osbject.prototype.colourBy = function (colour, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        // Trade memory for access speed.
        var newColour = [0, 0, 0];
        for (var i = 0; i < 3; i++) {
            var newC = this.colour[i] + colour[i];
            if (newC > 255 || newC < 0)
                throw new Error('Colour goes out of range.');
            newColour[i] = newC;
        }
        var newTime = this.colourTime + time;
        var newTimeS = newTime !== this.colourTime ? newTime.toString() : '';
        var colourS = this.tupleToString(this.colour);
        var newColourS = this.tupleToString(colour);
        this.osbCode.push(" C," + easing + "," + this.colourTime + "," + newTimeS + "," + colourS + "," + newColourS);
        this.colour = newColour;
        this.colourTime = newTime;
    };
    Osbject.prototype.getVectorScale = function () {
        return [this.vector, this.vectorTime];
    };
    Osbject.prototype.setVectorScale = function (vector, time, write) {
        if (write === void 0) { write = false; }
        if (time < this.vectorTime)
            throw new Error('Cannot go backwards in time.');
        this.vector = vector;
        this.vectorTime = time;
        if (write) {
            this.osbCode.push(" F,0," + time + ",," + this.tupleToString(vector));
        }
    };
    Osbject.prototype.vectorScaleBy = function (vector, time, easing) {
        if (easing === void 0) { easing = 0; }
        this.checkValidTime(time);
        var newVector = this.vector;
        for (var i = 0; i < 2; i++) {
            newVector[i] += vector[i];
        }
        var vectorS = this.tupleToString(this.vector);
        var newVectorS = this.tupleToString(newVector);
        var newTime = this.vectorTime + time;
        var newTimeS = newTime !== this.vectorTime ? newTime.toString() : '';
        this.osbCode.push(" V," + easing + "," + this.vectorTime + "," + newTimeS + "," + vectorS + "," + newVectorS);
        this.vector = newVector;
        this.vectorTime = newTime;
    };
    Osbject.prototype.setParameter = function (parameter, time) {
        this.osbCode.push(" P,0," + time + ",," + parameter);
    };
    // func(
    //     func: string,
    //     easing: number,
    //     startTime: number,
    //     endTime: number,
    //     val1: number | string,
    //     val2?: number,
    //     val3?: number,
    //     val4?: number,
    //     val5?: number,
    //     val6?: number,
    // ): void {
    //     let f = ` ${func}`;
    //     for (let i = 1 ; i < arguments.length ; i++) {
    //         f += `,${this.isDefined(arguments[i]) ? arguments[i] : ''}`;
    //     }
    //     this.osbCode.push(f);
    // }
    Osbject.prototype.toString = function () {
        return this.osbCode.join('\n');
    };
    Osbject.prototype.isDefined = function (x) {
        return (x !== undefined && x !== null);
    };
    Osbject.prototype.checkValidTime = function (time) {
        if (time < 0)
            throw new Error('Cannot use negative time.');
        if (!Number.isInteger(time))
            throw new Error('Cannot use non-integer time.');
    };
    Osbject.prototype.tupleToString = function (tuple) {
        var output = '';
        tuple.forEach(function (element) {
            output += element + ",";
        });
        return output.slice(0, -1);
    };
    return Osbject;
}());
//# sourceMappingURL=TStoryboard.js.map