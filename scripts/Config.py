{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
        {
            AFWConst.Name: "Browser",
            AFWConst.Type: AFWConst.UIWeb,
            AFWConst.Plugin: {
                #AFWConst.PluginName: AFWConst.PluginSelenium
                AFWConst.PluginName: AFWConst.PluginProxyWeb,
                AFWConst.Proxy: {
                    AFWConst.ProxyType: AFWConst.ProxyLocal,
                    AFWConst.ProxyLauncher: "python",
                    AFWConst.PluginName: "PluginSelenium"
                }
            },
            AFWConst.Browser: AFWConst.BrowserFireFox,
            AFWConst.SubUI: [
            {
                AFWConst.Name: "URLRate",
                AFWConst.Type: AFWConst.WebURL,
                AFWConst.URL: "http://www.boc.cn/sourcedb/whpj",
                AFWConst.BreakTime: 1000
            },
                ImportFile("ConfigRateSearch.py")
            ]
        }]
    },

    AFWConst.Action: {
        AFWConst.SubAction: [
        {
            AFWConst.Script: "Script.py"
        }]
    }
}
