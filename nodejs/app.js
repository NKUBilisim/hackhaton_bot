

// Modules loaded
const fs = require('fs');
const express = require('express');
const path = require('path');
var app = express();

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file
app.set('views', path.join(__dirname, 'app_server/views'));

// index page 
app.get('/', function(req, res) {
    var sLn = req.query.sLn;
    var sLt = req.query.sLt;
    var fLn = req.query.fLn;
    var fLt = req.query.fLt;
    
    res.render('index', {
        data: sLn
    });
});

app.listen(8088);
console.log('8088 is the magic port');