const express = require("express");
const router = express.Router();

//Home route
router.get("/", (req, res) => {
  try {
    res.redirect("/home");
  } catch (err) {
    console.error("Error rendering home page!", err);
    res.status(500).send("Internal Server Error");
  }
});

router.get("/home", (req, res) => {
  try {
    res.render("home");
  } catch (err) {
    console.error("Error rendering home page!", err);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
