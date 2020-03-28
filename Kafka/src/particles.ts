import { Storyboard, ColourValue } from "./storyboard.framework";
import { ParticlesHorizontal } from "./interfaces";
import {
    randomInt,
    pickRandomFromArray as randArray,
    randomRangeFromArray as randRangeArray,
} from "./utils";

export function particlesHorizontal(osb: Storyboard, params: ParticlesHorizontal ): void {    
    for (let i = params.startTime ; i < params.endTime ; i += (params.spawnRate)) {
        for (let j = 0 ; j < params.density ; j++) {
            const colour: ColourValue = params.colours 
                ? randArray(params.colours)
                : [255, 255, 255];

            const startX = params.startX ?? 720;
            const endX = params.endX ?? -120;
            
            const p = osb.osbject({
                colour,
                fileName: params.fileName,
                x: startX,
                y: randomInt(480),
                startTime: i,
                scale: randRangeArray(params.scales, 2),
            });

            const activeTime = Math.round(
                ((startX - endX) / randRangeArray(params.speeds, 0)) * 1000
            );

            p.moveX({
                endTime: i + activeTime,
                end: endX,
                easing: params.translateEasing,
            });

            if (params.fade) {
                const fade = params.fade;

                if (
                    fade.inTime != undefined && fade.inDuration != undefined &&
                    i < fade.inTime + fade.inDuration
                ) {
                    p.fade({
                        startTime: fade.inTime,
                        changeTime: fade.inDuration,
                        start: 0,
                        end: randRangeArray(fade.peaks, 2),
                    });
                }
                
                if (
                    fade.outTime != undefined && fade.outDuration != undefined &&
                    i + activeTime > fade.outTime + fade.outDuration
                ) {
                    p.fade({
                        startTime: fade.outTime,
                        changeTime: fade.outDuration,
                        end: 0,
                    })
                }
            }

            if (params.deviation) {
                p.moveY({
                    endTime: i + activeTime,
                    change: randRangeArray(params.deviation, 0),
                });
            }
        }
    }
}
