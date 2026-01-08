# 鳌太行者 (Aotai Walker)

[![Deploy to GitHub Pages](https://github.com/fangzz12138/Aotai_walker/actions/workflows/deploy.yml/badge.svg)](https://github.com/fangzz12138/Aotai_walker/actions/workflows/deploy.yml)

一个基于 Pygame 开发的硬核生存模拟游戏，重现徒步“鳌太线”的艰难旅程。

## 🎮 游戏在线试玩
**[点击这里开始冒险](https://fangzz12138.github.io/Aotai_walker/)**

## 🌟 游戏特色
- **环境模拟**：实时模拟鳌太线多变的天气、气温和风力。
- **生存机制**：管理体力、饥饿、口渴、体温、健康以及精神状态（SAN值）。
- **物资管理**：背负重量限制，合理分配食物、水和露营装备。
- **动态地图**：在经典的鳌太路段（如火烧坡、盆景园、白起庙、大爷海等）间穿梭。
- **事件系统**：旅途中会遇到各种随机事件，考验你的决策能力。

## 🛠️ 技术栈
- **语言**: Python 3.12
- **引擎**: Pygame CE (Community Edition)
- **Web 技术**: Pygbag (将 Python 编译为 WebAssembly 运行于浏览器)
- **部署**: GitHub Actions & GitHub Pages

## 🚀 本地运行指南

1. **克隆仓库**
   ```bash
   git clone https://github.com/fangzz12138/Aotai_walker.git
   cd Aotai_walker
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **启动游戏**
   ```bash
   python main.py
   ```

## 🌐 Web 版开发与部署

如需更新 Web 版本，请确保已安装 `pygbag`：

1. **本地预览 Web 版**
   ```bash
   python -m pygbag .
   ```
   然后在浏览器打开 `http://localhost:8000`。

2. **发布更新**
   将更改推送到 `master` 分支，GitHub Actions 会自动处理后续的所有打包与部署工作。

## 📝 存档说明
- 本地版：保存于项目根目录的 `savegame.json`。
- Web 版：存档保存于浏览器的 LocalStorage 中。

## ⚖️ 免责声明
本游戏仅为模拟体验，鳌太线具有极高的真实危险性，现实中请勿在无经验和装备的情况下轻易尝试。

---
*由 GitHub Copilot 辅助开发*
