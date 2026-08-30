# Switch
自用 Switch 整合包，根据以下整合清单，自动更新打包

## 整合清单

| 项目 | 作者 | 软件 | 版本 | 更新日期 | 存放路径 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphere-NX | `^atmosphere.*.zip$` | `1.11.2` | 20260616 | `switch_sdcard` | 大气层，Switch 系统破解核心 |
| [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphere-NX | `fusee.bin` | `1.11.2` | 20260616 | `switch_sdcard/bootloader/payloads/fusee.bin` | 大气层，Switch 系统破解核心 |
| [hekate](https://github.com/easyworld/hekate) | easyworld | `^hekate.*sc.zip$` | `v6.5.3` | 20260714 | `switch_sdcard` | bootloader 程序，用来启动大气层 |
| [sys-patch](https://github.com/impeeza/sys-patch) | impeeza | `sys-patch.zip` | `v1.5.7` | 20251111 | `switch_sdcard` | 外挂的大气层签名补丁，依赖 Tesla，替代 sigpatch |
| [Lockpick_RCMDecScots](https://github.com/zdm65477730/Lockpick_RCMDecScots) | zdm65477730 | `Lockpick_RCM.bin` | `v2.0.0` | 20260806 | `switch_sdcard/bootloader/payloads/Lockpick_RCM.bin` | 主机系统的密钥提取工具 |
| [TegraExplorer](https://github.com/zdm65477730/TegraExplorer) | zdm65477730 | `TegraExplorer.bin` | `v4.2.0` | 20251121 | `switch_sdcard/bootloader/payloads/TegraExplorer.bin` | Hekate 下的文件管理工具 |
| [Ultrahand-Overlay](https://github.com/ppkantorski/Ultrahand-Overlay) | ppkantorski | `sdout.zip` | `v2.5.3` | 20260718 | `switch_sdcard` | Tesla 启动器 |
| [ovl-sysmodules](https://github.com/ppkantorski/ovl-sysmodules) | ppkantorski | `ovlSysmodules.ovl` | `v1.5.3` | 20260625 | `switch_sdcard/switch/.overlays/ovlSysmodules.ovl` | Tesla 系统管理 |
| [Status-Monitor-Overlay](https://github.com/ppkantorski/Status-Monitor-Overlay) | ppkantorski | `Status-Monitor-Overlay.ovl` | `v1.4.1+r4` | 20260719 | `switch_sdcard/switch/.overlays/Status-Monitor-Overlay.ovl` | Tesla 系统监视器 |
| [EdiZon-Overlay](https://github.com/ppkantorski/EdiZon-Overlay) | ppkantorski | `ovlEdiZon.ovl` | `v1.0.9` | 20240930 | `switch_sdcard/switch/.overlays/ovlEdiZon.ovl` | Tesla 金手指游戏修改 |
| [Horizon-OC](https://github.com/Horizon-OC/Horizon-OC) | Horizon-OC | `dist.zip` | `2.5.1` | 20260726 | `switch_sdcard` | 超频组件 |
| [DBIPatcher](https://github.com/rashevskyv/DBIPatcher) | rashevskyv | `DBI.nro` | `905` | 20260829 | `switch_sdcard/switch/DBI/DBI.nro` | 游戏安装，存档管理和文件传输工具（NRO） |
| [DBIPatcher](https://github.com/rashevskyv/DBIPatcher) | rashevskyv | `translation_zhcn.bin` | `905` | 20260829 | `switch_sdcard/switch/DBI/translation.bin` | DBI 中文插件 |
| [Hekate-Toolbox](https://github.com/WerWolv/Hekate-Toolbox) | WerWolv | `HekateToolbox.nro` | `v4.0.4` | 20251201 | `switch_sdcard/switch/HekateToolbox/HekateToolbox.nro` | 深海工具箱，插件管理（NRO） |
| [JKSV](https://github.com/J-D-K/JKSV) | J-D-K | `JKSV.nro` | `12/02/2025` | 20251202 | `switch_sdcard/switch/JKSV/JKSV.nro` | 游戏存档管理工具（NRO） |
