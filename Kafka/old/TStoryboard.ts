import * as fs from 'fs';

export class TStoryboard {
    private background: Osbject[];
    private foreground: Osbject[];
    private location: string;

    constructor(location: string) {
        this.location = location;
        this.background = [];
        this.foreground = [];
    };

    osbject(
        fileName: string,
        x = 320,
        y = 240,
        layer = 'Background',
        anchor = 'Centre',
        startTime = 0,
    ): Osbject {
        const osbject = new Osbject(fileName, x, y, layer, anchor, startTime);

        switch (layer) {
            case 'Background' :
            case 'bg' :
                this.background.push(osbject);
                break;
            case 'Foreground' :
            case 'fg' :
                this.foreground.push(osbject);
                break;
            default:
                throw new Error(`Cannot assign layer ${layer}`);
        }

        return osbject;
    };

    export(): void {
        const osbAsString =
            '[Events]\n' +
            '//Background and Video events\n' +
            '//Storyboard Layer 0 (Background)\n' +
            this.osbjectsToString(this.background) +
            '//Storyboard Layer 1 (Fail)\n' +
            '//Storyboard Layer 2 (Pass)\n' +
            '//Storyboard Layer 3 (Foreground)\n' +
            this.osbjectsToString(this.foreground) +
            '//Storyboard Sound Samples\n';

        fs.writeFile(this.location, osbAsString, (err: any) => {
            if (err) throw err;
            console.log(`Writing to ${this.location}...`)
            console.log('Done!');
        });
    }

    private osbjectsToString(osbjects: Osbject[]): string {
        let out = '';
        osbjects.forEach(osbject => {
            out += osbject.toString() + '\n';
        });
        return out;
    }
}

export interface IOsbject {}

class Osbject implements IOsbject {
    private osbCode: string[];

    private x: number;
    private xTime: number;
    private y: number;
    private yTime: number;
    private scale: number;
    private scaleTime: number;
    private fade: number;
    private fadeTime: number;
    private rotation: number;
    private rotationTime: number;
    private colour: [number, number, number];
    private colourTime: number;
    private vector: [number, number];
    private vectorTime: number;
    // private parameter: string;
    // private parameterTime: number;

    constructor(
        private readonly fileName: string,
        private readonly startX: number = 320,
        private readonly startY: number = 240,
        private readonly layer: string = 'Background',
        private readonly anchor: string = 'Centre',
        private readonly startTime: number = 0,
    ) {
        this.osbCode = [
            `Sprite,${layer},${anchor},"${fileName}",${startX},${startY}`
        ];

        this.x = startX;
        this.y = startY;
        this.scale = 1;
        this.fade = 1;
        this.rotation = 0;
        this.colour = [255, 255, 255];
        this.vector = [1, 1];
        // this.parameter = '';
        
        this.xTime = startTime;
        this.yTime = startTime;
        this.scaleTime = startTime;
        this.fadeTime = startTime;
        this.rotationTime = startTime;
        this.colourTime = startTime;
        this.vectorTime = startTime;
        // this.parameterTime = startTime;
    }

    getX(): [number, number] {
        return [this.x, this.xTime];
    }

    setX(x: number, time: number, write: boolean = false): void {
        if (time < this.xTime)
            throw new Error('Cannot go backwards in time.')
        
        this.x = x;
        this.xTime = time;

        if (write) {
            this.osbCode.push(` F,0,${time},,${x}`)
        }
    }

    moveXBy(x: number, time: number, easing: number = 0): void {
        this.checkValidTime(time);
        
        const newX: number = this.x + x;
        const newTime: number = this.xTime + time;

        const newTimeS: string = newTime !== this.xTime ? newTime.toString() : '';

        this.osbCode.push(` MX,${easing},${this.xTime},${newTimeS},${this.x},${newX}`);

        this.x = newX;
        this.xTime = newTime;
    }

    getY(): [number, number] {
        return [this.y, this.yTime];
    }

    setY(y: number, time: number, write: boolean = false): void {
        if (time < this.yTime)
            throw new Error('Cannot go backwards in time.')
        
        this.y = y;
        this.yTime = time;

        if (write) {
            this.osbCode.push(` F,0,${time},,${y}`)
        }
    }

    moveYBy(y: number, time: number, easing: number = 0): void {
        this.checkValidTime(time);
        
        const newY: number = this.y + y;
        const newTime: number = this.yTime + time;

        const newTimeS: string = newTime !== this.yTime ? newTime.toString() : '';

        this.osbCode.push(` MY,${easing},${this.yTime},${newTimeS},${this.y},${newY}`);

        this.y = newY;
        this.yTime = newTime;
    }

    getFade(): [number, number] {
        return [this.fade, this.fadeTime];
    }

    setFade(fade: number, time: number, write: boolean = false): void {
        if (time < this.fadeTime)
            throw new Error('Cannot go backwards in time.')
        
        this.fade = fade;
        this.fadeTime = time;

        if (write) {
            this.osbCode.push(` F,0,${time},,${fade}`)
        }
    }

    fadeBy(fade: number, time: number, easing: number = 0): void {
        this.checkValidTime(time);
        
        const newFade: number = this.fade + fade;
        const newTime: number = this.fadeTime + time;

        const newTimeS: string = newTime !== this.fadeTime ? newTime.toString() : '';

        this.osbCode.push(` F,${easing},${this.fadeTime},${newTimeS},${this.fade},${newFade}`);

        this.fade = newFade;
        this.fadeTime = newTime;
    }

    getScale(): [number, number] {
        return [this.scale, this.scaleTime];
    }

    setScale(scale: number, time: number, write: boolean = false): void {
        if (time < this.scaleTime)
            throw new Error('Cannot go backwards in time.')
        
        this.scale = scale;
        this.scaleTime = time;

        if (write) {
            this.osbCode.push(` S,0,${time},,${scale}`)
        }
    }

    scaleBy(scale: number, time: number, easing: number = 0): void {
        this.checkValidTime(time);
        
        const newScale: number = this.scale + scale;
        const newTime: number = this.scaleTime + time;

        const newTimeS: string = newTime !== this.scaleTime ? newTime.toString() : '';

        this.osbCode.push(` S,${easing},${this.scaleTime},${newTimeS},${this.scale},${newScale}`);

        this.scale = newScale;
        this.scaleTime = newTime;
    }

    getRotation(): [number, number] {
        return [this.rotation, this.rotationTime];
    }

    setRotation(rotation: number, time: number, write: boolean = false): void {
        if (time < this.rotationTime)
            throw new Error('Cannot go backwards in time.')
        
        this.rotation = rotation;
        this.rotationTime = time;

        if (write) {
            this.osbCode.push(` F,0,${time},,${rotation}`)
        }
    }

    rotateBy(rotation: number, time: number, easing: number = 0): void {
        this.checkValidTime(time);
        
        const newRotation: number = this.rotation + rotation;
        const newTime: number = this.rotationTime + time;

        const newTimeS: string = newTime !== this.rotationTime ? newTime.toString() : '';

        this.osbCode.push(` R,${easing},${this.rotationTime},${newTimeS},${this.rotation},${newRotation}`);

        this.rotation = newRotation;
        this.rotationTime = newTime;
    }

    getColour(): [[number, number, number], number] {
        return [this.colour, this.colourTime];
    }

    setColour(colour: [number, number, number], time: number, write: boolean = false): void {
        if (time < this.colourTime)
            throw new Error('Cannot go backwards in time.')

        this.colour = colour;
        this.colourTime = time;

        if (write) {
            this.osbCode.push(` F,0,${time},,${this.tupleToString(colour)}`)
        }
    }

    colourBy(colour: [number, number, number], time: number, easing: number = 0): void {
        this.checkValidTime(time);

        // Trade memory for access speed.
        const newColour: [number, number, number] = [0, 0, 0];
        for (let i = 0 ; i < 3 ; i++) {
            const newC: number = this.colour[i] + colour[i];
            
            if (newC > 255 || newC < 0)
                throw new Error('Colour goes out of range.')

            newColour[i] = newC;
        }

        const newTime: number = this.colourTime + time;
        const newTimeS: string = newTime !== this.colourTime ? newTime.toString() : '';

        const colourS: string = this.tupleToString(this.colour);
        const newColourS: string = this.tupleToString(colour);

        this.osbCode.push(` C,${easing},${this.colourTime},${newTimeS},${colourS},${newColourS}`);

        this.colour = newColour;
        this.colourTime = newTime;
    }

    getVectorScale(): [[number, number], number] {
        return [this.vector, this.vectorTime];
    }

    setVectorScale(vector: [number, number], time: number, write: boolean = false): void {
        if (time < this.vectorTime)
            throw new Error('Cannot go backwards in time.')

        this.vector = vector;
        this.vectorTime = time;

        if (write) {
            this.osbCode.push(` F,0,${time},,${this.tupleToString(vector)}`)
        }
    }

    vectorScaleBy(vector: [number, number], time: number, easing: number = 0): void {
        this.checkValidTime(time);

        const newVector = this.vector;
        for (let i = 0 ; i < 2 ; i++) {
            newVector[i] += vector[i];
        }

        const vectorS: string = this.tupleToString(this.vector);
        const newVectorS: string = this.tupleToString(newVector);

        const newTime: number =  this.vectorTime + time;
        const newTimeS: string = newTime !== this.vectorTime ? newTime.toString() : '';

        this.osbCode.push(` V,${easing},${this.vectorTime},${newTimeS},${vectorS},${newVectorS}`);

        this.vector = newVector;
        this.vectorTime = newTime;
    }

    setParameter(parameter: string, time: number): void {
        this.osbCode.push(` P,0,${time},,${parameter}`);
    } 

    // func(
    //     func: string,
    //     easing: number,
    //     startTime: number,
    //     endTime: number,
    //     val1: number | string,
    //     val2?: number,
    //     val3?: number,
    //     val4?: number,
    //     val5?: number,
    //     val6?: number,
    // ): void {
    //     let f = ` ${func}`;

    //     for (let i = 1 ; i < arguments.length ; i++) {
    //         f += `,${this.isDefined(arguments[i]) ? arguments[i] : ''}`;
    //     }

    //     this.osbCode.push(f);
    // }

    toString(): string {
        return this.osbCode.join('\n');
    }

    private isDefined(x: any): boolean {
        return (x !== undefined && x !== null);
    }

    private checkValidTime(time: number): void {
        if (time < 0)
            throw new Error('Cannot use negative time.');
        if (!Number.isInteger(time))
            throw new Error('Cannot use non-integer time.')
    }

    private tupleToString(tuple: any[]): string {
        let output = '';

        tuple.forEach(element => {
            output += `${element},`;
        });

        return output.slice(0, -1);
    }
}
