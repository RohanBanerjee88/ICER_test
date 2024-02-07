const cacheService = require("./cacheService");
const { getDataWithCaching } = require("./app");

jest.mock("./cacheService"); // Automatically mocks the cacheService module

describe("getDataWithCaching", () => {
  beforeEach(() => {
    cacheService.get.mockReset(); // Reset mock function before each test
    cacheService.set.mockReset();
  });

  test("should fetch data from the server on cache miss", () => {
    cacheService.get.mockReturnValue(undefined); // Simulate cache miss
    const serverData = "Server data";
    jest.spyOn(console, "log").mockImplementation(() => {});
  
    const result = getDataWithCaching("123");
  
    expect(result).toBe(serverData);
    expect(cacheService.set).toHaveBeenCalledWith("123", serverData);
    expect(console.log).toHaveBeenCalledWith("Fetching data from server for id 123");
  });
  

  test("should return cached data on cache hit", () => {
    const cachedData = "Cached data";
    cacheService.get.mockReturnValue(cachedData); // Simulate cache hit
    jest.spyOn(console, "log").mockImplementation(() => {});

    const result = getDataWithCaching("123");

    expect(result).toBe(cachedData);
    expect(cacheService.set).not.toHaveBeenCalled(); // Cache should not be updated on hit
    expect(console.log).toHaveBeenCalledWith("Cache hit for id 123");
  });
});

