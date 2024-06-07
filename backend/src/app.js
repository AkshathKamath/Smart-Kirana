const express = require("express");
const app = express();
const path = require("path");

// Set EJS as the view engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Route for rendering the EJS file
app.get("/", (req, res) => {
  res.render("data_upload");
});

module.exports = app;
