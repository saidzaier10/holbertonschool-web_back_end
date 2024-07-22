export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  let result = '';
  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      if (result !== '') {
        result += '-';
      }
      result += value.slice(startString.length);
    }
  }
  return result;
}
