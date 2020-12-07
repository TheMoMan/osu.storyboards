import { Storyboard } from './storyboard.framework';
import * as fs from 'fs';
import { Lyrics } from './lyrics/lyrics';
import { aurora } from './auroras';
import { bridge } from './bridge';
import { Effects } from './effects';

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

const effects = new Effects(osb);

// === Lyrics set up
const lyricsText: string[] = fs.readFileSync('./inputs/lyrics.txt').toString().split('\r\n' || '\n');

const charMap: string[] = [];

lyricsText.forEach(line => {
  for (let i = 0 ; i < line.length ; i++) {
    const c = line.charAt(i);
    if (!charMap.includes(c)) 
      charMap.push(c);
  }
});

const lyrics = new Lyrics(osb, lyricsText, charMap, beats());

// Intro/Outro setup

const night = osb.osbject({
  fileName: 'sb/backgrounds/night_1.jpg',
  x: 360,
  y: 440,
  startTime: 1031,
  scale: .4,
});

const night2 = osb.osbject({
  fileName: 'sb/backgrounds/night_1.jpg',
  x: 320,
  y: 240,
  startTime: 293204,
  scale: .4,
});

// Post Intro setup

const mainBg = osb.osbject({
  fileName: 'bg.jpg',
  x: 320,
  y: 240,
  startTime: 18422,
  scale: .444444444,
});

const blueBg = osb.osbject({
  fileName: 'sb/backgrounds/blue.jpg',
  x: 320,
  y: 240,
  startTime: 53204,
  scale: .444444444,
});

// Gotta do meteors here for layer order
effects.meteors(18422, 108857);
effects.meteors(122770, 199291);
effects.meteors(230596, 291465);

const mainBgFg = osb.osbject({
  fileName: 'sb/backgrounds/foreground.png',
  startTime: 18422,
  scale: .444444444,
});

const blueBgFg = osb.osbject({
  fileName: 'sb/backgrounds/foreground_blue.png',
  startTime: 53204,
  scale: .444444444,
  x: 320,
  y: 507,
  anchor: 'BottomCentre'
});

const aurora1 = osb.osbject({
  fileName: 'sb/backgrounds/aurora_1.png',
  x: 370,
  y: 100,
  startTime: 53204,
});

const aurora2 = osb.osbject({
  fileName: 'sb/backgrounds/aurora_2.png',
  x: 268,
  y: 100,
  startTime: 53204,
});

const mainBgBlur = osb.osbject({
  fileName: 'sb/backgrounds/blur.jpg',
  startTime: 108857,
  scale: .444444444,
});

const tenshi = osb.osbject({
  fileName: 'sb/tenshi/default.png',
  layer: 'Foreground',
  x: 126.8,
  y: 396.8,
  startTime: 18422,
  scale: 0.444444444444,
})

const iku = osb.osbject({
  fileName: 'sb/iku/default.png',
  layer: 'Foreground',
  x: 527.7,
  y: 299.8,
  startTime: 18422,
  scale: 0.444444444444,
});

const tenshiBlue = osb.osbject({
  fileName: 'sb/tenshi/blue.png',
  layer: 'Foreground',
  x: 126.8,
  y: 396.8,
  startTime: 53204,
  scale: 0.444444444444,
})

const ikuBlue = osb.osbject({
  fileName: 'sb/iku/blue.png',
  layer: 'Foreground',
  x: 527.7,
  y: 299.8,
  startTime: 53204,
  scale: 0.444444444444,
});

// ================================= Intro =================================
night.fade({
  start: 0,
  end: 1,
  changeTime:beats(2),
});
night.moveX({
  change: -40,
  changeTime: measures(8),
});
night.moveY({
  change: -200,
  changeTime: measures(8),
});
night.moveX({
  change: -Math.pow(5, 1/2),
  changeTime: measures(1),
  easing: 7,
});
night.moveY({
  change: -Math.pow(25, 1/2),
  changeTime: measures(1),
  easing: 7,
});
night.scale({
  startTime: 16683,
  endTime: 18422,
  start: .3905,
  end: 10,
  easing: 18,
});
night.rotate({
  startTime: 16683,
  endTime: 18422,
  end: 3.141593,
  easing: 6,
});

lyrics.intro();

effects.ripple(14944);

// ================================= Verse 1 =================================

lyrics.main();

mainBg.fade({
  start: 0,
  end: 1,
  changeTime: 0,
});

mainBgFg.fade({
  start: 0,
  end: 1,
  changeTime: 0,
});

tenshi.fade({
  start: 1,
  end: 1,
  startTime: 18422,
  endTime: 53204,
});

iku.fade({
  start: 1,
  end: 1,
  startTime: 18422,
  endTime: 53204,
});

effects.floatingParticles(18422, 109074);

// ================================= Chorus 1 =================================

mainBg.fade({
  start: 0,
  end: 0,
  startTime: 53204,
})

mainBgFg.fade({
  start: 0,
  end: 0,
  startTime: 53204,
})

tenshi.fade({
  start: 0,
  end: 0,
  startTime: 53204,
  endTime: 53204,
});

iku.fade({
  start: 0,
  end: 0,
  startTime: 53204,
  endTime: 53204,
});

aurora([aurora1, aurora2], 53204, 108857, beats(1));

tenshiBlue.fade({
  start: 1,
  end: 1,
  startTime: 53204,
  endTime: 108857,
});

ikuBlue.fade({
  start: 1,
  end: 1,
  startTime: 53204,
  endTime: 108857,
});

blueBg.fade({
  start: 1,
  end: 1,
  startTime: 53204,
  endTime: 53204,
});

blueBgFg.fade({
  start: 1,
  end: 1,
  startTime: 53204,
  endTime: 53204,
});

// ================================= Verse 2 =================================

blueBg.fade({
  start: 0,
  end: 0,
  startTime: 110596,
  endTime: 110596,
});

blueBgFg.fade({
  start: 0,
  end: 0,
  startTime: 110596,
  endTime: 110596,
});

tenshiBlue.fade({
  start: 1,
  end: 0,
  changeTime: beats(4),
});

ikuBlue.fade({
  start: 1,
  end: 0,
  changeTime: beats(4),
});

tenshi.fade({
  start: 1,
  end: 1,
  startTime: 108857,
});

iku.fade({
  start: 1,
  end: 1,
  startTime: 108857,
});

mainBgBlur.fade({
  start: 0,
  end: 1,
  startTime: 108857,
  changeTime: beats(4),
});

mainBgBlur.fade({
  start: 1,
  end: 0,
  startTime: 115813,
  changeTime: measures(4),
});

mainBg.fade({
  start: 1,
  end: 1,
  startTime: 115813,
  endTime: 143639,
});

mainBgFg.fade({
  start: 1,
  end: 1,
  startTime: 115813,
  endTime: 143639,
});

effects.floatingParticles(122770, 199291);

// ================================= Chorus 2 =================================

mainBg.fade({
  start: 0,
  end: 0,
  endTime: 143639,
});

mainBgFg.fade({
  start: 0,
  end: 0,
  endTime: 143639,
});

tenshi.fade({
  end: 0,
  startTime: 143639,
});

iku.fade({
  end: 0,
  startTime: 143639,
});

aurora([aurora1, aurora2], 143639, 199291, beats(1));

tenshiBlue.fade({
  start: 1,
  end: 1,
  startTime: 143639,
  endTime: 199291,
});

ikuBlue.fade({
  start: 1,
  end: 1,
  startTime: 143639,
  endTime: 199291,
});

blueBg.fade({
  start: 1,
  end: 1,
  startTime: 143639,
  endTime: 143639,
});

blueBgFg.fade({
  start: 1,
  end: 1,
  startTime: 143639,
  endTime: 143639,
});

// ===

blueBg.fade({
  start: 0,
  end: 0,
  startTime: 201031,
  endTime: 201031,
});

blueBgFg.fade({
  start: 0,
  end: 0,
  startTime: 201031,
  endTime: 201031,
});

mainBgBlur.fade({
  start: 0,
  end: 1,
  startTime: 199291,
  endTime: 201031,
});

tenshi.fade({
  start: 1,
  end: 1,
  startTime: 199291,
  endTime: 199291,
});

iku.fade({
  start: 1,
  end: 1,
  startTime: 199291,
  endTime: 199291,
});

tenshiBlue.fade({
  start: 1,
  end: 0,
  startTime: 199291,
  endTime: 201031,
});

ikuBlue.fade({
  start: 1,
  end: 0,
  startTime: 199291,
  endTime: 201031,
});


// ================================= Bridge =================================

tenshi.fade({
  start: 0,
  end: 0,
  startTime: 206248,
  endTime: 206248,
});

iku.fade({
  start: 0,
  end: 0,
  startTime: 206248,
  endTime: 206248,
});

bridge(osb);

// ================================= Chorus 3 =================================

tenshi.fade({
  start: 1,
  end: 1,
  startTime: 230596,
  endTime: 244509,
});

iku.fade({
  start: 1,
  end: 1,
  startTime: 230596,
  endTime: 244509,
});

tenshi.fade({
  start: 0,
  end: 0,
  startTime: 244509,
  endTime: 244509,
});

iku.fade({
  start: 0,
  end: 0,
  startTime: 244509,
  endTime: 244509,
});

mainBgBlur.fade({
  start: 0,
  end: 0,
  startTime: 230596,
  endTime: 230596,
});

aurora([aurora1, aurora2], 244509, 286248, beats(1));

mainBg.fade({
  start: 1,
  end: 1,
  startTime: 230596,
  endTime: 230596,
});

mainBgFg.fade({
  start: 1,
  end: 1,
  startTime: 230596,
  endTime: 230596,
});

mainBg.fade({
  start: 0,
  end: 0,
  startTime: 244509,
  endTime: 244509,
});

mainBgFg.fade({
  start: 0,
  end: 0,
  startTime: 244509,
  endTime: 244509,
});

blueBg.fade({
  start: 1,
  end: 1,
  startTime: 244509,
  endTime: 244509,
});

blueBgFg.fade({
  start: 1,
  end: 1,
  startTime: 244509,
  endTime: 244509,
});

tenshiBlue.fade({
  start: 1,
  end: 1,
  startTime: 244509,
  endTime: 244509,
});

ikuBlue.fade({
  start: 1,
  end: 1,
  startTime: 244509,
  endTime: 244509,
});

effects.floatingParticles(230596, 291465);

// ===

blueBg.fade({
  start: 1,
  end: 0,
  startTime: 286248,
  endTime: 287987,
});

blueBgFg.fade({
  start: 1,
  end: 0,
  startTime: 286248,
  endTime: 287987,
});

mainBg.fade({
  start: 1,
  end: 1,
  startTime: 286248,
  endTime: 286248,
});

mainBgFg.fade({
  start: 1,
  end: 1,
  startTime: 286248,
  endTime: 286248,
});

mainBg.fade({
  start: 1,
  end: 0,
  startTime: 291465,
  changeTime: beats(3.5),
});

mainBgFg.fade({
  start: 1,
  end: 0,
  startTime: 291465,
  endTime: 291465,
});

tenshiBlue.fade({
  start: 1,
  end: 0,
  startTime: 286248,
  endTime: 287987,
});

ikuBlue.fade({
  start: 1,
  end: 0,
  startTime: 286248,
  endTime: 287987,
});

tenshi.fade({
  start: 1,
  end: 1,
  startTime: 286248,
  endTime: 286248,
});

iku.fade({
  start: 1,
  end: 1,
  startTime: 286248,
  endTime: 286248,
});

tenshi.fade({
  start: 1,
  end: 0,
  startTime: 291900,
  changeTime: beats(3),
});

iku.fade({
  start: 1,
  end: 0,
  startTime: 291900,
  changeTime: beats(3),
});

// ================================= Outro =================================

night2.fade({
  startTime: 293204,
  endTime: 294074,
  start: 0,
  end: 1,
});

night2.moveX({
  startTime: 293204,
  endTime: 308946,
  change: -40,
});

night2.moveY({
  startTime: 293204,
  endTime: 308946,
  change: 200,
});

night2.fade({
  startTime: 305518,
  endTime: 308946,
  start: 1,
  end: 0,
});

lyrics.outro();

// ================================= Whiteouts =================================
 
effects.whiteFlash(18422, beats(2), beats(0.5), 18, 1);
effects.whiteFlash(53204);
effects.whiteFlash(143639);
effects.whiteFlash(206248);
effects.whiteFlash(230596);
effects.whiteFlash(244509);

// ==================================================================

osb.export();
