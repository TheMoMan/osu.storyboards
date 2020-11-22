import { chdir } from 'process';
import { Osbject, Storyboard } from './storyboard.framework'
import { randomInt, randomRange, randomSign } from './utils';

const field: Osbject[] = [];
const lanePositions: number[] = [];
let _osb: Storyboard;

const bridgeStart = 206248;
const bridgeEnd = 230596;

function hit(time: number, lane: number, speed: number = 1000) {
  const rotation = randomSign();

  // === Glow splash
  const hit1 = _osb.osbject({
    fileName: 'sb/bridge/hit1.png',
    layer: 'Foreground',
    anchor: 'BottomCentre',
    x: lanePositions[lane - 1],
    y: 240,
    startTime: bridgeStart,
    fade: 0,
    scale: 0.7,
  });

  const hit2 = _osb.osbject({
    fileName: 'sb/bridge/hit1.png',
    layer: 'Foreground',
    anchor: 'BottomCentre',
    x: lanePositions[lane - 1],
    y: 240,
    startTime: bridgeStart,
    fade: 0,
    scale: 0.6,
    rotation: 3.141593
  });

  const hitFlash = 350;
  
  hit1.fade({
    startTime: time,
    endTime: Math.min(time + hitFlash, bridgeEnd),
    start: 1,
    end: 0,
    easing: 2,
  });

  hit2.fade({
    startTime: time,
    endTime: Math.min(time + hitFlash, bridgeEnd),
    start: 0.2,
    end: 0,
    easing: 2,
  });

  // === Particle splash
  const splashTime = 500;

  for (let i = 0 ; i < 5 ; i++) {
    const p = _osb.osbject({
      fileName: 'sb/particle.png',
      startTime: time,
      scale: 0.05,
      x: lanePositions[lane - 1],
      y: 240,
    });

    const p2 = _osb.osbject({
      fileName: 'sb/particle.png',
      startTime: time,
      scale: 0.05,
      x: lanePositions[lane - 1],
      y: 240,
    });
    
    p.setParameter('A');
    p2.setParameter('A');

    const dX = randomRange(-10, 10, 1);
    const dY = randomRange(-8, -50, 1);

    p.moveX({
      changeTime: splashTime,
      change: dX,
    });

    p.moveY({
      changeTime: splashTime,
      change: dY,
      easing: 30,
    });

    p.fade({
      startTime: time,
      endTime: Math.min(time + splashTime, bridgeEnd),
      start: 1,
      end: 0,
    });

    p2.moveX({
      changeTime: splashTime,
      change: dX,
    });

    p2.moveY({
      changeTime: splashTime,
      change: -dY,
      easing: 30,
    });

    p2.fade({
      startTime: time,
      endTime: Math.min(time + splashTime, bridgeEnd),
      start: 0.1,
      end: 0,
    });
  }

  // === Notes
  const note = _osb.osbject({
    fileName: 'sb/bridge/note.png',
    layer: 'Foreground',
    x: lanePositions[lane - 1],
    y: 240,
    startTime: time,
    scale: 0.4,
    fade: 0.8,
  });

  const note2 = _osb.osbject({
    fileName: 'sb/bridge/note.png',
    layer: 'Foreground',
    x: lanePositions[lane - 1],
    y: 240,
    startTime: time,
    scale: 0.4,
    fade: 0.2,
  });

  note.setParameter('A');

  note.moveY({
    startTime: time - speed,
    endTime: time,
    start: -40,
    end: 240,
  });

  note.rotate({
    startTime: time - speed,
    endTime: time,
    start: -3.141593 * rotation,
    end: 0,
  });

  note2.moveY({
    startTime: time - speed,
    endTime: time,
    start: 500,
    end: 240,
  });

  note2.rotate({
    startTime: time - speed,
    endTime: time,
    start: 3.141593 * rotation,
    end: 0,
  });
}

export function bridge(osb: Storyboard) {    
  _osb = osb; // Maybe I should've made a class after all. Oh well.

  const hitzone = osb.osbject({
    fileName: 'sb/bridge/hitzone.png',
    layer: 'Foreground',
    x: 320,
    y: 240,
    startTime: bridgeStart,
  });

  field.push(hitzone);

  hitzone.setParameter('A');

  for (let i = -4 ; i < 5 ; i++) {
    const spacing = 42.4;

    const lanePosition = 320 + (i * spacing);
    lanePositions.push(lanePosition);
    
    const lane = osb.osbject({
      fileName: 'sb/bridge/lane.png',
      layer: 'Foreground',
      x: lanePosition,
      y: 240,
      startTime: bridgeStart,
      fade: 0.5,
    });

    lane.setParameter('A');

    field.push(lane);
  };

  field.forEach((osbject) => {
    osbject.scale({
      startTime: bridgeStart,
      endTime: bridgeEnd,
      start: .444444444,
      end: .444444444,
    });
  });

  // ============== Arrangement ==============
  hit(bridgeStart, 4); hit(bridgeStart, 8);
  hit(206574, 5);
  hit(206900, 9);
  hit(207770, 1);
  hit(207878, 3);
  hit(207987, 5); hit(207987, 7);
  hit(208313, 6); hit(208313, 8);
  hit(208639, 7); hit(208639, 9);
  hit(208857, 5); hit(208857, 8);
  hit(209183, 3); hit(209183, 7);
  hit(209509, 2); hit(209509, 4);
  hit(209726, 1);
  hit(210052, 6);
  hit(210378, 2);
  hit(211248, 5);
  hit(211465, 5);
  hit(211791, 9);
  hit(212117, 6);
  hit(212552, 8);
  hit(212987, 7);
  hit(213204, 3); hit(213204, 5);
  hit(213422, 1);
  hit(213639, 2);
  hit(213857, 3);
  hit(214074, 6);
  hit(214291, 4);
  hit(214509, 3);
  hit(214726, 5);
  hit(214835, 6);
  hit(214944, 7);
  hit(215161, 2);
  hit(215378, 4);
  hit(215596, 2);
  hit(215813, 4); hit(215813, 6);
  hit(216139, 3); hit(216139, 6);
  hit(216465, 5);
  hit(216683, 6); hit(216683, 7); hit(216683, 9);
  hit(217009, 3); hit(217009, 5); hit(217009, 8);
  hit(217335, 1); hit(217335, 2); hit(217335, 4);
  hit(217987, 6);
  hit(218422, 5); hit(218422, 7); hit(218422, 9);
  hit(218748, 3); hit(218748, 5); hit(218748, 8);
  hit(219074, 4); hit(219074, 6); hit(219074, 7);
  hit(219291, 1); hit(219291, 3); hit(219291, 5);
  hit(220161, 2); hit(220161, 3); hit(220161, 5); hit(220161, 7);
  hit(221031, 3); hit(221031, 5); hit(221031, 6); hit(221031, 8);
  hit(221357, 7);
  hit(221683, 9);
  hit(221900, 3); hit(221900, 5); hit(221900, 7); hit(221900, 8);
  hit(222226, 9);
  hit(222552, 6);
  // hit(223204, 2);
  // hit(223422, 1);

  hit(223639, 7, 750);
  hit(223857, 9, 750);
  hit(224074, 6, 750);
  hit(224291, 8, 750);
  hit(224509, 5, 750);
  hit(224726, 7, 750);
  hit(224944, 4, 750);
  hit(225161, 6, 750);
  hit(225378, 3, 750);
  hit(225596, 6, 750);
  hit(225813, 4, 750);
  hit(226031, 7, 750);
  hit(226248, 3, 750);
  hit(226465, 6, 750);
  hit(226683, 2, 750);
  hit(226900, 5, 750);
  hit(227117, 1, 750);

  hit(228748, 1);
  hit(228857, 2);

  hit(229509, 5, 500);
  hit(229581, 7, 500);
  hit(229654, 9, 500);
  hit(229726, 7, 500);
  hit(229799, 8, 500);
  hit(229871, 6, 500);
  hit(229944, 7, 500);
  hit(230016, 5, 500);
  hit(230088, 6, 500);
  hit(230161, 4, 500);
  hit(230233, 5, 500);
  hit(230306, 3, 500);
  hit(230378, 4, 500);
  hit(230451, 2, 500);
  hit(230523, 3, 500);
  hit(bridgeEnd, 1, 500);

  bridgeParticles(bridgeStart, 227117, 'L');
  bridgeParticles(bridgeStart, 227117, 'R');
}

function bridgeParticles(start: number, end: number, side: 'L' | 'R') {
  const dTime = end - start;

  for (let i = 0 ; i < dTime ; i += 50) {
    for (let j = 0 ; j < 3 ; j++) {
      const p = _osb.osbject({
        fileName: 'sb/particle.png',
        startTime: start + i,
        scale: 0.1,
        x: side === 'L' ? -109 : 749,
        y: randomInt(480),
      });

      const active = 1500;

      p.setParameter('A');

      p.moveX({
        changeTime: active,
        change: randomInt(10, 200) * (side === 'L' ? 1 : -1),
        easing: 4,
      });

      p.moveY({
        changeTime: active,
        change: randomInt(-30, 30),
        easing: 4,
      });

      p.fade({
        changeTime: active,
        start: 0.5,
        end: 0,
      });
    }
  }
}

