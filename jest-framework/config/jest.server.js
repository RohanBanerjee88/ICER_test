const commonConfig = require("./jest.common");

module.exports = {
  ...commonConfig,
  setupFilesAfterEnv: ["<rootDir>/setup/setupServer.js"],
  // Add any server-specific configurations
};
