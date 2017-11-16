// Modules loaded
var express = require('express');
var ejsLayouts = require('express-ejs-layouts');
var routers = express.Router();
var homeController = require('../controllers/homeController');

// Routing was made
routers.get('/',fucntion(req,res){
    res.render('index');    
});
// Routers was exported
module.exports = routers;