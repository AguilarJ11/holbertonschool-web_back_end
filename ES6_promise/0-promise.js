export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const vamo = 'lopibeh';
    if (vamo) {
      resolve('Vamo lo pibeh');
    } else {
      reject(Error('Te pusiste la gorra'));
    }
  });
}
