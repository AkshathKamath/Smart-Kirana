const express = require("express");
const app = express();
const path = require("path");

//Setting views dir
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

//--------------------Routes-------------------------//

const homeRouter = require("./routes/home");
const formRouter = require("./routes/analytics_form");

// Root path
app.use("/", homeRouter);
app.use("/analytics/form", formRouter);

//General analytics and form path

//--------------------Routes-------------------------//

//Handling Errors
app.use((req, res, next) => {
  res.status(404).render("handle_errors", {
    status: 404,
    message: "Page Not Found",
    error:
      "The page you are looking for does not exist! Please enter a valid URL.",
  });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).render("handle_errors", {
    status: 500,
    message: "Internal Server Error",
    error: err.message,
  });
});

module.exports = app;
