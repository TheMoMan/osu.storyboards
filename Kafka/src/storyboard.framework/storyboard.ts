import * as fs from 'fs';
import { IOsbjectConstructor } from './interfaces';
import { Osbject } from './osbject';

export class Storyboard {
    private background: Osbject[];
    private fail: Osbject[];
    private pass: Osbject[];
    private foreground: Osbject[];
    private location: string;

    constructor(location: string) {
        this.location = location;
        this.background = [];
        this.fail = [];
        this.pass = [];
        this.foreground = [];
    };

    osbject(osbjs: IOsbjectConstructor): Osbject {
        const osbject = new Osbject(osbjs);

        const layer = osbjs.layer ? osbjs.layer : 'Background';

        switch (layer) {
            case 'Background' :
                this.background.push(osbject);
                break;
            case 'Foreground' :
                this.foreground.push(osbject);
                break;
            case 'Fail' :
                this.fail.push(osbject);
                break;
            case 'Pass' :
                this.pass.push(osbject);
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
            this.osbjectsToString(this.fail) +
            '//Storyboard Layer 2 (Pass)\n' +
            this.osbjectsToString(this.pass) +
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
