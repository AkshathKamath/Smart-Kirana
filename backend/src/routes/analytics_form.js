const express = require("express");
const router = express.Router();
const axios = require("axios");

//Post req
router.post("/", async (req, res) => {
  try {
    //Upload file to S3 bucket
    console.log("File upload successful!");
    const response = await axios.get("http://localhost:4000/show/clean");
    const data = response.data;
    console.log(data.msg);
    res.redirect("/analytics/form");
  } catch (err) {
    console.error("Error uploading file!", err);
    res.status(500).send("Internal Server Error");
  }
});

//Get req
router.get("/", async (req, res) => {
  try {
    const response1 = await axios.get("http://localhost:4000/show/general");
    const data = JSON.parse(response1.data);
    // console.log(Array.isArray(data)); //To test api conn

    console.log("API connection success!");
    res.render("analytics_form", { data });
  } catch (err) {
    console.error("Error in API connection!", err);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
