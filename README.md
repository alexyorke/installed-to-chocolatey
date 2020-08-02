# installed-to-chocolatey
Convert your locally installed software into Chocolatey packages. This looks up the software installed on your Windows computer and sees if there is a Chocolatey package which would install that software. If so, it adds it to the list of packages to install.

The code is absolutely atrocious; PRs are welcome.

This does not modify any installed programs. It just lists which ones that can be found via Chocolatey.

[![Updates](https://pyup.io/repos/github/alexyorke/installed-to-chocolatey/shield.svg)](https://pyup.io/repos/github/alexyorke/installed-to-chocolatey/) [![Python 3](https://pyup.io/repos/github/alexyorke/installed-to-chocolatey/python-3-shield.svg)](https://pyup.io/repos/github/alexyorke/installed-to-chocolatey/)

## Known issues

It is not perfect as sometimes the app names contain other numbers which conflict with Chocolatey's search, causing no search results. There is some primitive filtering on the programs (e.g. exclude updates and uninstallers) and it will remove the last word of the program name (e.g. `(x64)`) if no search results were found and then do another search. Always double check that the programs match before installing software from Chocolatey.

If the version is undefined, then the package version in the manifest will be invalid. This can cause issues when installing.


## Sample report (truncated)
```
<?xml version="1.0" encoding="utf-8"?><packages>
<package id="audacity" version="2.3.2" />
<package id="iisexpress" version="10.0.03203" />
<package id="sharex" version="13.0.1" />
<package id="intel-proset-drivers" version="21.30.2" />
<package id="treesizefree" version="4.4.1" />
<package id="adobereader" version="19.021.20061" />
<package id="netfx-4.7.2-devpack" version="4.7.03062" />
<package id="netfx-4.8" version="4.8.03928" />
...
</packages>


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
