import { Storyboard } from './storyboard.framework/storyboard';
import * as fs from 'fs';
import { normaliseIndex } from './utils';
import { IOsbject } from './storyboard.framework/interfaces';
import { renderLyrics } from './lyrics';

// Set up
const location = fs.readFileSync('./inputs/loc.txt').toString();

const osb: Storyboard = new Storyboard(`${location}/senya - Kafka Naru Gunjou e (-Mo-).osb`);
const osbject: Function = osb.osbject.bind(osb);

const BPM: number = 138;
const signature: number = 4;

function beats(beats: number = 1): number {
    return Math.round((60000 / BPM) * beats);
}

function measures(measures: number = 1): number {
    const beat = (60000 / BPM);
    return Math.round(beat * signature * measures);
}

// Lyrics set up
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
const bg = osb.osbject({fileName: 'bg.jpg', fade: 0});

// SB background

const night = osb.osbject({
    fileName: 'sb/backgrounds/night_1.jpg',
    x: 340,
    y: 440,
    startTime: 1031,
    scale: .4,
});

night.fade({start: 0, end: .67, changeTime: beats(1)});
night.fade({end: 0, startTime: 14944, changeTime: beats(1)});
night.moveX({change: -40, changeTime: measures(8.25)});
night.moveY({change: -200, changeTime: measures(8.25)});

// Lyrics
renderLyrics(osb, lyrics, charMap);

osb.export();
