#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成WiFi信息页面的二维码
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_qrcode():
    """生成二维码"""
    
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # GitHub Pages URL (index.html可以省略)
    url = "https://siven97.github.io/-/"
    
    print(f"生成二维码，链接到: {url}")
    
    # 创建二维码实例
    qr = qrcode.QRCode(
        version=5,  # 控制二维码的大小，1-40
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 高容错率
        box_size=10,  # 每个小格子的像素大小
        border=4,  # 边框的格子宽度
    )
    
    # 添加数据
    qr.add_data(url)
    qr.make(fit=True)
    
    # 创建图片
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 转换为RGB模式以便添加文字
    img = img.convert('RGB')
    
    # 创建一个更大的画布，用于添加标题和说明
    canvas_width = img.size[0]
    canvas_height = img.size[1] + 200  # 增加空间用于文字
    
    canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
    
    # 将二维码粘贴到画布中央
    qr_position = ((canvas_width - img.size[0]) // 2, 100)
    canvas.paste(img, qr_position)
    
    # 添加文字
    draw = ImageDraw.Draw(canvas)
    
    try:
        # 尝试使用系统字体
        title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
        text_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 24)
    except:
        # 如果找不到字体，使用默认字体
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # 标题
    title = "高端旅客尊享服务指南"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (canvas_width - title_width) // 2
    draw.text((title_x, 30), title, fill='black', font=title_font)
    
    # 说明文字
    instruction = "扫码查看详情 · WiFi密码可点击复制"
    inst_bbox = draw.textbbox((0, 0), instruction, font=text_font)
    inst_width = inst_bbox[2] - inst_bbox[0]
    inst_x = (canvas_width - inst_width) // 2
    draw.text((inst_x, canvas_height - 60), instruction, fill='#666666', font=text_font)
    
    # 保存二维码
    output_path = os.path.join(current_dir, 'wifi_qrcode.png')
    canvas.save(output_path)
    print(f"✅ 二维码已生成: {output_path}")
    
    # 生成一个简单版本（只有二维码，无文字）
    simple_output_path = os.path.join(current_dir, 'wifi_qrcode_simple.png')
    img.save(simple_output_path)
    print(f"✅ 简单版二维码已生成: {simple_output_path}")
    
    return output_path

def generate_wifi_qrcode():
    """生成WiFi直连二维码（可选）"""
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # WiFi信息
    ssid = "您的WiFi名称"  # 请替换为实际WiFi名称
    password = "031196699"
    security = "WPA"  # WPA, WEP, 或 nopass
    
    # WiFi二维码格式
    wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};;"
    
    # 创建二维码
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(wifi_string)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert('RGB')
    
    # 添加标题
    canvas_width = img.size[0]
    canvas_height = img.size[1] + 150
    canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
    canvas.paste(img, ((canvas_width - img.size[0]) // 2, 80))
    
    draw = ImageDraw.Draw(canvas)
    
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 36)
        text_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 20)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    title = "WiFi 直连"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((canvas_width - title_width) // 2, 20), title, fill='black', font=title_font)
    
    instruction = f"扫码自动连接 · 密码: {password}"
    inst_bbox = draw.textbbox((0, 0), instruction, font=text_font)
    inst_width = inst_bbox[2] - inst_bbox[0]
    draw.text(((canvas_width - inst_width) // 2, canvas_height - 50), instruction, fill='#666666', font=text_font)
    
    output_path = os.path.join(current_dir, 'wifi_direct_qrcode.png')
    canvas.save(output_path)
    print(f"✅ WiFi直连二维码已生成: {output_path}")
    print(f"   注意: 需要将 'ssid' 变量替换为实际的WiFi名称")
    
    return output_path

if __name__ == '__main__':
    print("=" * 60)
    print("WiFi信息二维码生成器")
    print("=" * 60)
    print()
    
    # 生成信息页面二维码
    print("1. 生成信息页面二维码...")
    generate_qrcode()
    print()
    
    # 生成WiFi直连二维码（可选）
    print("2. 生成WiFi直连二维码（可选）...")
    generate_wifi_qrcode()
    print()
    
    print("=" * 60)
    print("✅ 所有二维码生成完成！")
    print()
    print("📝 使用说明:")
    print("   1. wifi_qrcode.png - 完整版二维码（带标题和说明）")
    print("   2. wifi_qrcode_simple.png - 简单版二维码（仅二维码）")
    print("   3. wifi_direct_qrcode.png - WiFi直连二维码（需配置WiFi名称）")
    print()
    print("⚠️  重要提示:")
    print("   - 需要将 wifi-info.html 部署到Web服务器")
    print("   - 然后修改脚本中的 url 变量为实际URL")
    print("   - 重新运行脚本生成最终二维码")
    print("=" * 60)
