// In the Node.js module system, each file is treated as a separate module.
/*Functions and objects are added to the root of a module by specifying additional 
properties on the special exports object.*/
const { log, line_separator } = require("./misc");

// ****************************************************************************
/*
The module wrapper
exports, require, module, __filename, __dirname
*/
const Module = require("module");

// ****************************************************************************
const title = "Module info :";

log(line_separator);
log(title + "\n");

log("Check Main :");
if (require.main === module) {
  log("This is a main module.");
} else {
  log("This isn't a main module.");
}
log(`This module is ${__filename} in the folder of ${__dirname}.\n`);

log("Paths Searched During Resolution :");
log(require.resolve.paths("aaa"));
log("");

log(module);
log("");

log("Builtin Modules (provided by Node.js):");
log(Module.builtinModules);
