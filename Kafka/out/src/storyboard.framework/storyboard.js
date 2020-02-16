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
var osbject_1 = require("./osbject");
var Storyboard = /** @class */ (function () {
    function Storyboard(location) {
        this.location = location;
        this.background = [];
        this.fail = [];
        this.pass = [];
        this.foreground = [];
    }
    ;
    Storyboard.prototype.osbject = function (osbjs) {
        var osbject = new osbject_1.Osbject(osbjs);
        var layer = osbjs.layer ? osbjs.layer : 'Background';
        switch (layer.toLowerCase()) {
            case 'background':
            case 'bg':
                this.background.push(osbject);
                break;
            case 'foreground':
            case 'fg':
                this.foreground.push(osbject);
                break;
            case 'fail':
                this.fail.push(osbject);
                break;
            case 'pass':
                this.pass.push(osbject);
                break;
            default:
                throw new Error("Cannot assign layer " + layer);
        }
        return osbject;
    };
    ;
    Storyboard.prototype.export = function () {
        var _this = this;
        var osbAsString = '[Events]\n' +
            '//Background and Video events\n' +
            '//Storyboard Layer 0 (Background)\n' +
            this.osbjectsToString(this.background) +
            '//Storyboard Layer 1 (Fail)\n' +
            this.osbjectsToString(this.fail) +
            '//Storyboard Layer 2 (Pass)\n' +
            this.osbjectsToString(this.pass) +
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
    Storyboard.prototype.osbjectsToString = function (osbjects) {
        var out = '';
        osbjects.forEach(function (osbject) {
            out += osbject.toString() + '\n';
        });
        return out;
    };
    return Storyboard;
}());
exports.Storyboard = Storyboard;
//# sourceMappingURL=storyboard.js.map