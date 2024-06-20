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
    const response1 = await axios.get("http://localhost:4000/show/general/1");
    const data1 = JSON.parse(response1.data);
    const response2 = await axios.get("http://localhost:4000/show/size");
    const data2 = response2.data;
    const response3 = await axios.get("http://localhost:4000/show/general/2");
    const data3 = JSON.parse(response3.data);
    // console.log(data3);
    const data = {
      ...data2,
      list1: data1,
      list2: data3,
    };
    // console.log(data);
    // console.log(size);
    // console.log(Array.isArray(data)); //To test api conn

    console.log("API connection success!");
    res.render("analytics_form", { data });
  } catch (err) {
    console.error("Error in API connection!", err);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
