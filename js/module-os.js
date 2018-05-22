const os = require("os");
const util = require("util");

const { log, line_separator } = require("./misc");

// ****************************************************************************
const title = "OS info (os):";

const info = {
  "CPU architecture (Node.js)": os.arch(),
  "OS Platform (Node.js)": os.platform(),
  "OS Constants": os.constants,

  "OS Name": os.type(),
  "OS release": os.release(),
  "Hostname of the OS": os.hostname(),
  "User Info": os.userInfo(),
  "Home Directory": os.homedir(),
  "OS Temp Dir": os.tmpdir(),

  "Logical CPU core": os.cpus(),
  "OS Free System Memory (MB)": Math.floor(os.freemem() / 1024 / 1024),
  "OS Total System Memory (MB)": Math.floor(os.totalmem() / 1024 / 1024),
  "Network Interfaces (assigned an address)": os.networkInterfaces(),
  "System Up time (mins)": Math.floor(os.uptime() / 60)
};

// ****************************************************************************
log(line_separator);
log(title + "\n");

log(util.inspect(info, { showHidden: true, depth: null }));
