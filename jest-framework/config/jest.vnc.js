const commonConfig = require("./jest.common");

module.exports = {
  ...commonConfig,
  setupFilesAfterEnv: ["<rootDir>/setup/setupVNC.js"],
  // Add any VNC-specific configurations
};
