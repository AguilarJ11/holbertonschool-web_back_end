export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    resolve();
    if (fileName) {
      reject(Error(`${fileName} cannot be processed`));
    }
  });
}
