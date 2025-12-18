# WiFi信息二维码生成器

这个项目可以生成一个美观的WiFi信息展示页面，并生成对应的二维码。

## 文件说明

- `wifi-info.html` - WiFi信息展示页面（精美设计，支持密码点击复制）
- `generate_qrcode.py` - 二维码生成脚本
- `README.md` - 本说明文档

## 功能特点

✅ 精美的卡片式设计
✅ WiFi密码点击即可复制
✅ 响应式布局，适配手机和平板
✅ 流畅的动画效果
✅ 支持生成多种二维码

## 使用步骤

### 方法一：使用在线服务（推荐）

1. **部署HTML页面**
   - 将 `wifi-info.html` 上传到任何Web服务器
   - 或使用免费托管服务（如 GitHub Pages、Vercel、Netlify）

2. **生成二维码**
   ```bash
   # 安装依赖
   pip install qrcode pillow
   
   # 修改脚本中的URL为实际地址
   # 编辑 generate_qrcode.py，将 url 变量改为实际URL
   
   # 运行脚本
   python3 generate_qrcode.py
   ```

3. **打印或分享二维码**
   - 使用生成的 `wifi_qrcode.png`

### 方法二：本地测试

1. **直接打开HTML文件**
   ```bash
   # 在浏览器中打开
   open wifi-info.html
   ```

2. **使用本地服务器**
   ```bash
   # Python 3
   python3 -m http.server 8000
   
   # 然后访问 http://localhost:8000/wifi-info.html
   ```

### 方法三：使用免费托管服务

#### GitHub Pages（推荐）

1. 创建GitHub仓库
2. 上传 `wifi-info.html`
3. 在仓库设置中启用 GitHub Pages
4. 获得类似 `https://username.github.io/repo-name/wifi-info.html` 的URL
5. 修改 `generate_qrcode.py` 中的URL
6. 运行脚本生成二维码

#### Vercel（最简单）

1. 访问 https://vercel.com
2. 注册账号（可用GitHub登录）
3. 点击 "New Project"
4. 上传包含 `wifi-info.html` 的文件夹
5. 自动部署，获得URL
6. 生成二维码

## 自定义内容

### 修改WiFi密码

编辑 `wifi-info.html`，找到以下代码：

```javascript
const password = '031196699';  // 修改这里的密码
```

同时修改显示的密码：

```html
<span class="wifi-password" onclick="copyPassword()">
    031196699  <!-- 修改这里的显示密码 -->
    <span class="copy-icon">📋</span>
</span>
```

### 修改其他信息

直接编辑 `wifi-info.html` 中的文本内容即可。

## 生成的二维码类型

运行脚本后会生成3种二维码：

1. **wifi_qrcode.png** - 完整版（带标题和说明文字）
2. **wifi_qrcode_simple.png** - 简单版（仅二维码）
3. **wifi_direct_qrcode.png** - WiFi直连二维码（扫码自动连接WiFi）

## WiFi直连二维码

如果想生成扫码即可连接WiFi的二维码，需要：

1. 编辑 `generate_qrcode.py`
2. 找到 `generate_wifi_qrcode()` 函数
3. 修改以下变量：
   ```python
   ssid = "您的WiFi名称"  # 改为实际WiFi名称
   password = "031196699"  # WiFi密码
   security = "WPA"        # 加密方式：WPA/WEP/nopass
   ```
4. 重新运行脚本

## 技术栈

- HTML5 + CSS3 + JavaScript
- Python 3 + qrcode + Pillow
- 响应式设计
- 现代浏览器Clipboard API

## 浏览器兼容性

- ✅ Chrome/Edge (推荐)
- ✅ Safari (iOS/macOS)
- ✅ Firefox
- ✅ 微信内置浏览器

## 常见问题

### Q: 二维码扫不出来？
A: 确保HTML文件已部署到可访问的Web服务器，本地文件路径无法通过二维码访问。

### Q: 密码复制不成功？
A: 某些旧版浏览器可能不支持，建议使用现代浏览器或微信扫码。

### Q: 如何修改样式？
A: 直接编辑 `wifi-info.html` 中的 `<style>` 部分。

### Q: 可以添加更多信息吗？
A: 可以！按照现有格式添加新的 `info-item` 即可。

## 示例效果

扫描二维码后，用户将看到：
- 📱 精美的卡片式界面
- 🎨 渐变色彩设计
- 📋 点击即可复制WiFi密码
- ✨ 流畅的动画效果

## 许可证

MIT License - 可自由使用和修改

## 联系方式

如有问题，请联系开发者。
