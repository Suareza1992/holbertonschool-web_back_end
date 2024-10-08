function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const int8view = new Int8Array(buffer);
  int8view[position] = value;
  return new DataView(buffer);
}

export default createInt8TypedArray;
