const NodeCache = require("node-cache");
const cache = new NodeCache();

const CACHE_TTL_SECONDS = 60; // Cache items expire after 60 seconds

function set(key, value) {
  cache.set(key, value, CACHE_TTL_SECONDS);
}

function get(key) {
  return cache.get(key);
}

function del(key) {
  cache.del(key);
}

module.exports = { set, get, del };

