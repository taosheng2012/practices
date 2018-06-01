// The process object is a global that provides information about, and control over,
// the current Node.js process.
// As a global, it is always available to Node.js applications without using require().
const util = require("util");

const { log, line_separator } = require("./misc");

// ****************************************************************************
const title = "Node.js info:";

const info = {
  "Config Options": process.config,
  "Current Working Directory": process.cwd(),
  "User Environment": process.env,
  "Node.js Executable Pathname": process.execPath,
  "Memory Usage": process.memoryUsage(),
  "OS Platform": process.platform,
  Metadata: process.release,
  Version: process.versions
};

process.on("exit", exitCode => {
  log(`Node.js is exiting with code ${exitCode}`);
});

// ****************************************************************************
log(line_separator);
log(title + "\n");

log(util.inspect(info, { showHidden: true, depth: null }));
