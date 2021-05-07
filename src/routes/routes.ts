import { monitor } from "@colyseus/monitor";
import {Application, Request, Response, NextFunction} from  'express';
/*const debug = require("../common/consoleOutputs")
const log = function(arguments) {
    debug.changeDebugCtx("ws");
    console.log(arguments)
}
*/

export class Routes {
    constructor(app :Application) {
    
        /* ROUTES */
        // Main web page

        Routes.get(app, '/','index.ejs', {} )
        Routes.get(app, '/blog','blog.ejs', {params:{pageName:"Blog", bg:"img/page-top-bg/3.jpg",breadcrumb:{name:"Home", url:"/",breadcrumb:{name:"Blog", url:"" } }}} )
        Routes.get(app, '/contact','contact.ejs', {params:{pageName:"Contact", bg:"img/page-top-bg/4.jpg",breadcrumb:{name:"Home",url:"/",breadcrumb:{name:"Contact", url:"" } }}})
        Routes.get(app, '/reviews','reviews.ejs', {params:{pageName:"Reviews", bg:"img/page-top-bg/2.jpg",breadcrumb:{name:"Home",url:"/",breadcrumb:{name:"Reviews", url:"" } }}})
        Routes.get(app, '/games','games.ejs', {params:{pageName:"Games", bg:"img/page-top-bg/1.jpg",breadcrumb:{name:"Home",url:"/",breadcrumb:{name:"Games", url:"" } }}})
        Routes.get(app, '/game-single','game-single.ejs', {params:{pageName:"Games", bg:"img/page-top-bg/1.jpg",breadcrumb:{name:"Home",url:"/",breadcrumb:{name:"Games", url:"/games",breadcrumb:{name:"Game", url:"" } } }}})
        Routes.get(app, '/pathbuilder','pathbuilder.ejs', {} )
        Routes.get(app, '/pb','pathbuilder.ejs', {} )
        
      

        app.get("/kick", (req :Request, res :Response) => {
            res.send("It's time to kick ass and chew bubblegum!");
        });

        app.get('/race', function(req:Request, res:Response) {
            res.render('pages/ClientPage_AuthoritativeServer', { user:"me"});
            console.log('app.get : \/race_pos');
        });



        /**
         * Bind @colyseus/monitor
         * It is recommended to protect this route with a password.
         * Read more: https://docs.colyseus.io/tools/monitor/
         */
        app.use("/colyseus", monitor());
    
        };

        static get(app : Application,pageName:string, pageUrl:string ,  param : Object){
            app.get(pageName, function(req:Request, res:Response) {
                res.render(pageUrl, param);
                console.log('app.get : \/' + pageUrl + ' with :'  );
                console.log(param)
            });
        }
}