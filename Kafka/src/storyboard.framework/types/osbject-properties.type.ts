export type ColourValue = [number, number, number];
export type VectorValue = [number, number];

export type OsbjectArrayValue = ColourValue | VectorValue;
export type OsbjectValue = number | OsbjectArrayValue;

export type Layer = 'Background' | 'Pass' | 'Fail' | 'Foreground';
