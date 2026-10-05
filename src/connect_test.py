"""
第一个脚本：连接一台网络设备，执行一条命令并打印结果。

这是整个工具包的最小可运行骨架。跑通它，你就完成了
「用代码登录设备」的第一步。

用法：
    python src/connect_test.py
"""
from netmiko import ConnectHandler

# 设备连接参数（先用你的 eNSP/GNS3 模拟器里的一台设备）
device = {
    "device_type": "cisco_ios_telnet",   # 模拟器常用 telnet；真实设备用 SSH 驱动
    "host": "192.168.56.101",
    "username": "admin",
    "password": "admin123",
    "secret": "admin123",                # enable 密码
}

def main():
    print("正在连接设备 ...")
    with ConnectHandler(**device) as conn:
        # 进入特权模式
        conn.enable()
        # 查看设备基本信息
        output = conn.send_command("show version")
        print(output)
    print("连接成功，命令执行完毕。")

if __name__ == "__main__":
    main()
