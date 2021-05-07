//https://tslog.js.org/#/?id=api-documentation
import { Logger } from "tslog";

const log: Logger = new Logger(
    { name: "console", 
    overwriteConsole: true 
    //,    exposeStack: true
});

