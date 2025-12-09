# Switch
自用 Switch 整合包，根据以下整合清单，自动更新打包

## 整合清单

| 项目 | 作者 | 软件 | 版本 | 更新日期 | 存放路径 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphere-NX | `^atmosphere.*.zip$` | `1.10.1` | 20251209 | `switch_sdcard` | 大气层，Switch 系统破解核心 |
| [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphere-NX | `fusee.bin` | `1.10.1` | 20251209 | `switch_sdcard/bootloader/payloads/fusee.bin` | 大气层，Switch 系统破解核心 |
| [hekate](https://github.com/easyworld/hekate) | easyworld | `^hekate.*sc.zip$` | `v6.4.2` | 20251203 | `switch_sdcard` | bootloader 程序，用来启动大气层 |
| [sys-patch](https://github.com/impeeza/sys-patch) | impeeza | `sys-patch.zip` | `v1.5.7` | 20251111 | `switch_sdcard` | 外挂的大气层签名补丁，依赖 Tesla，替代 sigpatch |
| [Lockpick_RCMDecScots](https://github.com/zdm65477730/Lockpick_RCMDecScots) | zdm65477730 | `Lockpick_RCM.bin` | `1.9.16.0` | 20251121 | `switch_sdcard/bootloader/payloads/Lockpick_RCM.bin` | 主机系统的密钥提取工具 |
| [TegraExplorer](https://github.com/zdm65477730/TegraExplorer) | zdm65477730 | `TegraExplorer.bin` | `v4.2.0` | 20251121 | `switch_sdcard/bootloader/payloads/TegraExplorer.bin` | Hekate 下的文件管理工具 |
| [nx-ovlloader](https://github.com/ppkantorski/nx-ovlloader) | ppkantorski | `nx-ovlloader+.zip` | `v2.0.0` | 20251129 | `switch_sdcard` | Tesla 启动器 |
| [Ultrahand-Overlay](https://github.com/ppkantorski/Ultrahand-Overlay) | ppkantorski | `ovlmenu.ovl` | `v2.2.2` | 20251207 | `switch_sdcard/switch/.overlays/ovlmenu.ovl` | Tesla 菜单 |
| [Ultrahand-Overlay](https://github.com/ppkantorski/Ultrahand-Overlay) | ppkantorski | `lang.zip` | `v2.2.2` | 20251207 | `switch_sdcard/config/ultrahand/lang` | Tesla 菜单 |
| [ovl-sysmodules](https://github.com/ppkantorski/ovl-sysmodules) | ppkantorski | `ovlSysmodules.ovl` | `v1.4.5` | 20251206 | `switch_sdcard/switch/.overlays/ovlSysmodules.ovl` | Tesla 系统管理 |
| [Status-Monitor-Overlay](https://github.com/ppkantorski/Status-Monitor-Overlay) | ppkantorski | `Status-Monitor-Overlay.ovl` | `v1.3.2+r2` | 20251206 | `switch_sdcard/switch/.overlays/Status-Monitor-Overlay.ovl` | Tesla 系统监视器 |
| [EdiZon-Overlay](https://github.com/ppkantorski/EdiZon-Overlay) | ppkantorski | `ovlEdiZon.ovl` | `v1.0.9` | 20240930 | `switch_sdcard/switch/.overlays/ovlEdiZon.ovl` | Tesla 金手指游戏修改 |
| [OC_Toolkit_SC_EOS](https://github.com/halop/OC_Toolkit_SC_EOS) | halop | `sys-clk.zip` | `1.7.0` | 20251130 | `switch_sdcard` | Tesla 超频插件 |
| [OC_Toolkit_SC_EOS](https://github.com/halop/OC_Toolkit_SC_EOS) | halop | `kip.zip` | `1.7.0` | 20251201 | `switch_sdcard/atmosphere/kips` | 超频组件 |
| [DBIPatcher](https://github.com/rashevskyv/DBIPatcher) | rashevskyv | `^DBI.*zhcn.nro$` | `849` | 20251206 | `switch_sdcard/switch/DBI/DBI.nro` | 游戏安装，存档管理和文件传输工具（NRO） |
| [Hekate-Toolbox](https://github.com/WerWolv/Hekate-Toolbox) | WerWolv | `HekateToolbox.nro` | `v4.0.4` | 20251201 | `switch_sdcard/switch/HekateToolbox/HekateToolbox.nro` | 深海工具箱，插件管理（NRO） |
| [JKSV](https://github.com/J-D-K/JKSV) | J-D-K | `JKSV.nro` | `12/02/2025` | 20251202 | `switch_sdcard/switch/JKSV/JKSV.nro` | 游戏存档管理工具（NRO） |
