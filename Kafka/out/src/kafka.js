"use strict";
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
var storyboard_1 = require("./storyboard.framework/storyboard");
var fs = __importStar(require("fs"));
var lyrics_1 = require("./lyrics");
// Set up
var location = fs.readFileSync('./inputs/loc.txt').toString();
var osb = new storyboard_1.Storyboard(location + "/senya - Kafka Naru Gunjou e (-Mo-).osb");
var osbject = osb.osbject.bind(osb);
var BPM = 138;
var signature = 4;
function beats(beats) {
    if (beats === void 0) { beats = 1; }
    return Math.round((60000 / BPM) * beats);
}
function measures(measures) {
    if (measures === void 0) { measures = 1; }
    var beat = (60000 / BPM);
    return Math.round(beat * signature * measures);
}
// Lyrics set up
var lyrics = fs.readFileSync('./inputs/lyrics.txt').toString().split('\r\n' || '\n');
var charMap = [];
lyrics.forEach(function (line) {
    for (var i = 0; i < line.length; i++) {
        var c = line.charAt(i);
        if (!charMap.includes(c))
            charMap.push(c);
    }
});
// Remove background
var bg = osb.osbject({ fileName: 'bg.jpg', fade: 0 });
// SB background
var night = osb.osbject({
    fileName: 'sb/backgrounds/night_1.jpg',
    x: 340,
    y: 440,
    startTime: 1031,
    scale: .4,
});
night.fade({ start: 0, end: .67, changeTime: beats(1) });
night.fade({ end: 0, startTime: 14944, changeTime: beats(1) });
night.moveX({ change: -40, changeTime: measures(8.25) });
night.moveY({ change: -200, changeTime: measures(8.25) });
// Lyrics
lyrics_1.renderLyrics(osb, lyrics, charMap);
osb.export();
//# sourceMappingURL=kafka.js.map