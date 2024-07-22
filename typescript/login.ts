// Static class and methods
// Private constructor

class IAMlogger{

    // Data variables
    private static singletonUser;
    private  static username: string;
    private  static password: string;

    // Constructor
    private constructor(username: string, password: string){
        IAMlogger.username = username;
        IAMlogger.password = password;
    }

    // methods
    public static login(username: string, password: string){

        // Limit the number of objects to 1
        if(IAMlogger.singletonUser == null){
            IAMlogger.singletonUser = new IAMlogger(username, password);
        }

        return IAMlogger.singletonUser;
    }

    public static logout(){
        IAMlogger.singletonUser = null
        console.log("You have successfully logged out");
        console.log("");
        
    }

    // Global access to the singleton instance
    public static getUser(){ return {username: IAMlogger.username, password: IAMlogger.password}; }


}


IAMlogger.login("Jovita", "pswdkanza")
console.log(IAMlogger.getUser());
IAMlogger.logout();


IAMlogger.login("Phillip", "pswdbaguma")
console.log(IAMlogger.getUser());
IAMlogger.logout();

IAMlogger.login("atim", "pswdwinnie")
console.log(IAMlogger.getUser());
IAMlogger.logout();


IAMlogger.login("valentine", "pswdkiguli")
console.log(IAMlogger.getUser());



















