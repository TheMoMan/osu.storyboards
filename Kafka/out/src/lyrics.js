"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function renderLyrics(osb, lyrics, charMap) {
    var kanji;
    var fadeDuration = 600;
    var fadeOffset = 100;
    function charSpacing(offset, i, currentLine, kanji) {
        var _a, _b;
        return i === 0 ? offset : (kanji.includes(i - 1)
            ? ((_a = currentLine[i - 1]) === null || _a === void 0 ? void 0 : _a.getX().value) + 76
            : ((_b = currentLine[i - 1]) === null || _b === void 0 ? void 0 : _b.getX().value) + 56 || 0) + (kanji.includes(i) ? 22 : 0);
    }
    var order0 = [0, 4, 8, 2, 6, 1, 5, 9, 3, 7];
    var line0 = [];
    kanji = [0];
    for (var i = 0; i < lyrics[0].length; i++) {
        var char = lyrics[0].charAt(i);
        var c = osb.osbject({
            fileName: "sb/lyrics/" + charMap.indexOf(char) + ".png",
            scale: kanji.includes(i) ? 0.4 : 0.28,
            startTime: 1031,
            x: charSpacing(40, i, line0, kanji),
            y: kanji.includes(i) ? 100 : 114,
        });
        c.fade({
            startTime: 1031 + order0[i] * fadeOffset,
            changeTime: fadeDuration,
            start: 0,
            end: .80,
            easing: 2,
        });
        c.fade({
            startTime: 6683 + order0[i] * fadeOffset,
            changeTime: fadeDuration,
            start: .80,
            end: 0,
            easing: 2,
        });
        line0.push(c);
    }
    var order1 = [0, 3, 1, 2, 4];
    var line1 = [];
    kanji = [0, 2];
    for (var i = 0; i < lyrics[1].length; i++) {
        var char = lyrics[1].charAt(i);
        var c = osb.osbject({
            fileName: "sb/lyrics/" + charMap.indexOf(char) + ".png",
            scale: kanji.includes(i) ? 0.4 : 0.28,
            startTime: 1031,
            x: charSpacing(240, i, line1, kanji),
            y: kanji.includes(i) ? 200 : 214,
        });
        c.fade({
            startTime: 4509 + order1[i] * fadeOffset,
            changeTime: fadeDuration,
            start: 0,
            end: .80,
            easing: 2,
        });
        c.fade({
            startTime: 7117 + order1[i] * fadeOffset,
            changeTime: fadeDuration,
            start: .80,
            end: 0,
            easing: 2,
        });
        line1.push(c);
    }
    var order2 = [0, 6, 2, 8, 3, 1, 7, 4, 5];
    var line2 = [];
    kanji = [0, 1, 2, 4, 5];
    for (var i = 0; i < lyrics[2].length; i++) {
        var char = lyrics[2].charAt(i);
        var c = osb.osbject({
            fileName: "sb/lyrics/" + charMap.indexOf(char) + ".png",
            scale: kanji.includes(i) ? 0.4 : 0.28,
            startTime: 1031,
            x: charSpacing(10, i, line2, kanji),
            y: kanji.includes(i) ? 150 : 164,
        });
        c.fade({
            startTime: 7987 + order2[i] * fadeOffset,
            changeTime: fadeDuration,
            start: 0,
            end: .80,
            easing: 2,
        });
        c.fade({
            startTime: 13639 + order2[i] * fadeOffset,
            changeTime: fadeDuration,
            start: .80,
            end: 0,
            easing: 2,
        });
        line2.push(c);
    }
    var order3 = [0, 3, 1, 6, 5, 4, 2, 7];
    var line3 = [];
    kanji = [];
    for (var i = 0; i < lyrics[3].length; i++) {
        var char = lyrics[3].charAt(i);
        var c = osb.osbject({
            fileName: "sb/lyrics/" + charMap.indexOf(char) + ".png",
            scale: kanji.includes(i) ? 0.4 : 0.28,
            startTime: 1031,
            x: charSpacing(200, i, line3, kanji),
            y: kanji.includes(i) ? 250 : 264,
        });
        c.fade({
            startTime: 11465 + order3[i] * fadeOffset,
            changeTime: fadeDuration,
            start: 0,
            end: .80,
            easing: 2,
        });
        c.fade({
            startTime: 14074 + order3[i] * fadeOffset,
            changeTime: fadeDuration,
            start: .80,
            end: 0,
            easing: 2,
        });
        line3.push(c);
    }
}
exports.renderLyrics = renderLyrics;
//# sourceMappingURL=lyrics.js.map