; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Woodrow Wilson Bridge"
#define MyAppVersion "1.1"
#define MyAppPublisher "Porcej"
#define MyAppURL "https://github.com/porcej/wwbridge"
#define MyAppExeName "ww_bridge.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E65020BA-AB9F-4B54-B78C-C607C3658F6F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\ww_bridge
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename=wwbridge_setup
Compression=lzma
SolidCompression=yes
LicenseFile=license.txt
ArchitecturesInstallIn64BitMode=x64


[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\dist\ww_bridge.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\config.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.json"; DestDir: "{app}"; Flags: ignoreversion; Permissions: users-modify
Source: "install.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "start.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "stop.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "remove.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "license.txt"; DestDir: "{app}"; Flags: ignoreversion

; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKLM; Subkey: "SOFTWARE\Porcej\wwbridge"; ValueType: string; ValueName: "Path"; ValueData: "{app}"

[Run]
Filename: "{app}\config.exe"
Filename: "{app}\install.bat"
Filename: "{app}\start.bat"

[UninstallRun]
Filename: "{app}\stop.bat"
Filename: "{app}\remove.bat"

[Icons]
Name: "{group}\WWBridge Start"; Filename: "{app}\start.bat"
Name: "{group}\WWBridge Stop"; Filename: "{app}\stop.bat"
Name: "{group}\Configuration"; Filename: "{app}\config.exe"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"

