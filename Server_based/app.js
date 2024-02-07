const cacheService = require("./cacheService");

function fetchDataFromServer(id) {
  // Simulating fetching data from a server
  console.log(`Fetching data from server for id ${id}`);
  return `Data for id ${id}`;
}

function getDataWithCaching(id) {
  const cachedData = cacheService.get(id);

  if (cachedData) {
    console.log(`Cache hit for id ${id}`);
    return cachedData;
  }

  const fetchedData = fetchDataFromServer(id);
  cacheService.set(id, fetchedData);
  return fetchedData;
}

module.exports = { getDataWithCaching };

