//Creating the server
const express = require("express");
const app = express();
var xmlparser = require('express-xml-bodyparser');
const csv = require('csv');
const axios = require('axios');
const port = 2222;

// parse application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: false }));

// parse application/json
app.use(express.json());

//Xml parser
app.use(xmlparser());

let dataNumber;

app.post("/receive-xml", (req, res) => {
    console.log("xml data: ", req.body.data);
    dataNumber = parseInt(req.body.data * 2);

    axios.post('http://localhost:3333/receive-json', {
        data: dataNumber
    })
        .then(function (response) {
            console.log(response.data);
            res.send({ "Data sent: ": dataNumber });
        })
        .catch(function (error) {
            console.log(error)
        })
});

app.post("/receive-csv", (req, res) => {
    console.log("Csv data: ", req.body)
});

//listens for a port number
app.listen(port, error => {
    console.log("Error: ", error);
    if (error) {
        console.log("Error running the server", error);
    }
    console.log("Server is running on port", port)
});