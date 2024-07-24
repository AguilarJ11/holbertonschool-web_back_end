export default function hasValuesFromArray(set, array) {
  let hasValue = true;
  for (const value of array) {
    if (!set.has(value)) {
      hasValue = false;
    }
  }
  return hasValue;
}
