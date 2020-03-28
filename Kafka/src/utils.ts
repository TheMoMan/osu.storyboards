export function normaliseValue(value: number, array: number[]): number {
    return (value - Math.min(...array)) / (Math.max(...array) - Math.min(...array));
};

export function normaliseIndex(index: number, array: number[]): number {
    return normaliseValue(array[index], array);
};

export function randomInt(max: number, min: number = 0): number {
    return Math.floor(Math.random() * (max - min + 1) + min);
};

export function randomRange(max: number, min: number = 0, decimals?: number): number {
    const value = Math.random() * (max - min) + min;

    if (decimals || decimals === 0) {
        return Number(value.toFixed(decimals));
    }

    return value;
}

export function randomRangeFromArray(range: [number, number], decimals?: number): number {
    return randomRange(range[0], range[1], decimals);
}

export function pickRandomFromArray(arr: any[]): any {
    if (arr.length === 1) return arr[0];
    if (arr.length > 0) return arr[randomInt(arr.length - 1)];
    return undefined;
};
