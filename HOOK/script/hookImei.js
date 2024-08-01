Java.perform(function x() {

    //监测到检测到mac地址获取
    Java.use("android.net.wifi.WifiInfo").getMacAddress.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('监测到检测到mac地址获取')));
        return this.getMacAddress();
    };
    //测到硬件HardwareAddress地址
    Java.use("java.net.NetworkInterface").getHardwareAddress.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到硬件HardwareAddress地址获取')));
        return this.getHardwareAddress();
    };

    //检测到硬件InetAddresses地址
    Java.use("java.net.NetworkInterface").getInetAddresses.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到硬件InetAddresses地址获取')));
        return this.getInetAddresses();
    };

    //检测到网络SSID获取
    Java.use("android.net.wifi.WifiManager").getConnectionInfo.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到网络SSID获取')));
        return this.getConnectionInfo();
    };

    //检测到网络列表获取
    Java.use("android.net.wifi.WifiManager").getScanResults.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到网络列表获取')));
        return this.getScanResults();
    };

    //检测到网络列表获取
    Java.use("android.telephony.TelephonyManager").getDeviceId.overload().implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到IMEI获取')));
        return this.getDeviceId();
    };

    //检测读取应用安装列表
    // Java.use("android.content.pm.PackageManager").getInstalledPackages.overload('int').implementation = function (x) {
    //     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测读取应用安装列表')));
    //     return this.getInstalledPackages(x);
    // };


    //检测到andId获取
    Java.use("android.provider.Settings$Secure").getString.implementation = function (x, y) {
        if (y === 'android_id') {
            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到andId获取')));
        }
        return this.getString(x, y);
    };

    //检测到系统账户权限获取
    Java.use("android.accounts.AccountManager").getAccountsByType.implementation = function (x) {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到系统账户权限获取')));
        return this.getAccountsByType(x);
    };
    //检测到监听呼入电话信息
    Java.use("android.telephony.TelephonyManager").listen.implementation = function (x, y) {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到监听呼入电话信息')));
        return this.listen(x, y);
    };
    //检测到去电信息
    Java.use("android.telephony.TelephonyManager").getCallState.overload().implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测到去电信息')));
        return this.getCallState();
    };

    //sd卡信息
    Java.use("android.os.Environment").getExternalStorageState.overload().implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('sd卡信息')));
        return this.getExternalStorageState();
    };

    //sd卡信息2
    Java.use("android.os.Environment").getExternalStorageDirectory.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('sd卡信息2')));
        return this.getExternalStorageDirectory();
    };

    //ip地址获取
    Java.use("android.net.wifi.WifiInfo").getIpAddress.implementation = function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('ip地址获取')));
        return this.getIpAddress();
    };

    // Java.choose("com.mc.gates.gates_scenes.ui.MainActivity", {
    //     onMatch: function (instance) { //该类有多少个实例，该回调就会被触发多少次
    //         instance.getPackageManager.implementation = function () {
    //             console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测读取应用安装列表')));
    //             return this.getPackageManager();
    //         };
    //     },
    //     onComplete: function () {
    //     }
    // });

    var app = Java.use('android.app.ActivityThread').currentApplication();
    var packManager = app.getPackageManager();
    packManager.getInstalledPackages.overload('int').implementation = function (x) {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new('检测读取应用安装列表')));
        return getInstalledPackages(x)
    }
    // var PackageManager = Java.use('android.content.pm.PackageManager');
    //
    // PackageManager.getInstalledPackages.overload('int').implementation = function (flags) {
    //     console.log('Hooked getInstalledPackages()');
    //     return this.getInstalledPackages(flags);
    // };
});

