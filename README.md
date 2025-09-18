# Switch
自用 Switch 整合包，根据以下整合清单，自动更新打包

## 整合清单

| 项目 | 作者 | 软件 | 版本 | 更新日期 | 存放路径 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphere-NX | `^atmosphere.*.zip$` | `1.9.4` | 20250903 | `switch_sdcard` | 大气层，破解官方系统权限，运行插件和软件 |
| [Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphere-NX | `fusee.bin` | `1.9.4` | 20250903 | `switch_sdcard/bootloader/payloads/fusee.bin` | 大气层，破解官方系统权限，运行插件和软件 |
| [hekate](https://github.com/easyworld/hekate) | easyworld | `^hekate.*sc.zip$` | `v6.3.1` | 20250529 | `switch_sdcard` | bootloader 程序，用来加载 atmosphere、sigpatch |
| [sys-patch](https://github.com/impeeza/sys-patch) | impeeza | `sys-patch.zip` | `v1.5.6` | 20250505 | `switch_sdcard` | 外挂的大气层签名补丁，使大气层可运行破解软件，依赖 Tesla，替代 sigpatch |
| [Lockpick_RCMDecScots](https://github.com/zdm65477730/Lockpick_RCMDecScots) | zdm65477730 | `Lockpick_RCM.bin` | `1.9.15.0` | 20250516 | `switch_sdcard/bootloader/payloads/Lockpick_RCM.bin` | 主机系统的密钥提取工具 |
| [TegraExplorer](https://github.com/zdm65477730/TegraExplorer) | zdm65477730 | `TegraExplorer.bin` | `v4.2.0` | 20250516 | `switch_sdcard/bootloader/payloads/TegraExplorer.bin` | Hekate 下的文件管理工具 |
| [nx-ovlloader](https://github.com/zdm65477730/nx-ovlloader) | zdm65477730 | `nx-ovlloader.zip` | `1.0.7` | 20250801 | `switch_sdcard` | Tesla 启动器 |
| [Ultrahand-Overlay](https://github.com/zdm65477730/Ultrahand-Overlay) | zdm65477730 | `Ultrahand.zip` | `2.1.0-pre-release` | 20250906 | `switch_sdcard` | Tesla 菜单，替代 Tesla-Menu |
| [ovl-sysmodules](https://github.com/zdm65477730/ovl-sysmodules) | zdm65477730 | `ovl-sysmodules.zip` | `v1.3.1` | 20250801 | `switch_sdcard` | Tesla 系统管理 |
| [Status-Monitor-Overlay](https://github.com/zdm65477730/Status-Monitor-Overlay) | zdm65477730 | `StatusMonitor.zip` | `v1.2.2` | 20250906 | `switch_sdcard` | Tesla 系统监视器 |
| [EdiZon-Overlay](https://github.com/zdm65477730/EdiZon-Overlay) | zdm65477730 | `EdiZon.zip` | `v1.0.8` | 20250801 | `switch_sdcard` | Tesla 金手指游戏修改，含 NRO |
| [QuickNTP](https://github.com/zdm65477730/QuickNTP) | zdm65477730 | `QuickNTP.zip` | `v1.5.1` | 20250801 | `switch_sdcard` | Tesla 时间同步工具 |
| [OC_Toolkit_SC_EOS](https://github.com/halop/OC_Toolkit_SC_EOS) | halop | `sys-clk.zip` |  | 20250801 | `switch_sdcard` | Tesla 超频插件 |
| [OC_Toolkit_SC_EOS](https://github.com/halop/OC_Toolkit_SC_EOS) | halop | `kip.zip` | `1.6.8` | 20250903 | `switch_sdcard/atmosphere/kips` | 超频组件 |
| [Checkpoint](https://github.com/BernardoGiordano/Checkpoint) | BernardoGiordano | `Checkpoint.nro` | `v3.10.1` | 20250622 | `switch_sdcard/switch/Checkpoint/Checkpoint.nro` | 游戏存档管理工具 |
| [dbi](https://github.com/rashevskyv/dbi) | rashevskyv | `DBI.810.zhcn.nro` | `810` | 20250911 | `switch_sdcard/switch/DBI/DBI.nro` | 游戏安装，存档管理和文件传输工具 |
| [Hekate-Toolbox](https://github.com/WerWolv/Hekate-Toolbox) | WerWolv | `HekateToolbox.nro` | `v4.0.3` | 20230417 | `switch_sdcard/switch/HekateToolbox/HekateToolbox.nro` | 深海工具箱，插件管理 |
| [Goldleaf](https://github.com/XorTroll/Goldleaf) | XorTroll | `Goldleaf.nro` | `1.1.1` | 20250610 | `switch_sdcard/switch/Goldleaf/Goldleaf.nro` | 文件管理工具 |
| [JKSV](https://github.com/J-D-K/JKSV) | J-D-K | `JKSV.nro` | `09/13/2025` | 20250914 | `switch_sdcard/switch/JKSV/JKSV.nro` | 游戏存档管理工具 |
| [NX-Activity-Log](https://github.com/zdm65477730/NX-Activity-Log) | zdm65477730 | `NX-Activity-Log.nro` | `v1.5.7` | 20250429 | `switch_sdcard/switch/NX-Activity-Log/NX-Activity-Log.nro` | 游戏游玩时间记录工具 |
