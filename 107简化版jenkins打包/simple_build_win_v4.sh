#!/bin/bash
gradle_properties_file=./gradle.properties
file_to_delete=app/src/main/assets/ConfigVigame.xml
rm "$file_to_delete"
echo "#----simple_build.sh---" >> "$gradle_properties_file"
#清理原本文件中包含模块的默认属性
sed -i "/OBS=/d" "$gradle_properties_file"
sed -i "/ArtOBS=/d" "$gradle_properties_file"
sed -i "/stringEncrypt=/d" "$gradle_properties_file"
sed -i "/isAdObs=/d" "$gradle_properties_file"
sed -i "/replaceAccountName=/d" "$gradle_properties_file"
sed -i "/aloneAbi64=/d" "$gradle_properties_file"

#重新给属性赋值
echo "OBS=$OBS" >> "$gradle_properties_file"
echo "ArtOBS=$ArtOBS" >> "$gradle_properties_file"
echo "stringEncrypt=$stringEncrypt" >> "$gradle_properties_file"
echo "isAdObs=$isAdObs" >> "$gradle_properties_file"
echo "replaceAccountName=$replaceAccountName" >> "$gradle_properties_file"
echo "aloneAbi64=$aloneAbi64" >> "$gradle_properties_file"


##测试代码,正式使用需要注释掉
#channel="white"
#LIBS_NG_MD="ng_weatherCore,ng_news,ng_hot_dex,ng_tencen_weixin"
#LIBS_AD_MD="wb_ad_baidu"
##测试代码end

#其他一些属性
support_oppo="false"
isXQD="false"
isWhiteWrap="false"

if [[ $channel == "white" ]]; then
    #白包渠道,扩展库可以都不带
    isWhiteWrap="true"
    #默认白包都不带扩展模块
    LIBS_NG_BASE=""
    LIBS_AD_ALL=""
    LIBS_TRACK=""
    LIBS_TJ=""
    LIBS_NG_OTHER=""
else
    #非白包的默认配置
    isWhiteWrap="false"
    LIBS_NG_BASE=$LIBS_NG_MD  #外部参数传入
    LIBS_AD_ALL=$LIBS_AD_MD
    LIBS_TRACK=""
    LIBS_TJ=""
    #其他模块,
    LIBS_NG_OTHER=",ng_platform2,ng_open_prpr,ng_open_scenes,ng_open_launcher"
fi


#商店渠道主要是bh相关库携带不一样,这里先只区分bh相关库
if [[ $channel == "vivo" ]]; then
    #viyy 渠道: d模自启, 秒拉, 置灰拉活,vivo弹出
    LIBS_NG_BH=",ng_dddipml,dd_dcore,dd_c_instr,dd_account,dd_dk"
elif [[ $channel == "oppo" ]]; then
    #opyy渠道
    #ovstore_v1.0.8.1分支开始,所有渠道不再携带app_pin模块, 此处脚本为了兼容以前的分支,所以未去除, 实际1081后的分支modules模块中已去除此模块
    LIBS_NG_BH=",ng_dddipml,dd_dcore,dd_c_instr,dd_account,dd_dk,app_pin"
    support_oppo="true"
elif [[ $channel == "csj" ]]; then
    #兜底渠道
    #ovstore_v1.0.8.1分支开始,所有渠道不再携带app_pin模块, 此处脚本为了兼容以前的分支,所以未去除, 实际1081后的分支modules模块中已去除此模块
    LIBS_NG_BH=",ng_dddipml,dd_dcore,dd_c_instr,dd_dk,dd_account,dd_c_op_kg,app_pin"
    support_oppo="true"
elif [[ $channel == "xiaomi" ]]; then
    #小米
    LIBS_NG_BH=",ng_dddipml"
elif [[ $channel == "huawei" ]]; then
    #华为
    LIBS_NG_BH=",ng_dddipml,dd_dk"
elif [[ $channel == "honor" ]]; then
    #荣耀
    LIBS_NG_BH=",ng_dddipml,dd_account,dd_dk"
elif [[ $channel == "xqd" ]]; then
    #xqd包, 可以不用bh
    LIBS_NG_BH=""
    isXQD="true"
    LIBS_NG_OTHER=",ng_platform2"
elif [[ $channel == "iaa" ]]; then
    #内广渠道,bh
    LIBS_NG_BH=""
    LIBS_NG_OTHER=",ng_platform2"
fi

LIBS_NG_ALL="$LIBS_NG_BASE$LIBS_NG_OTHER$LIBS_NG_BH"




#清理原本文件中包含模块的默认属性
sed -i "/isWhiteWrap=/d" "$gradle_properties_file"
sed -i "/LIBS_NG=/d" "$gradle_properties_file"
sed -i "/LIBS_TRACK=/d" "$gradle_properties_file"
sed -i "/LIBS_AD=/d" "$gradle_properties_file" #
sed -i "/LIBS_TJ=/d" "$gradle_properties_file"
sed -i "/support_oppo=/d" "$gradle_properties_file"
sed -i "/isXQD=/d" "$gradle_properties_file"

#重新给属性赋值
echo "isWhiteWrap=$isWhiteWrap" >> "$gradle_properties_file"
echo "LIBS_NG=$LIBS_NG_ALL" >> "$gradle_properties_file"
echo "LIBS_TRACK=$LIBS_TRACK" >> "$gradle_properties_file"
echo "LIBS_AD=$LIBS_AD_ALL" >> "$gradle_properties_file"
echo "LIBS_TJ=$LIBS_TJ" >> "$gradle_properties_file"
echo "support_oppo=$support_oppo" >> "$gradle_properties_file"
echo "isXQD=$isXQD" >> "$gradle_properties_file"

