import { Storyboard, IOsbject } from '../storyboard.framework';
import { randomRange } from '../utils';
import { mainTiming } from './timing';

export class Lyrics {
  private osb: Storyboard;
  private lyrics: string[];
  private charMap: string[];
  private beats: number;

  constructor(osb: Storyboard, lyrics: string[], charMap: string[], beats?: number) {
    this.osb = osb;
    this.lyrics = lyrics;
    this.charMap = charMap;
    this.beats = beats || 1000;
  }

  private charSpacing(offset: number, i: number, currentLine: IOsbject[], kanji: number[]): number {
    return i === 0 ? offset : (
      kanji.includes(i-1)
        ? <number>currentLine[i-1]?.getX().value + 76
        : <number>currentLine[i-1]?.getX().value + 56 || 0
    ) + (
      kanji.includes(i) ? 22 : 0
    );
  }

  public intro() {
    let kanji: number[];
    let fadeDuration: number = 600;
    let fadeOffset: number = 100;
    
    const order0 = [0, 4, 8, 2, 6, 1, 5, 9, 3, 7];
    const line0: IOsbject[] = [];
    kanji = [0];

    for (let i = 0 ; i < this.lyrics[0].length ; i++) {
      const char = this.lyrics[0].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 1031,
        x: this.charSpacing(40, i, line0, kanji),
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
    
    const order1 = [0, 3, 1, 2, 4];
    const line1: IOsbject[] = [];
    kanji = [0, 2];
    for (let i = 0 ; i < this.lyrics[1].length ; i++) {
      const char = this.lyrics[1].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 1031,
        x: this.charSpacing(240, i, line1, kanji),
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
    
    const order2 = [0, 6, 2, 8, 3, 1, 7, 4, 5];
    const line2: IOsbject[] = [];
    kanji = [0, 1, 2, 4, 5];
    for (let i = 0 ; i < this.lyrics[2].length ; i++) {
      const char = this.lyrics[2].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 1031,
        x: this.charSpacing(10, i, line2, kanji),
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
    
    const order3 = [0, 3, 1, 6, 5, 4, 2, 7];
    const line3: IOsbject[] = [];
    kanji = [];
    for (let i = 0 ; i < this.lyrics[3].length ; i++) {
      const char = this.lyrics[3].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 1031,
        x: this.charSpacing(200, i, line3, kanji),
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

  public outro() {
    let kanji: number[];
    let fadeDuration: number = 600;
    let fadeOffset: number = 100;

    const order0 = [0, 4, 8, 2, 6, 1, 5, 9, 3, 7];
    const line0: IOsbject[] = [];
    kanji = [0, 4, 5];
    for (let i = 0 ; i < this.lyrics[48].length ; i++) {
      const char = this.lyrics[48].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 293204,
        x: this.charSpacing(40, i, line0, kanji),
        y: kanji.includes(i) ? 100 : 114,
      });
      c.fade({
        startTime: 293204 + order0[i] * fadeOffset,
        changeTime: fadeDuration,
        start: 0,
        end: .80,
        easing: 2,
      });
      c.fade({
        startTime: 298857 + order0[i] * fadeOffset,
        changeTime: fadeDuration,
        start: .80,
        end: 0,
        easing: 2,
      });
      line0.push(c);
    }

    const order1 = [0, 3, 1, 2, 4];
    const line1: IOsbject[] = [];
    kanji = [0, 2];
    for (let i = 0 ; i < this.lyrics[49].length ; i++) {
      const char = this.lyrics[49].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 296683,
        x: this.charSpacing(240, i, line1, kanji),
        y: kanji.includes(i) ? 200 : 214,
      });
      c.fade({
        startTime: 296683 + order1[i] * fadeOffset,
        changeTime: fadeDuration,
        start: 0,
        end: .80,
        easing: 2,
      });
      c.fade({
        startTime: 298857 + order1[i] * fadeOffset,
        changeTime: fadeDuration,
        start: .80,
        end: 0,
        easing: 2,
      });
      line1.push(c);
    }

    const order2 = [0, 6, 2, 8, 3, 9, 1, 7, 4, 5];
    const line2: IOsbject[] = [];
    kanji = [0, 2, 7, 8];
    for (let i = 0 ; i < this.lyrics[50].length ; i++) {
      const char = this.lyrics[50].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 300161,
        x: this.charSpacing(10, i, line2, kanji) + (i === 0 ? 0 : -35),
        y: kanji.includes(i) ? 150 : 164,
      });
      c.fade({
        startTime: 300161 + order2[i] * fadeOffset,
        changeTime: fadeDuration,
        start: 0,
        end: .80,
        easing: 2,
      });
      c.fade({
        startTime: 305518 + order2[i] * fadeOffset,
        changeTime: fadeDuration,
        start: .80,
        end: 0,
        easing: 2,
      });
      c.moveX({
        startTime: 305518 + order2[i] * fadeOffset,
        changeTime: fadeDuration,
        change: 35,
        easing: 2,
      });
      c.moveY({
        startTime: 305518 + order2[i] * fadeOffset,
        changeTime: fadeDuration,
        change: -50,
        easing: 2,
      });
      c.rotate({
        startTime: 305518 + order2[i] * fadeOffset,
        changeTime: fadeDuration,
        change: 0.3,
        easing: 2,
      });
      line2.push(c);
    }

    const order3 = [0, 3, 1, 6, 5, 4, 2];
    const line3: IOsbject[] = [];
    kanji = [0];
    for (let i = 0 ; i < this.lyrics[51].length ; i++) {
      const char = this.lyrics[51].charAt(i);
      const c = this.osb.osbject({
        fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
        scale: kanji.includes(i) ? 0.4 : 0.28,
        startTime: 303639,
        x: this.charSpacing(200, i, line3, kanji) + (i === 0 ? 0 : -35),
        y: kanji.includes(i) ? 250 : 264,
      });
      c.fade({
        startTime: 303639 + order3[i] * fadeOffset,
        changeTime: fadeDuration,
        start: 0,
        end: .80,
        easing: 2,
      });
      c.fade({
        startTime: 305518 + order3[i] * fadeOffset,
        changeTime: fadeDuration,
        start: .80,
        end: 0,
        easing: 2,
      });
      c.moveX({
        startTime: 305518 + order3[i] * fadeOffset,
        changeTime: fadeDuration,
        change: 35,
        easing: 2,
      });
      c.moveY({
        startTime: 305518 + order3[i] * fadeOffset,
        changeTime: fadeDuration,
        change: -50,
        easing: 2,
      });
      c.rotate({
        startTime: 305518 + order3[i] * fadeOffset,
        changeTime: fadeDuration,
        change: 0.3,
        easing: 2,
      });
      line3.push(c);
    }
  }

  public main() {
    const fadeIn = 500;
    const fadeOut = 500;

    [...this.lyrics].splice(4, 44).forEach((line, i) => {
      for (let j = 0 ; j < line.length ; j++) {
        const char = line.charAt(j);

        const c = this.osb.osbject({
          fileName: `sb/lyrics/${this.charMap.indexOf(char)}.png`,
          layer: 'Foreground',
          startTime: mainTiming[i][0],
          x: 30 + (j * 45),
          y: 110,
        });

        const startTime = mainTiming[i][0] - fadeIn;
        const endTime = mainTiming[i][0] + this.beats * (mainTiming[i][1] || 8) - fadeOut;
        const aliveTime = endTime - startTime;
        const xDisplace = aliveTime * 0.005;
        const offset = j * 50;
        const transitionVector = [0.15, 0.225];
        const transitionBase = [0.2, 0.2];

        if (!mainTiming[i][2]) {
          c.fade({
            startTime: startTime + offset,
            changeTime: fadeIn,
            start: 0,
            end: 1,
          });
        } else {
          c.fade({
            startTime: mainTiming[i][0],
            endTime: mainTiming[i][0],
            start: 0,
            end: 1,
          });
        }

        c.fade({
          startTime: endTime - fadeOut + offset,
          changeTime: fadeOut,
          start: 1,
          end: 0,
        });

        c.moveX({
          startTime,
          endTime,
          change: xDisplace,
        });

        c.moveY({
          startTime,
          endTime,
          change: randomRange(aliveTime * 0.0005, aliveTime * 0.0015, 2) * (j % 2 === 0 ? -1 : 1),
        });

        // c.vector({
        //   startTime: startTime + offset,
        //   changeTime: fadeIn,
        //   start: transitionVector,
        //   end: transitionBase,
        //   easing: 1,
        // });

        c.vector({
          startTime: endTime - fadeOut + offset,
          changeTime: fadeOut,
          start: transitionBase,
          end: transitionVector,
          easing: 2,
        });
      }
    });
  }
}
