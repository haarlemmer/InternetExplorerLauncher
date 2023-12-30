# Internet Explorer Launcher

Bypass "Internet Explorer 11 is No Longer Supported" and launch it to use websites that requires it.
绕过 “不再支持 Internet Explorer 11”，强制启动 IE11 以使用依赖于 IE 的网站

针对 Windows 10  22H2 版本中，Internet Explorer 11 在卸载 Microsoft Edge 后，依旧无法启动，提示 “不再支持 Internet Explorer 11” 的折中解决方案

## Usage
```cmd
iexplorerLauncher-console.exe [URL]
```
若URL未指定，则使用`about:blank`作为缺省值

**注意: 由于启动 Internet Explorer 11 需要添加 `-Embedded` 参数，而由于Internet Explorer 11 的离谱 Bug，`-Embedded` 会成为URL的一部分，为了避免对目标文件或query部分的影响，程序会在URL后加上 `?nope=` 或 `&nope=`**

## 设置为默认浏览器以使用需要调用作为默认浏览器的 IE 的应用
Internet Explorer 11 被作为默认浏览器调用时依旧拒绝启动，可以将此程序设置为默认浏览器，便可以间接启动 IE。

### 作为浏览器注册到 Windows
将程序放置于 `C:\InternetExplorerLauncher\` 下，则可执行位置应为 `C:\InternetExplorerLauncher\iexploreLauncher.exe`，然后加载注册表文件 `RegisterAsABrowser.reg`，前往Windows设置 - 应用 - 默认应用，将浏览器改为 `Internet Explorer Launcher` 即可

### 移除浏览器注册
若要移除此浏览器注册，删除以下注册表项(文件夹):
```
HKEY_CURRENT_USER\Software\Clients\StartMenuInternet\iexploreLauncher\
HKEY_CURRENT_USER\Software\Classes\InternetExplorerLauncher
```
删除以下注册表键：
```
HKEY_CURRENT_USER\Software\RegisteredApplications\Internet Explorer Launcher
```
