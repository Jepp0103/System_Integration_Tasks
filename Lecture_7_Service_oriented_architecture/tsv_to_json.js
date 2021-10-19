const axios = require('axios');

const endpoint = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYbybiVenyLTJ39ysmw36TfyJWU8p9UK72f81LJ_eIo6vwsV9va_aWETMCgl8EXOefIzTRABU7DqRZ/pub?output=tsv";

axios.get(endpoint)
    .then(function (response) {
        console.log("TSV:")
        console.log(response.data);

        console.log("JSON:")
        console.log(tsvToJson(response.data));
    })
    .catch(function (error) {
        console.log(error)
    });

function tsvToJson(tsv) {
    const [headers, ...rows] = tsv.trim().split('\n').map(r => r.split('\t'))
    jsonData = JSON.stringify(rows.reduce((a, r) => [
        ...a,
        Object.assign(... (r.map(
            (x, i, _, c = x.trim()) => ({ [headers[i].trim()]: isNaN(c) ? c : Number(c) })
        )))
    ], []));

    return jsonData
}