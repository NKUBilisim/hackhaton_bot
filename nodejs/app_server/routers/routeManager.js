var routers = require('./homeRouters');

module.exports = function(app){
    // Comissioned for the '/' request
    app.use('/', routers);
}