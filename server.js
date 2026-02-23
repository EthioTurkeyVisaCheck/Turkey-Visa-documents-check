const express = require("express");
const multer = require("multer");
const axios = require("axios");
const FormData = require("form-data");
const fs = require("fs");

const app = express();
const upload = multer({ dest: "uploads/" });

const BOT_TOKEN = "8371746608:AAGXkauY6uJH7DwvhuvjkmSrjl4pJiux0Nc_TOKEN";
const CHAT_ID = "8349642445";

app.post("/upload", upload.single("document"), async (req, res) => {
  try {
    const filePath = req.file.path;

    const form = new FormData();
    form.append("chat_id", CHAT_ID);
    form.append("document", fs.createReadStream(filePath));

    await axios.post(
      `https://api.telegram.org/bot${BOT_TOKEN}/sendDocument`,
      form,
      { headers: form.getHeaders() }
    );

    fs.unlinkSync(filePath);
    res.send({ success: true });
  } catch (error) {
    console.error(error);
    res.send({ success: false });
  }
});

app.listen(3000, () => console.log("Server running on port 3000"));