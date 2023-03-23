// self.addEventListener('fetch', e => {
//     const {url} = e.request;
//     const newUrl = url.replace(url, 'https://example.com/');
//     console.log(newUrl);
//     e.respondWith(fetch(newUrl));
    
//   });

self.addEventListener("fetch", function (event) {
    if (isCrossOrigin(event.request)) {
      return;
    }
    event.respondWith(handleRequest(event));
  });
  
  const handleRequest = async event => {
    let response = await fetch(event.request);
    storeData(request, response.clone());
    return response;
  };