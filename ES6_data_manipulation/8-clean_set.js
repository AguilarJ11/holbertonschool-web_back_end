export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }
  const stringRes = [];
  for (const value of set) {
    if (value.includes(startString)) {
      const stringPart = value.substring(startString.length);
      stringRes.push(stringPart);
    }
  }
  return stringRes.join('-');
}
