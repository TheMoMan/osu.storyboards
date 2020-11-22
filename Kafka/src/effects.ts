import { Storyboard } from './storyboard.framework';
import { randomInt, randomRange, randomSign } from './utils';

export class Effects {
  private osb: Storyboard;

  constructor(osb: Storyboard) {
    this.osb = osb;
  }

  public ripple(start: number) {
    const offset = 50;
    const time = 1200;
    
    const ripple1 = this.osb.osbject({
      fileName: 'sb/ring.png',
      x: 320,
      y: 240,
      scale: 0,
      startTime: start,
    });

    ripple1.setParameter('A');

    const ripple2 = this.osb.osbject({
      fileName: 'sb/ring.png',
      x: 320,
      y: 240,
      scale: 0,
    });

    ripple2.setParameter('A');

    const ripple3 = this.osb.osbject({
      fileName: 'sb/ring.png',
      x: 320,
      y: 240,
      scale: 0,
    });

    ripple3.setParameter('A');

    ripple1.scale({
      startTime: start,
      endTime: start + time,
      start: 0,
      end: 1,
      easing: 4,
    });

    ripple1.fade({
      startTime: start,
      endTime: start + time,
      start: 1,
      end: 0,
    });

    ripple2.scale({
      startTime: start + offset,
      endTime: start + time + offset,
      start: 0,
      end: 0.8,
      easing: 4,
    });

    ripple2.fade({
      startTime: start + offset,
      endTime: start + time,
      start: 1,
      end: 0,
    });

    ripple3.scale({
      startTime: start + offset * 2,
      endTime: start + time + offset * 2,
      start: 0,
      end: 0.6,
      easing: 4,
    });

    ripple3.fade({
      startTime: start + offset * 2,
      endTime: start + time,
      start: 1,
      end: 0,
    });
  }

  public meteors(start: number, end: number) {
    const dTime = end - start;

    for (let i = 0 ; i < dTime ; i += randomInt(5000, 10000)) {
      const m = this.osb.osbject({
        fileName: 'sb/drop.png',
        startTime: start + i,
        vector: [0.05, 0.5],
        x: randomInt(100, 740),
        y: -10,
        rotation: 3.141593 * .25,
        fade: 0.2,
      });

      m.setParameter('A');

      m.moveX({
        change: -500,
        changeTime: 150,
      });

      m.moveY({
        change: 500,
        changeTime: 150,
      });
    }
  }

  public floatingParticles(start: number, end: number) {
    const dTime = end - start;

    for (let i = 0 ; i < dTime ; i += randomInt(800, 1500)) {
      const timeRemaining = end - (start + i);
      if (timeRemaining < 3000) break;

      const p = this.osb.osbject({
        fileName: 'sb/particle.png',
        layer: 'Foreground',
        startTime: start + i,
        x: randomInt(-70, 710),
        y: randomInt(300, 440),
        fade: 0,
        scale: randomRange(0.15, 0.33, 2),
        // colour: [150, 200, 255],
      });

      p.setParameter('A');

      const timeAlive = Math.min(randomInt(3000, 8000), timeRemaining + 500);
      const speed = 0.01;
      const xPercentage = randomRange(0, 1, 2);

      p.moveX({
        changeTime: timeAlive,
        change: timeAlive * speed * xPercentage * randomSign(),
      });

      p.moveY({
        changeTime: timeAlive,
        change: timeAlive * speed * (1 - xPercentage) * randomSign(),
      });

      p.fade({
        changeTime: 500,
        start: 0,
        end: 0.67,
      });

      p.fade({
        startTime: start + i + timeAlive - 500,
        endTime: start + i + timeAlive,
        start: 0.67,
        end: 0,
      });
    }
  }
}
