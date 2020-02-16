export function normaliseValue(value: number, array: number[]): number {
    return (value - Math.min(...array)) / (Math.max(...array) - Math.min(...array));
}

export function normaliseIndex(index: number, array: number[]): number {
    return normaliseValue(array[index], array);
}
