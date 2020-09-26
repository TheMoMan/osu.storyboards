import { IOsbjectProperty } from ".";

export interface IOsbject {
  getX(): IOsbjectProperty;
  getY(): IOsbjectProperty;
  getFade(): IOsbjectProperty;
  getScale(): IOsbjectProperty;
  getRotation(): IOsbjectProperty;
  getColour(): IOsbjectProperty
  getVectorScale(): IOsbjectProperty;
}
