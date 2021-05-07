import Arena from "@colyseus/arena";
import { monitor } from "@colyseus/monitor";
import {Routes } from './routes/routes'
import express from  'express';
require("./tools/consoleOutputs")
import mongoose from 'mongoose';
//import {InitPagesData} from "./logic/websiteContent/initWebSite"
import {getPageInfo} from "./logic/websiteContent/pageContent"


/**
 * Import your Room files
 */
import { MyRoom } from "./rooms/MyRoom";

export default Arena({
    getId: () => "Your Colyseus App",

    initializeGameServer: (gameServer) => {
        /**
         * Define your room handlers:
         */
        gameServer.define('my_room', MyRoom);

    },

    initializeExpress: (app) => {

        global.baseDirectory = require('path').resolve(__dirname, '..')
         // definition of the path of the views
        app.set('views', __dirname + '/views');
        // templating system
        app.set('view engine', 'ejs');
        // path to statics (pictures, scripts , css)
        app.use(express.static(global.baseDirectory + '/src/public'));
        // pathes to modules used for front-end and managed through NPM
        app.use('/font-awesome', express.static(global.baseDirectory + '/node_modules/font-awesome'));
        app.use('/bootstrap', express.static(global.baseDirectory + '/node_modules/bootstrap/dist/'));
        app.use('/jquery', express.static(global.baseDirectory + '/node_modules/jquery/dist/'));
        app.use('/moment', express.static(global.baseDirectory + '/node_modules/moment/min/'));
        app.use('/jquery-ui', express.static(global.baseDirectory + '/node_modules/jquery-ui-dist/'));
        app.use('/bootstrap-input-spinner', express.static(global.baseDirectory + '/node_modules/bootstrap-input-spinner/src'));
        app.use('/bootstrap-table', express.static(global.baseDirectory + '/node_modules/bootstrap-table/dist'));
        app.use('/phaser', express.static(global.baseDirectory + '/node_modules/phaser/dist'));
        app.use('/pathBuilder', express.static(global.baseDirectory + '/node_modules/phaser3-plugin-pathbuilder/dist'));
        app.use('/colyseus.js', express.static(global.baseDirectory + '/node_modules/colyseus.js/dist'));
        app.use('/path2d-polyfill.js', express.static(global.baseDirectory + '/node_modules/path2d-polyfill/src'));
        app.use('/animate.css',express.static(global.baseDirectory + '/node_modules/animate.css'))
        app.use('/magnific-popup',express.static(global.baseDirectory + '/node_modules/magnific-popup/dist'))
        app.use('/owl.carousel',express.static(global.baseDirectory + '/node_modules/owl.carousel/dist'))
        app.use('/slicknav',express.static(global.baseDirectory + '/node_modules/slicknav/dist'))
        app.use('/sticky-sidebar',express.static(global.baseDirectory + '/node_modules/sticky-sidebar/dist'))
        
        mongoose.connect('mongodb://127.0.0.1:27017/local', {
            useNewUrlParser: true,
            useUnifiedTopology: true,
            useFindAndModify: false,
            useCreateIndex: true
          });
                
           

        
        /**
         * Bind your custom express routes here:
         */
        new Routes(app)
    },


    beforeListen: () => {
        /**
         * Before before gameServer.listen() is called.
         */
    }
});