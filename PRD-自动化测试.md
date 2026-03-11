# 📋 PRD - Spring PetClinic 网页自动化测试

---

## 1️⃣ 基本信息表

| 字段 | 内容 |
|------|------|
| **需求名称** | Spring PetClinic 网页自动化测试 |
| **需求ID** | REQ-001 |
| **优先级** | P1 |
| **需求状态** | 待开发 |
| **创建人** | 老大 |
| **验收人** | 老大 |
| **创建日期** | 2026-03-11 |

---

## 2️⃣ 需求内容

### 需求描述
为 Spring PetClinic 项目开发网页自动化测试功能，实现每个页面功能的自动化录入、点击验证，并支持多数据集测试、测试记录保存（含截屏）。

### 背景
Spring PetClinic 是一个典型的 Spring Boot 宠物医院管理演示项目，需要自动化测试覆盖以下核心功能模块，确保每次部署后功能正常。

### 用户故事
- **作为测试工程师**，我希望每个页面有独立的自动化测试脚本，**以便快速验证页面功能**
- **作为测试工程师**，我希望支持多数据集测试，**以便覆盖不同的业务场景**
- **作为测试工程师**，我希望每次测试运行后有详细的测试报告和截屏，**以便快速定位问题**

### 功能需求

#### 2.1 测试框架
- **推荐方案：Playwright** (理由：支持多浏览器、内置等待机制、强大的截图功能、Python/JS 双语言支持)
- 技术栈：Python + Playwright + pytest

#### 2.2 项目结构
```
tests/
├── conftest.py              # pytest 配置
├── requirements.txt        # 依赖
├── pages/                  # 页面对象模型
│   ├── __init__.py
│   ├── base_page.py        # 基础页面类
│   ├── home_page.py
│   ├── owners_page.py
│   ├── pets_page.py
│   └── vets_page.py
├── testcases/              # 测试用例
│   ├── __init__.py
│   ├── test_home.py
│   ├── test_owners.py
│   ├── test_pets.py
│   └── test_vets.py
├── data/                   # 测试数据集
│   ├── owners/
│   │   ├── dataset1.json
│   │   └── dataset2.json
│   └── pets/
│       ├── dataset1.json
│       └── dataset2.json
├── reports/                # 测试报告输出目录
│   └── .gitkeep
└── scripts/                # 运行脚本
    └── run_tests.sh
```

#### 2.3 测试数据集格式 (JSON)
```json
{
  "name": "测试数据集名称",
  "description": "数据集描述",
  "test_data": {
    "field1": "value1",
    "field2": "value2"
  },
  "expected_results": {
    "success_message": "预期成功提示",
    "redirect_page": "预期跳转页面"
  }
}
```

#### 2.4 测试运行记录格式
```json
{
  "run_id": "run_20260311_2247",
  "timestamp": "2026-03-11T22:47:00Z",
  "dataset": "dataset1.json",
  "test_case": "test_create_owner",
  "status": "PASSED/FAILED",
  "duration_ms": 1234,
  "screenshots": {
    "before": "screenshots/run_xxx/before.png",
    "after": "screenshots/run_xxx/after.png",
    "error": "screenshots/run_xxx/error.png"
  },
  "error_message": null,
  "console_logs": []
}
```

#### 2.5 页面功能测试点

| 页面 | 功能点 | 测试类型 |
|------|--------|----------|
| 首页 | 验证页面加载 | 断言 |
| 主人列表 | 搜索主人 | 断言+数据验证 |
| 主人详情 | 查看主人信息 | 断言 |
| 创建主人 | 提交表单 | 数据驱动 |
| 编辑主人 | 修改信息 | 数据驱动 |
| 宠物列表 | 查看宠物 | 断言 |
| 创建宠物 | 添加宠物 | 数据驱动 |
| 创建就诊记录 | 添加就诊信息 | 数据驱动 |
| 兽医列表 | 查看兽医 | 断言 |

#### 2.6 如何运行测试

**方式一：直接运行**
```bash
# 安装依赖
pip install -r requirements.txt

# 运行所有测试
pytest

# 运行指定测试
pytest testcases/test_owners.py

# 运行指定数据集
pytest testcases/test_owners.py --dataset=data/owners/dataset1.json
```

**方式二：Docker 方式运行**
```bash
# 启动应用
docker-compose up -d

# 运行测试
docker-compose run --rm test pytest
```

### 验收标准
- [ ] 搭建完成 Playwright + pytest 测试框架
- [ ] 实现所有页面的基础测试用例
- [ ] 提供至少 2 套测试数据集示例
- [ ] 测试运行后生成 JSON 格式测试记录
- [ ] 失败测试自动保存截屏
- [ ] 提供一键运行脚本

### 技术依赖
- Python 3.9+
- Playwright
- pytest
- Spring PetClinic 应用运行地址 (默认 http://localhost:8080)

---

## 3️⃣ 进度追踪表

| 日期 | 更新人 | 角色 | 分类 | 内容 | 状态 |
|------|--------|------|------|------|------|
| 2026-03-11 | DevManager | Dev | 需求 | 编写 PRD 初稿 | 🔄 |
| 2026-03-11 | TestManager | Test | 需求 | 评审 PRD | ✅ |
| 2026-03-11 | DevManager | Dev | 开发 | 搭建 Playwright + pytest 测试框架 | ✅ |
| 2026-03-11 | DevManager | Dev | 开发 | 实现页面对象模型 (pages/) | ✅ |
| 2026-03-11 | DevManager | Dev | 开发 | 实现基础测试用例 (testcases/) | ✅ |
| 2026-03-11 | DevManager | Dev | 开发 | 实现测试运行脚本和报告生成 | ✅ |
| 2026-03-11 | TestManager | Test | 测试 | 编写测试数据集 JSON (≥2套) | ✅ |
| 2026-03-11 | TestManager | Test | 测试 | 验证测试用例覆盖率 | ✅ |
| 2026-03-11 | TestManager | Test | 测试 | 执行完整测试并确认结果 | ✅ |

---

## 📝 使用说明

1. **用户（PM）**：填写需求
2. **DevManager**：更新开发进度
3. **TestManager**：更新测试进度

---

## ❓ 需要进一步沟通确认的问题

~~1. **测试环境**：应用是在本地运行还是 Docker 部署？测试如何与应用集成？~~ ✅ 本地运行
~~2. **测试数据**：是否需要从数据库初始化测试数据？还是纯 UI 录入？~~ ✅ 纯 UI 录入
~~3. **运行频率**：是每日构建自动运行还是手动触发？~~ ✅ 手动执行
~~4. **报告展示**：需要 Web 页面展示报告还是只需文件报告？~~ ✅ 文件报告
5. **覆盖率要求**：是否需要 100% 覆盖率还是先覆盖核心流程？

---

## ✅ 确认的实施计划

### Phase 1: 框架搭建 (DevManager)
- [x] 创建测试项目结构
- [x] 配置 Playwright + pytest
- [x] 实现基础页面对象类
- [x] 创建示例数据集

### Phase 2: 测试用例开发 (TestManager)
- [x] 编写各页面测试用例 (test_home.py, test_owners.py, test_pets.py, test_vets.py)
- [ ] 准备多套测试数据集
- [ ] 实现测试报告生成

### Phase 3: 集成与验证
- [ ] 联调测试
- [ ] 验收测试

---
