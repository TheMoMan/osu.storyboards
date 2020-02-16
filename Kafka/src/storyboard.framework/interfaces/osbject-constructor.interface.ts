export interface IOsbjectConstructor {
    readonly fileName: string;
    readonly layer?: string;
    readonly anchor?: number;
    readonly x?: number;
    readonly y?: number;
    readonly scale?: number;
    readonly fade?: number;
    readonly rotation?: number;
    readonly colour?: [number, number, number];
    readonly vector?: [number, number];
    readonly parameter?: string;
    readonly startTime?: number;
}
