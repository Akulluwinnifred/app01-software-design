"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Hp = exports.Lenovo = exports.IBM = exports.Dell = void 0;
var Dell = /** @class */ (function () {
    function Dell() {
    }
    Dell.prototype.setBrand = function () {
        return "Keyboard input";
    };
    Dell.prototype.boot = function () {
        console.log("Dell  booting...");
    };
    return Dell;
}());
exports.Dell = Dell;
var IBM = /** @class */ (function () {
    function IBM() {
    }
    IBM.prototype.setBrand = function () {
        return "Brand: IBM";
    };
    IBM.prototype.boot = function () {
        console.log("IBM  booting...");
    };
    return IBM;
}());
exports.IBM = IBM;
var Lenovo = /** @class */ (function () {
    function Lenovo() {
    }
    Lenovo.prototype.setBrand = function () {
        return "Brand: Lenovo";
    };
    Lenovo.prototype.boot = function () {
        console.log("Lenovo  booting...");
    };
    return Lenovo;
}());
exports.Lenovo = Lenovo;
var Hp = /** @class */ (function () {
    function Hp() {
    }
    Hp.prototype.setBrand = function () {
        return "Brand: Hp";
    };
    Hp.prototype.boot = function () {
        console.log("HP  booting...");
    };
    return Hp;
}());
exports.Hp = Hp;
