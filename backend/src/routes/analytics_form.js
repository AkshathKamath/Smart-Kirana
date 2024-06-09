const express = require("express");
const router = express.Router();
const axios = require("axios");

//Post req
router.post("/", (req, res) => {
  try {
    //Upload file to S3 bucket
    console.log("File upload successful!");
    const data = null;
    res.render("analytics_form", { data });
  } catch (err) {
    console.error("Error uploading file!", err);
    res.status(500).send("Internal Server Error");
  }
});

//Get req
router.get("/", async (req, res) => {
  try {
    const response = await axios.get("http://localhost:4000/show/test");
    const data = response.data;
    // console.log(data.size); //To test api conn

    console.log("API connection success!");
    res.render("analytics_form", { data });
  } catch (err) {
    console.error("Error in API connection!", err);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
