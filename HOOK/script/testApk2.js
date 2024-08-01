Java.perform(function x() {

    // Java.use('xxx.a.activity.detail.AboutActivity').onCreate.overload("android.os.Bundle").implementation = function (bundle) {
    //     this.onCreate(bundle)
    //     console.log("--->" + bundle)
    // }

    Java.use('com.tramini.plugin.a.h.b').a.overload("com.tramini.plugin.b.b").implementation = function (e) {
        e.o.value = 1
        console.log("dddd -->" + e.i())
        console.log("dddd -->" + e.f())
        console.log("dddd -->" + e.o.value)
        return this.a(e)
    }
    Java.use('com.tramini.plugin.b.b').b.overload().implementation = function () {
        return 1
    }
    Java.use('com.adjust.sdk.Adjust').onCreate.implementation = function (e) {
        console.log("adjust 初始化")
        return this.onCreate(e)
    }
    Java.use('android.app.Activity').onCreate.overload("android.os.Bundle").implementation = function (bundle) {
        this.onCreate(bundle)
        console.log("开启一个activit->" + this)
    }
    Java.use('com.adjust.sdk.Adjust').getAttribution.implementation = function () {

        var attr = this.getAttribution()
        attr.network.value = "adjust:click"
        console.log("adjust 归因" + attr.network.value)
        return attr
    }

    Java.use('com.chartboost.heliumsdk.impl').getAttribution.implementation = function () {

        var attr = this.getAttribution()
        attr.network.value = "adjust:click"
        console.log("adjust 归因" + attr.network.value)
        return attr
    }
});

