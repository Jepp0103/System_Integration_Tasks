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
    dataNumber = (req.body.data * 2).toString();

    axios.post('http://127.0.0.1:3333/receive-json', {
        data: dataNumber
    })
        .then(function (response) {
            console.log(response.data);
            res.send(response.data);
        })
        .catch(function (error) {
            console.log(error)
        })
});


//listens for a port number
app.listen(port, error => {
    if (error) {
        console.log("Error running the server", error);
    }
    console.log("Server is running on port", port)
});