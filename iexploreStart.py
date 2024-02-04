#    Internet Explorer Launcher for Windows 10 22H2 or larer version that can't launch it directly.
#    Copyright (C) 2024 Jiangbo Liu
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sys, re, os

def getIexploreStartCmd(iexplorePath, url):
    startCmd = f'"{iexplorePath}" '
    haveQuery = urlHaveQuery(url)
    if haveQuery:
        if urlHaveAnd(url=url):
            url = urlReplaceAnd(url)
        startCmd = startCmd + f'{url}^&nope= -Embedding'
    else:
        startCmd = startCmd + f'{url}?nope= -Embedding'
    return startCmd

def urlHaveQuery(url):
    chkRegex = re.compile(r"\?")
    chkRet = chkRegex.findall(url)
    chkResult = False
    if '?' in chkRet:
        chkResult = True
    return chkResult

def urlHaveAnd(url):
    chkRegex = re.compile(r"&")
    chkRet = chkRegex.findall(url)
    chkResult = False
    if '&' in chkRet:
        chkResult = True
    return chkResult

def urlReplaceAnd(url):
    chkRegex = re.compile(r"&")
    return chkRegex.sub("^&", url)


if __name__ == "__main__":
    haveUrl = False
    print("Internet Exolprer Launcher for Windows 10 22H2 v1.0")
    if len(sys.argv) > 1:
        haveUrl = True
        url = sys.argv[1]
        print(f"URL in argv: {url}")
        iexploreStartCmd = getIexploreStartCmd("C:\Program Files\Internet Explorer\iexplore.exe", url)
    else:
        print('No URL in argv, start iexplore.exe with url "about:blank"')
        iexploreStartCmd = getIexploreStartCmd("C:\Program Files\Internet Explorer\iexplore.exe", "about:blank")
    print(f"Execute: {iexploreStartCmd}")
    print("Internet Explorer started, you can close the window now.")
    os.system(iexploreStartCmd)
    print("Internet Explorer exited, exiting.")
    

"""
if __name__ == "__main__":
    testPatterns = [
        "https://www.icbc.com.cn/trans.html?transid=123456",
        "http://www.baidu.com/",
        "https://example.com/?abc=def",
        "https://www.baidu.com/baidu?ie=utf-8&wd=vscode+online"
    ]
    os.system(getIexplorerStartCmd("C:\Program Files\Internet Explorer\iexplore.exe", testPatterns[3]))
    
    for pattern in testPatterns:
        print(f"Pattern: {pattern}\nChkRet: {urlHaveQuery(pattern)}")
        ret=getIexplorerStartCmd('C:\Program Files\Internet Explorer\iexplore.exe', pattern)
        print(f"CmdRet: {ret}")
        

        print(getIexplorerStartCmd("C:\Program Files\Internet Explorer\iexplore.exe", testPatterns[3]))
        
"""
