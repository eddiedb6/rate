{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
        {
            AFWConst.Name: "Browser",
            AFWConst.Type: AFWConst.UIWeb,
            AFWConst.Plugin: {
                AFWConst.PluginName: AFWConst.PluginSelenium
            },
            AFWConst.Browser: AFWConst.BrowserFireFox,
            AFWConst.SubUI: [
            {
                AFWConst.Name: "URLRate",
                AFWConst.Type: AFWConst.WebURL,
                AFWConst.URL: "http://www.boc.cn/sourcedb/whpj",
                AFWConst.BreakTime: 10000 # Give time for proxy setting
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
