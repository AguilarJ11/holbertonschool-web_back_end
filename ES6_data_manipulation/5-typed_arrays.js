export default function createInt8TypedArray(length, position, value) {
  const arrayBuff = new ArrayBuffer(length);
  const int8 = new Int8Array(arrayBuff);

  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  int8[position] = value;
}
