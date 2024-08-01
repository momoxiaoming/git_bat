Java.perform(function x() {

    Java.use('android.app.Activity').onCreate.overload("android.os.Bundle").implementation = function (bundle) {
        this.onCreate(bundle)
        console.log("开启一个activit->" + this)
    }
    //
    // Java.use('com.starbaba.stepaward.module.aboutus.AboutusActivity').onResume.implementation = function () {
    //     this.onResume()
    //
    //     console.log("onResume------")
    //     try {
    //         // 启动 TestActivity
    //         var Intent = Java.use('android.content.Intent');
    //         var currentActivity = Java.cast(this, Java.use('android.app.Activity'));
    //         var context = currentActivity.getApplicationContext();
    //         var targetClass = Java.use('java.lang.Class').forName('com.xm.ark.debugtools.DebugToolPageActivity');
    //         var intent = Intent.$new.overload('android.content.Context', 'java.lang.Class').call(this, targetClass);
    //         this.startActivity(intent);
    //         console.log("startActivity------")
    //     }catch(err){
    // 		console.log(err);
    // 		return;
    // 	}
    //
    // };

    Java.use('com.starbaba.stepaward.business.appInfo.AppInfoActivity').oo0oOO0O.implementation = function () {
        console.log("AppInfoActivity-----密码验证通过:" + this.o0Oo00o0.value)

        return true
    }

    //    public static void o0oo0o0O(String str, String str2, String str3) {
    //
    Java.use('com.starbaba.stepaward.base.utils.o0oo0OO0').o0oo0o0O.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function (x, y, z) {

        console.log("log文件 x:" + x)
        console.log("log文件 y:" + y)
        console.log("log文件 z:" + z)

        return this.o0oo0o0O(x, y, z)
    }

    Java.use('com.starbaba.stepaward.base.utils.o0oo0OO0').oO0Oo0Oo.overload('java.io.File', 'java.lang.String', 'java.lang.String').implementation = function (x, y, z) {
        console.log("文件路径:" + x.getPath())
        return this.oO0Oo0Oo(x, y, z)
    }
    // Java.use('com.starbaba.stepaward.module.lauch.LaunchAdActivity$o0OOOoO').o0OOOoO.implementation = function (x) {
    //     console.log("审核开关:" + x)
    //     return this.o0OOOoO(false)
    // }
    // Java.use('com.starbaba.stepaward.module.lauch.LaunchAdActivity$o0OOOoO').onFailure.overload('java.lang.String', 'java.lang.String').implementation = function (x, y) {
    //     console.log("onFailure:" + x)
    //     return this.onFailure(x, y)
    // }
    // Java.use('com.starbaba.stepaward.module.lauch.LaunchAdActivity$o0OOOoO').onSuccess.overload('java.lang.Object').implementation = function (x) {
    //     console.log("onSuccess:" + x)
    //     return this.onSuccess(x)
    // }


    // Java.use('com.xmiles.step_xmiles.oOoOO0oO').o0OOOoO.implementation = function (x) {
    //     var rlt=this.o0OOOoO(x)
    //     console.log("解密:" + x+" --> "+rlt)
    //     return rlt
    // }
    // Java.use('com.starbaba.stepaward.module.lauch.LaunchAdActivity').OOO000.implementation = function (x) {
    //     console.log("OOO000:" + x)
    //     return this.OOO000(x)
    // }

    Java.use('nh').o0OooO0.overload().implementation = function () {
        console.log("强制审核状态为false:")
        return false
    }

    Java.use('nh').o0oo0o0O.overload().implementation = function () {
        console.log("强制自然量状态为false:")
        return false
    }

    //
    // Java.use('com.xmiles.tool.network.volley.oO0Oo0Oo').o0OOOoO.implementation = function (x, y) {
    //
    //     console.log("1--->" + x.o0OOOoO())
    //     console.log("2--->" + x.OO0O00O())
    //     console.log("3--->" + x.o0oo0o0O())
    //     var rlt = this.o0OOOoO(x, y)
    //     return rlt
    //
    // }
    // Java.use('com.xmiles.tool.network.volley.oO0Oo0Oo').oOOo0OO0.implementation = function (x, y) {
    //     console.log("响应--->" + y.toString())
    //     var rlt = this.oOOo0OO0(x, y)
    //     return rlt
    // }
    //
    // Java.use('com.xmiles.tool.network.volley.oO0Oo0Oo').o00oOOOO.implementation = function (x, y) {
    //     console.log("响应--->" + y.data.value)
    //     console.log("响应--->" + x.class)
    //
    //     var rlt = this.o00oOOOO(x, y)
    //     return rlt
    // }
    // Java.use('m2').oOooOoO.implementation = function (x) {
    //     console.log("响应--->" + x.class)
    //     var rlt = this.oOooOoO(x)
    //     return rlt
    // }
    // Java.use('l2').o0oo0o0O.implementation = function (x) {
    //     console.log("响应2--->" + x.class)
    //     var rlt = this.o0oo0o0O(x)
    //     return rlt
    // }
    //
    // Java.use('com.xmiles.tool.network.oOoOO0oO').o0OooO0.implementation = function (x) {
    //     console.log("参数--->" + x)
    //     var rlt = this.o0OooO0(x)
    //     console.log("结果--->" + rlt)
    //
    //     return rlt
    // }

    // Java.use('com.xmiles.tool.network.oOoOO0oO').OO0O00O.implementation = function (x) {
    //     var rlt = this.OO0O00O(x)
    //     console.log("结果--->" + rlt.toString())
    //     return rlt
    // }


    Java.use('do.do.do.do.this').o00oOo00.implementation = function (x1, x2, x3, x4) {
        var rlt = this.o00oOo00(x1, x2, x3, x4)
        console.log("结果--->" + x4)
        return rlt
    }

    Java.use('com.rn.io.utils.o0OooO0').o0OOOoO.implementation = function (x1) {
        var rlt = this.o0OOOoO(x1)
        console.log("强制本地检测:false")
        return false
    }
});

