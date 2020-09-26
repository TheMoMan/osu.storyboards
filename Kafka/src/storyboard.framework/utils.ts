export function sumTwoArrays(a: number[], b: number[]): number[] {
  if (a.length !== b.length) throw new Error('Both arrays must be same length.')

  for (let i = 0 ; i < a.length ; i++) {
    a[i] += b[i];
  }

  return a;
}

export function capitaliseFirstChar(s: string) {
  return s.charAt(0).toLocaleUpperCase() + s.slice(1);
}
