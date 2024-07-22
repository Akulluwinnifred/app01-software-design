// Static class and methods
// Private constructor
var IAMlogger = /** @class */ (function () {
    // Constructor
    function IAMlogger(username, password) {
        IAMlogger.username = username;
        IAMlogger.password = password;
    }
    // methods
    IAMlogger.login = function (username, password) {
        // Limit the number of objects to 1
        if (IAMlogger.singletonUser == null) {
            IAMlogger.singletonUser = new IAMlogger(username, password);
        }
        return IAMlogger.singletonUser;
    };
    IAMlogger.logout = function () {
        IAMlogger.singletonUser = null;
        console.log("You have successfully logged out");
        console.log("");
    };
    // Global access to the singleton instance
    IAMlogger.getUser = function () { return { username: IAMlogger.username, password: IAMlogger.password }; };
    return IAMlogger;
}());
IAMlogger.login("Jovita", "pswdkanza");
console.log(IAMlogger.getUser());
IAMlogger.logout();
IAMlogger.login("Phillip", "pswdbaguma");
console.log(IAMlogger.getUser());
IAMlogger.logout();
IAMlogger.login("atim", "pswdwinnie");
console.log(IAMlogger.getUser());
IAMlogger.logout();
IAMlogger.login("valentine", "pswdkiguli");
console.log(IAMlogger.getUser());
