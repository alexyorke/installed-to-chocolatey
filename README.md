# installed-to-chocolatey
Convert your locally installed software into Chocolatey packages. This looks up the software installed on your Windows computer and sees if there is a Chocolatey package which would install that software. If so, it adds it to the list of packages to install.

The code is absolutely atrocious; PRs are welcome.


## Known issues

It is not perfect as sometimes the app names contain other numbers which conflict with Chocolatey's search, causing no search results. There is some primitive filtering on the programs (e.g. exclude updates and uninstallers) and it will remove the last word of the program name (e.g. `(x64)`) if no search results were found and then do another search. Always double check that the programs match before installing software from Chocolatey.


## Sample report (truncated)
```
Chocolatey Package List:
ChocolateyGUI
vscode-chrome-debug
speccy
adobereader
sqlserver-odbcdriver
typescript
nodejs-lts
windows-sdk-6.0
resharper-platform
netfx-4.5.1-devpack
rescuetime
...


This is how I matched them:
Visual Studio Community 2019->visualstudio2019community
Adobe Creative Cloud->adobe-creative-cloud
Audacity->audacity
Backblaze->cyberduck
Battle.net->battle.net
Dolphin->dolphin
Visual Studio Enterprise 2019->visualstudio2019enterprise
Foxit Reader->FoxitReader
Google Chrome->GoogleChrome
heroku->heroku-cli
...
```

The reports do not match up as I have deleted most of the output.
