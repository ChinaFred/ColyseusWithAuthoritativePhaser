import {Page, DefinedTags, BlogArticle } from "./pageContent";
import mongoose from 'mongoose';
const Schema = mongoose.Schema;

export async  function InitPagesData(){
   await feedPages()
   //await feedPageHierarchy()
   await feedSomeBlogArticles()
}

 

 async function feedPages(){
   var IndexPage = new Page({
       pagename : "Index",
       background : "img/page-top-bg/3.jpg",
       url : "/", 
       parentPage : null
   });
   await IndexPage.save();
   var BlogPage = new Page({
       pagename : "Blog",
       background : "img/page-top-bg/3.jpg",
       url : "/blog",
       parentPage : await Page.findOne({ pagename:"Index" })
   });
   await BlogPage.save();
   var ContactPage = new Page({
       pagename : "Contact",
       background : "img/page-top-bg/4.jpg",
       url : "/contact",
       parentPage : await Page.findOne({ pagename:"Index" })
   });
   await ContactPage.save();
   var ReviewsPage = new Page({
       pagename : "Reviews",
       background : "img/page-top-bg/2.jpg",
       url : "/reviews",
       parentPage : await Page.findOne({ pagename:"Index" })
   });
   await ReviewsPage.save();
   var gamesPage = new Page({
       pagename : "Games",
       background : "img/page-top-bg/1.jpg",
       url : "/games",
       parentPage : await Page.findOne({ pagename:"Index" })
   });
   await gamesPage.save();
   var gamePage = new Page({
       pagename : "Game",
       background : "img/page-top-bg/1.jpg",
       url : "/game",
       parentPage : await Page.findOne({ pagename:"Games" })
   });
   await gamePage.save();
 
}

/*
async function feedPageHierarchy(){
   var IndexHierarchy = new PageHierarchy({
      pagename : await Page.findOne({ name:"Index" }),
      parentPage :null
   })
   IndexHierarchy.save()
   var BlogHierarchy = new PageHierarchy({
      pagename : await  Page.findOne({ name:"Blog" }),
      parentPage :await  Page.findOne({ name:"Index" })
   })
   BlogHierarchy.save()
   var ContactHierarchy = new PageHierarchy({
      pagename : await  Page.findOne({ name:"Contact" }),
      parentPage :await Page.findOne({ name:"Index" })
   })
   ContactHierarchy.save()
   var ReviewsHierarchy = new PageHierarchy({
      pagename : await Page.findOne({ name:"Reviews" }),
      parentPage :await Page.findOne({ name:"Index" })
   })
   ReviewsHierarchy.save()
   var GamesHierarchy = new PageHierarchy({
      pagename :await  Page.findOne({ name:"Games" }),
      parentPage :await Page.findOne({ name:"Index" })
   })
   GamesHierarchy.save()
   var GameHierarchy = new PageHierarchy({
      pagename : await Page.findOne({ name:"Game" }),
      parentPage :await Page.findOne({ name:"Games" })
   })
   GameHierarchy.save()

}
*/


async  function feedSomeBlogArticles(){
   var article1 = new BlogArticle({
       title : "The best VR games on the market",
       image: "/img/blog-big/1.jpg", 
       preview : "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore mag....." ,
       text :  "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....",
       publication : new Date(), 
       modification : null,
       author : "Kassbinette",
       tags :"Racing, Gaming", 
       comments: [
           {
           user: "Tommy Tom",
           content : "Houlala what a great article", 
           votes : 8}, 
           {
               user: "Lolly Jack ",
               content : "What are you talking about? ", 
               votes : 1}, 
       ]
   })
   var article2 = new BlogArticle({
       title : "The best online game is out now!",
       image: "/img/blog-big/2.jpg", 
       preview : "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore mag....." ,
       text :  "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.....",
       publication : new Date(), 
       modification : null,
       author : "JJay",
       tags :"Racing, Gaming", 
       comments: [
           {
           user: "Tommy Tom",
           content : "Houlala what a great article", 
           votes : 8}, 
           {
               user: "Lolly Jack ",
               content : "What are you talking about? ", 
               votes : 1}, 
       ]
   })
   
   // Insert the article in our MongoDB database
   article1.save();
   article2.save();
   
   BlogArticle.findOne({}, (err:Object,post:Object)=>{
       console.log(post);
   })
}
