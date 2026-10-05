# Network Automation Toolkit

用 Python 批量管理网络设备的自动化工具包。

不用再一台台手动登录交换机/路由器敲命令——用代码批量完成配置下发、配置备份、巡检采集与报告生成。

## 功能规划

- [ ] 设备批量连接（SSH / netmiko）
- [ ] 配置批量备份（自动导出 running-config）
- [ ] 批量下发配置（VLAN / OSPF / BGP 等）
- [ ] 设备巡检采集（CPU / 内存 / 接口状态）
- [ ] 巡检报告生成（Excel）
- [ ] 配置差异对比（diff）

## 技术栈

- Python 3.12
- netmiko（网络设备 SSH 自动化库）
- openpyxl（生成 Excel 巡检报告）

## 项目结构

```
network-automation-toolkit/
├── src/          # 源码
├── inventory/    # 设备清单（devices.yaml）
├── configs/      # 备份的配置与下发模板
├── reports/      # 巡检报告输出
└── README.md
```

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 连接一台设备测试
python src/connect_test.py
```

## 作者

Jinqi Sun · 网络工程专业在读

> 本项目为求职作品，用于展示 Python + 网络自动化能力，将随学习进度持续完善。
