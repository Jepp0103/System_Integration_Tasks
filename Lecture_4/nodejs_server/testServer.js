//Creating the server
const express = require("express");
const app = express();
var xmlparser = require('express-xml-bodyparser');
const csv = require('csv');
const fileSystem = require("fs");
const port = 3333;

// parse application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: false }));

// parse application/json
app.use(express.json());

//Xml parser
app.use(xmlparser());

let data;

app.post("/receive-json", (req, res) => {
    console.log("json received: ", req.body.data)
    res.send({ "Here is your new data ": req.body.data * 3 });
});

//listens for a port number
app.listen(port, error => {
    console.log("Error: ", error);
    if (error) {
        console.log("Error running the server", error);
    }
    console.log("Server is running on port", port)
});