import mongoose from 'mongoose';
import { createSchema, Type, typedModel } from 'ts-mongoose';
const Schema = mongoose.Schema;

var pageSchema = createSchema({
    pagename : String,
    background : String,
    url: String, 
    parentPage :  {type:Schema.Types.ObjectId, ref: 'Page'} 
})
export var Page = mongoose.model('Page', pageSchema)

var definedTagsSchema = createSchema({
    title: String, 
    description: String
})
export var DefinedTags = mongoose.model('DefinedTags', definedTagsSchema)

var blogArticleSchema = createSchema({
    title: String, 
    preview: String, 
    image : String, 
    text: String, 
    publication : Date, 
    modification : Date, 
    author: String,
    tags: [String],
    comments: [{
        user: String,
        content: String,
        votes: Number
    }]
})
export var BlogArticle = mongoose.model('Blog', blogArticleSchema)

export async function getPageInfo(pageName: string){
    let Page  = typedModel('Page', pageSchema)
     var page = (await Page.findOne({ pagename: pageName })) ;
    console.log(page)
    if (page.parentPage != null)
    {
        console.log(page.parentPage)
    }

}

