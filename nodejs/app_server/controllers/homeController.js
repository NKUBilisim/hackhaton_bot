// Modules loaded
var app = require('express');
var ejsLayouts = require('express-ejs-layouts');

module.exports.homeController = function(req,res){
    res.render('index');
}