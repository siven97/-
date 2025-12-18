# 启用 GitHub Pages 详细步骤

## 🚨 当前状态：404错误

这是因为GitHub Pages还没有启用。请按照以下步骤操作：

## 📝 启用步骤（5分钟）

### 步骤1：访问仓库设置

1. 打开浏览器，访问：
   ```
   https://github.com/siven97/-
   ```

2. 点击仓库顶部的 **Settings**（设置）标签

### 步骤2：找到Pages设置

1. 在左侧菜单中，向下滚动找到 **Pages**
2. 点击 **Pages**

### 步骤3：配置Pages

1. 在 **Source** 部分：
   - Branch: 选择 **main**
   - Folder: 选择 **/ (root)**
   
2. 点击 **Save** 按钮

### 步骤4：等待部署

1. 页面会显示：
   ```
   Your site is ready to be published at https://siven97.github.io/-/
   ```

2. 等待 1-2 分钟，刷新页面

3. 当显示变为：
   ```
   Your site is live at https://siven97.github.io/-/
   ```
   就说明部署成功了！

### 步骤5：测试访问

在浏览器中访问：
```
https://siven97.github.io/-/wifi-info.html
```

如果能看到页面，说明成功了！

## ✅ 成功后的操作

1. **测试二维码**
   - 用微信扫描 `wifi_qrcode.png`
   - 应该能看到WiFi信息页面
   - 点击密码测试复制功能

2. **如果还是404**
   - 等待5-10分钟（首次部署可能需要更长时间）
   - 清除浏览器缓存
   - 或使用无痕模式访问

## 🔧 常见问题

### Q1: 找不到Pages选项？
**A**: 确保：
- 仓库是Public（公开）的
- 您是仓库的所有者
- 刷新页面重试

### Q2: 显示"GitHub Pages is currently disabled"？
**A**: 
- 检查仓库是否为Private（私有）
- 如果是Private，需要升级到GitHub Pro才能使用Pages
- 或将仓库改为Public

### Q3: 部署后还是404？
**A**:
- 等待更长时间（最多10分钟）
- 检查URL是否正确
- 确认文件名是 `wifi-info.html`（区分大小写）

## 📱 快速验证方法

### 方法1：浏览器测试
```
https://siven97.github.io/-/wifi-info.html
```

### 方法2：检查部署状态
1. 访问仓库主页
2. 点击右侧的 **Environments**
3. 查看 **github-pages** 的部署状态

## 🎯 完成后

一旦GitHub Pages启用成功：
- ✅ 二维码可以正常扫描
- ✅ 页面可以正常访问
- ✅ WiFi密码可以点击复制
- ✅ 所有功能都能正常使用

## 📞 需要帮助？

如果按照步骤操作后仍然有问题：
1. 截图Settings -> Pages页面
2. 告诉我具体的错误信息
3. 我会帮您解决

---

**预计完成时间**: 5-10分钟
**难度**: ⭐⭐☆☆☆（简单）
