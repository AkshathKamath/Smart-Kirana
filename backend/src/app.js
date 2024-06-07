const express = require("express");
const app = express();
const path = require("path");
const multer = require("multer");
const axios = require("axios");

//Setting views dir
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

//Storing the file
const uploadsDir = path.join(__dirname, "../..", "dataset");

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, uploadsDir);
  },
  filename: (req, file, cb) => {
    const file_name = "supermarket" + path.extname(file.originalname);
    cb(null, file_name);
  },
});
const upload = multer({ storage: storage });

// Routes
//-----------------------------------------------------//

app.get("/", (req, res) => {
  try {
    res.render("data_upload");
  } catch (err) {
    console.error("Error rendering home page!", err);
    res.status(500).send("Internal Server Error");
  }
});

//-----------------------------------------------------//

app.post("/analyticsForm", upload.single("file"), (req, res) => {
  try {
    console.log("File upload successful!");
    const data = null;
    res.render("analytics_form", { data });
  } catch (err) {
    console.error("Error uploading file!", err);
    res.status(500).send("Internal Server Error");
  }
});

//-----------------------------------------------------//

app.get("/analyticsForm", async (req, res) => {
  try {
    const response = await axios.get("http://localhost:4000/showData");
    const data = response.data;
    // console.log(data.size); //To test api conn

    console.log("API connection success!");
    res.render("analytics_form", { data });
  } catch (err) {
    console.error("Error in API connection!", err);
    res.status(500).send("Internal Server Error");
  }
});

//-----------------------------------------------------//

module.exports = app;
