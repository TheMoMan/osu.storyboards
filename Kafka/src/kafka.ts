import { Storyboard, ColourValue } from './storyboard.framework';
import * as fs from 'fs';
import { lyricsIntro } from './lyrics';

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

const v1Bg = osb.osbject({
    fileName: 'sb/backgrounds/aurora_1.jpg',
    x: 370,
    y: 240,
    startTime: 18422,
    scale: .55
});

v1Bg.moveX({ change: -100, endTime: 51465 })
v1Bg.fade({ start: 0, end: 1, changeTime: beats(2) });
v1Bg.fade({ end: 0, startTime: 49726, changeTime: beats(2) });

const tenshi = osb.osbject({
    fileName: 'sb/tenshi.png',
    layer: 'Foreground',
    x: 126.25,
    y: 396.6,
    startTime: 18422,
    scale: 0.444444444444,
    colour: [0, 0, 0],
})

tenshi.colour({
    end: [255, 255, 255],
    changeTime: beats(2),
});

tenshi.fade({
    end: 0,
    startTime: 108857,
    changeTime: beats(2),
});

// Chorus 1

const chorusBg = osb.osbject({
    fileName: 'bg.jpg',
    startTime: 49726,
    scale: 0.444444444444,
    fade: 0,
});

chorusBg.fade({
    end: 1,
    changeTime: measures(2),
});

chorusBg.fade({
    end: 0,
    startTime: 108857,
    changeTime: measures(1),
});

osb.export();
