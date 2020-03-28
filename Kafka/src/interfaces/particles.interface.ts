import { ColourValue } from "../storyboard.framework";

export interface ParticlesFadeParams {
    inTime?: number,
    outTime?: number, 
    peaks: [number, number],
    inDuration?: number,
    outDuration?: number,
}

export interface ParticlesParams {
    fileName: string;
    startTime: number;
    endTime: number;
    speeds: [number, number];
    translateEasing?: number;
    deviation?: [number, number];
    density: number;
    spawnRate: number;
    colours?: ColourValue[];
    scales: [number, number];
    fade?: ParticlesFadeParams,
}

export interface ParticlesHorizontal extends ParticlesParams {
    startX?: number,
    endX?: number,
}
