export default function loadBalancer(chinaDownload, USDownload) {
  return new Promise((resolve) => {
    const china = chinaDownload();
    const US = USDownload();

    Promise.race([china, US]).then((result) => {
      resolve(result);
    });
  });
}
