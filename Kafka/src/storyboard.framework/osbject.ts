import { IOsbject, IOsbjectProperty, IOsbjectConstructor, IOsbjectModifier } from "./interfaces";
import { sumTwoArrays } from "./utils";
import { OsbjectValue, OsbjectArrayValue } from "./types";

export class Osbject implements IOsbject {
    private osbCode: string[];

    private _x: IOsbjectProperty;
    private _y: IOsbjectProperty;
    private _scale: IOsbjectProperty;
    private _fade: IOsbjectProperty;
    private _rotation: IOsbjectProperty;
    private _colour: IOsbjectProperty;
    private _vector: IOsbjectProperty;

    constructor(osbjs: IOsbjectConstructor) {
        if (!osbjs.fileName) throw new Error('File name not given.');

        const startTime = osbjs.startTime ? osbjs.startTime : 0;

        this._x = {
            value: <number>osbjs.x ?? 320,
            time: startTime,
        };
        this._y = {
            value: <number>osbjs.y ?? 240,
            time: startTime,
        }
        this._scale = {
            value: <number>osbjs.scale ?? 1,
            time: startTime,
        }
        this._fade = {
            value: <number>osbjs.fade ?? 1,
            time: startTime,
        }
        this._rotation = {
            value: <number>osbjs.rotation ?? 0,
            time: startTime,
        }
        this._colour = {
            value: osbjs.colour ?? [255, 255, 255],
            time: startTime,
        }
        this._vector = {
            value: osbjs.vector ?? [1, 1],
            time: startTime,
        }

        const fileName = osbjs.fileName;
        const layer = osbjs.layer ?? 'Background';
        const anchor = osbjs.anchor ?? 'Centre';

        this.osbCode = [
            `Sprite,${layer},${anchor},"${fileName}",${this._x.value},${this._y.value}`
        ];

        if (osbjs.scale != null)
            this.osbCode.push(` S,0,${startTime},,${osbjs.scale}`);
        if (osbjs.fade != null)
            this.osbCode.push(` F,0,${startTime},,${osbjs.fade}`);
        if (osbjs.rotation != null)
            this.osbCode.push(` R,0,${startTime},,${osbjs.rotation}`);
        if (osbjs.colour != null)
            this.osbCode.push(` C,0,${startTime},,${osbjs.colour.join(',')}`);
        if (osbjs.vector != null)
            this.osbCode.push(` V,0,${startTime},,${osbjs.vector.join(',')}`);
    }

    getX(): IOsbjectProperty {
        return this._x;
    }

    moveX(x: IOsbjectModifier): void {
        this.sbFunction(x, 'MX');
    }

    getY(): IOsbjectProperty {
        return this._y;
    }

    moveY(y: IOsbjectModifier): void {
        this.sbFunction(y, 'MY');
    }

    getScale(): IOsbjectProperty {
        return this._scale;
    }

    scale(scale: IOsbjectModifier): void {
        this.sbFunction(scale, 'S');
    }

    getFade(): IOsbjectProperty {
        return this._fade;
    }

    fade(fade: IOsbjectModifier): void {
        // console.log(this._fade)
        this.sbFunction(fade, 'F');
        // console.log(this._fade)
    }

    getRotation(): IOsbjectProperty {
        return this._rotation;
    }

    rotate(rotation: IOsbjectModifier): void {
        this.sbFunction(rotation, 'R');
    }

    getColour(): IOsbjectProperty {
        return this._colour;
    }

    colour(colour: IOsbjectModifier): void {
        this.sbFunction(colour, 'C');
    }

    getVectorScale(): IOsbjectProperty {
        return this._vector;
    }

    vector(vector: IOsbjectModifier): void {
        this.sbFunction(vector, 'V');
    }

    setParameter(param: string, time?: number): void {
        if (!time) time = this._fade.time;
        this.osbCode.push(` P,0,${time},,${param}`);
    }

    toString(): string {
        return this.osbCode.join('\n');
    }

    private sbFunction(dF: IOsbjectModifier, func: string): void {
        if ((dF.endTime != null) && (dF.changeTime != null))
            throw new Error('Can only do either endTime or changeTime (not both).');

        let sbParameter: IOsbjectProperty;

        switch (func) {
            case 'MX': 
                sbParameter = this._x;
                break;
            case 'MY':
                    sbParameter = this._y;
                break;
            case 'F':
                    sbParameter = this._fade;
                break;
            case 'S':
                    sbParameter = this._scale;
                break;
            case 'R':
                    sbParameter = this._rotation;
                break;
            case 'C':
                    sbParameter = this._colour;
                break;
            case 'V':
                    sbParameter = this._vector;
                break;
            default:
                throw new Error('Invalid function.');
        }

        let {time, value} = sbParameter;

        if (time == undefined || value == undefined)
            throw new Error();

        const easing: number = <number>dF.easing ?? 0;
        const startTime: number = <number>dF.startTime ?? time;
        const endTime: number = <number>dF.endTime ?? startTime + (<number>dF.changeTime ?? 0);

        if (!Number.isInteger(startTime)) throw new Error(`Non-integer _time. ${startTime}, ${endTime}`);

        let start: number | number[];
        let end: number | number[] | undefined;

        let startAsString: string = '';
        let endAsString: string = '';

        if (['MX', 'MY', 'F', 'S', 'R'].includes(func)) {
            start = <number>dF.start ?? <number>value;
            startAsString = String(start);
            
            value = <number>value;
            dF.change = <number>dF.change;

            end = <number>dF.end ?? (dF.change ? value + dF.change : undefined);
            if (end != null) endAsString = String(end);
        }
        if (['C', 'V'].includes(func)) {
            start = dF.start ? <OsbjectArrayValue>dF.start : <OsbjectArrayValue>value;
            startAsString = start.join(',');

            value = <OsbjectArrayValue>value;
            dF.change = <OsbjectArrayValue>dF.change;

            if (dF.end != null) end = <OsbjectArrayValue>dF.end;
            if (dF.change != null) end = sumTwoArrays(<OsbjectArrayValue>dF.change, value);
            end = <OsbjectArrayValue>end;

            if (func === 'C') {
                end.forEach(c => {
                    if (c > 255 || !Number.isInteger(c)) throw new Error(`Invalid RGB value: ${end}`)
                });
            }

            if (end != null) endAsString = end.join(',');
        }

        let code: string = ` ${func},${easing},${startTime},${endTime},${startAsString}`;
        if (end != null) code += `,${endAsString}`;

        this.osbCode.push(code);

        if (end != null) sbParameter.value = <OsbjectValue>end;
        sbParameter.time = endTime ? endTime : startTime;
    }
}
