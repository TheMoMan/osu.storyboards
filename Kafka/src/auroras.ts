import { Osbject } from './storyboard.framework';
import { randomRange } from './utils';

export function aurora(auroras: [Osbject, Osbject], start: number, end: number, beats: number) {
  const aurora1 = auroras[0];
  const aurora2 = auroras[1];
  const length = end - start;
  const fadeOut = beats * 4

  aurora1.setParameter('A');

  aurora1.fade({
    start: 0,
    end: 0.75,
    startTime: start,
    endTime: start,
  });

  aurora1.fade({
      end: 0,
      startTime: end,
      changeTime: fadeOut,
  });

  aurora1.moveX({
      start: 370,
      end: 260,
      endTime: end + fadeOut,
  });

  aurora1.vector({
      end: [0.5, 0.5],
      startTime: start,
  });

  aurora2.setParameter('A');

  aurora2.fade({
    start: 0,
    end: 0.75,
    startTime: start,
    endTime: start,
  });

  aurora2.fade({
      end: 0,
      startTime: end,
      changeTime: beats * 4,
  });

  aurora2.moveX({
      start: 268,
      end: 370,
      endTime: end + fadeOut,
  });

  aurora2.vector({
    end: [0.5, 0.5],
    startTime: start,
  });

  for (let i = 0 ; i < 30 ; i++) {
    aurora1.vector({
      end: [0.5, randomRange(0.55, 0.45, 2)],
      changeTime: Math.floor(length/30),
      easing: 5,
    });

    aurora2.vector({
      end: [0.5, randomRange(0.52, 0.48, 2)],
      changeTime: Math.floor(length/30) + Math.floor(length/60),
      easing: 5,
    });
  }
}
