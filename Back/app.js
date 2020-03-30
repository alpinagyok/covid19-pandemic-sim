var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");

var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");

var app = express();

// app.get('/api/hello', (req, res) => {
//   res.send({ express: 'Hello From Express' });
// });

app.get("/api/hello", callName);

function callName(req, res) {
  // let { PythonShell } = require("python-shell");
  // var package_name = "pytube";
  // let options = {
  //   args: [package_name]
  // };
  // PythonShell.run("./install_package.py", options, function(err, results) {
  //   if (err) throw err;
  //   else console.log(results);
  // });

  // Use child_process.spawn method from
  // child_process module and assign it
  // to variable spawn
  var spawn = require("child_process").spawn;

  // Parameters passed in spawn -
  // 1. type_of_script
  // 2. list containing Path of the script
  //    and arguments for the script

  // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will
  // so, first name = Mike and last name = Will
  // var process = spawn('python',["./hello.py",
  //                         req.query.firstname,
  //                         req.query.lastname] );
  // var process = spawn('python',["./coronamodel-master/model.py"] );
  // var process = spawn("python", ["./model.py"]);
  // var process = spawn("python", ["./install_package.py"]);
  var process = spawn("python", [
    "./model.py",
    req.query.switch0,
    req.query.start0,
    req.query.end0,
    req.query.eff0,
    req.query.switch1,
    req.query.start1,
    req.query.end1,
    req.query.eff1
  ]);

  // Takes stdout data from script which executed
  // with arguments and send this data to res object

  // res.send({ express: 'Hello From Express' });

  process.stdout.on("data", function(data) {
    res.send({ express: data.toString() });
    // res.send('Hello From Express');
  });
  process.stdout.on("data", data => {
    console.log(`data:${data}`);
  });
  process.stderr.on("data", data => {
    console.log(`error:${data}`);
  });
  process.on("close", () => {
    console.log("Closed");
  });
}

app.use(express.static(path.join(__dirname, "build")));

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "build", "index.html"));
});

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "jade");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use("/", indexRouter);
app.use("/users", usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

module.exports = app;
