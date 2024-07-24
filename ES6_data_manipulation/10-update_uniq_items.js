export default function updateUniqueItems(imTheMap) {
  if (!(imTheMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [key, value] of imTheMap) {
    if (value === 1) {
      imTheMap.set(key, 100);
    }
  }
  return imTheMap;
}
