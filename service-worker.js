const CACHE_NAME = "edgegrid-v1";

const APP_SHELL = [
    "./",
    "./index.html",
    "./about.html",
    "./courses.html",
    "./tools.html",
    "./blog.html",
    "./contact.html",
    "./faq.html",
    "./VIPmembers.html",
    "./css/styles.css",
    "./js/main.js",
    "./manifest.json"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(APP_SHELL);
        })
    );

    self.skipWaiting();
});

self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => cacheName !== CACHE_NAME)
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );

    self.clients.claim();
});

self.addEventListener("fetch", event => {
    if (event.request.method !== "GET") {
        return;
    }

    event.respondWith(
        caches.match(event.request).then(cachedResponse => {
            return cachedResponse || fetch(event.request).catch(() => {
                return caches.match("./index.html");
            });
        })
    );
});
