import { Storyboard, ColourValue } from './storyboard.framework';
import * as fs from 'fs';
import { lyricsIntro } from './lyrics';
import { particlesHorizontal } from './particles';
import { ParticlesFadeParams } from './interfaces';

// === Set up
const location = fs.readFileSync('./inputs/loc.txt').toString();

const osb: Storyboard = new Storyboard(`${location}/senya - Kafka Naru Gunjou e (-Mo-).osb`);

const BPM: number = 138;
const signature: number = 4;

function beats(beats: number = 1): number {
    return Math.round((60000 / BPM) * beats);
}

function measures(measures: number = 1): number {
    const beat = (60000 / BPM);
    return Math.round(beat * signature * measures);
}

// === Lyrics set up
const lyrics: string[] = fs.readFileSync('./inputs/lyrics.txt').toString().split('\r\n' || '\n');

const charMap: string[] = [];

lyrics.forEach(line => {
    for (let i = 0 ; i < line.length ; i++) {
        const c = line.charAt(i);
        if (!charMap.includes(c)) 
            charMap.push(c);
    }
});

// Remove background
const bg = osb.osbject({ fileName: 'bg.jpg', fade: 0 });

// === SB background

// Intro
const night = osb.osbject({
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

lyricsIntro(osb, lyrics, charMap);

// Verse 1
// const tenshiBg1 = osb.osbject({
//     fileName: 'sb/tenshi/a.png',
//     x: 480,
//     y: 220,
//     startTime: 18422,
//     scale: .6,
//     colour: [0, 0, 0]
// });

// tenshiBg1.moveY({ end: 280, endTime: 32335 });
// tenshiBg1.fade({ end: 0, startTime: 19291 });
// tenshiBg1.fade({ end: 1, startTime: 31465 });

// const tenshi1 = osb.osbject({
//     fileName: 'sb/tenshi/a.png',
//     x: 480,
//     y: 220,
//     startTime: 18422,
//     scale: .6,
// });

// tenshi1.fade({ start: 0, end: 1, changeTime: beats(2) });
// tenshi1.fade({ end: 0, startTime: 31465, changeTime: beats(2) });
// tenshi1.moveY({ end: 280, endTime: 32335 });

const v1Bg = osb.osbject({
    fileName: 'sb/backgrounds/aurora_1.jpg',
    x: 320,
    y: 240,
    startTime: 18422,
    scale: .54
});

v1Bg.moveX({ change: -50, endTime: 51465 })
v1Bg.fade({ start: 0, end: 1, changeTime: beats(2) });
v1Bg.fade({ end: 0, startTime: 49726, changeTime: beats(2) });

const tenshi1 = osb.osbject({
    fileName: 'sb/tenshi/b.png',
    x: 20,
    y: 140,
    startTime: 18422,
    scale: .8,
});

tenshi1.moveX({ change: 60, endTime: 32335 });
tenshi1.fade({ start: 0, end: 1, changeTime: beats(2) });
tenshi1.fade({ end: 0, startTime: 31465, changeTime: beats(2) });

osb.export();
