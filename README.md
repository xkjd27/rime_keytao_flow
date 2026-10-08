# 键道6・流 - KeyTao 双形顶功输入方案

基于[键道6](https://github.com/xkinput/KeyTao)的布局与设计，把原版固定码表转成
「流」方案的词库：简码层级与重码顺序保留原版，形码由流引擎在运行时按字筛选。

## 布局

* 声母键 `bcdefghjklmnpqrstwxyz`（`sh` = `e`；`zh` = `q`/`f`、`ch` = `j`/`w`，
  按韵母分「外侧 / 内侧」）
* 笔形键 `aiouv`
* 飞键：`zh` 接 `ai`/`ao`/`e`、`ch` 接 `ao`/`e`、韵母 `uang` 都可用两个键位
  （装 = `fm`/`fx`，这 = `qe`/`fe`，光 = `gm`/`gx`）

## 与键道6的区别

| | 键道6 | 键道6・流 |
| --- | ---|---|
| 码表词库 | ✅ 固定码表 | ✅ 原版码表转换（简码与顺序保留） |
| 词组码长 | ❌ 最长6码，无全码 | ✅ 按词组长度配置全码，简码自动排权 |
| 码长调整 | ❌ 纯手动排码排重 | ✅ <kbd>-</kbd> <kbd>=</kbd> 键排码功能，自动避重 |
| 用户词 | ❌ 需要改文件部署 | ✅ <kbd>`</kbd> 键造词功能 |
| 次码支持 | ✅ 任意长度次码 | ➖ 仅支持一简码 |
| 声笔笔简码 | ✅ 支持 | ❌ 不支持 |
| 单字模式 | ✅ 支持 | ❌ 不支持 |

由于 键道6・流 使用词库权重自动排码，候选顺序可能与 键道6 略有出入
（同码重码、形码深度大的位置）；但有了自主排码功能，用户可以自己实时修改码长。

另外由于使用了大量 lua 脚本，该方案性能可能不如键道6。

## 词库

`rime/keytao_orig.*` 由键道6 原版码表（`keytao.single` / `keytao.phrase` /
`keytao.supplement`）转换而来：

* `keytao_orig.dict.yaml` 词组（import 单字 / 形码表）
* `keytao_orig.danzi.dict.yaml` 单字音码
* `keytao_orig.shape.dict.yaml` 纯形码条目
* `keytao_orig.shape.txt` 每个字的完整形码（运行时筛选用）

权重用 **len-dupe**：先按原码码长分层（原码越短权重越高），只有同一个生成码
里的重码才按原表顺序做次级排序。

重新生成（需要 KeyTao 仓库；默认读 `/tmp/KeyTao`，不在会自动 clone）：

```sh
python3 engine/tools/keytao_table_to_flow_dict.py --out-dir rime
```

## 排码

在打字过程中，使用 <kbd>-</kbd> <kbd>=</kbd> 按键即可排码：
- <kbd>-</kbd> 缩短编码，提高权重
- <kbd>=</kbd> 加长编码，降低权重

## 造词

按 <kbd>`</kbd> 进入造词模式。在造词模式中，正常输入希望要编码的词组或句子。输入过程中不会完全上屏，输入完成后：
- 按 <kbd>-</kbd> 自动以词组全码加入词库，之后继续按 <kbd>-</kbd> <kbd>=</kbd> 调整新词的码长
- 按 <kbd>=</kbd> 删除自造词或清空输入法自带词库中的排码（非自造词只能还原默认编码权重，不可删除）

## 用户词库

在用户配置目录中，会生成 `keytao_flow.order.userdb` 用户词库，用于存储所有自造词与编辑过的排码。请注意备份保存，避免词库丢失。同步和备份时请删库覆盖，合并词库可能会导致算法异常

## 配置

可调项写在用户配置目录的 `keytao_flow.custom.yaml`，重新部署后生效：

```yaml
patch:
  # 调序与造词数据库：
  # leveldb 高性能 默认
  # txt 纯文本 方便手动修改
  flow_order/backend: leveldb

  # 最近造词列表上限（默认 20）
  flow_order/recent_max: 20

  # 候选提示配置
  flow_hint:
    # 笔码提示
    shape: true
    # 不可顶功提示（⛔️）
    topup: true

  # 次简（🔹 + Tab 上屏/学习）；键道6 的次选走撇号，这里默认关闭
  flow_secondary: false
```

## 致谢与许可

* 星空键道原作者：吅吅大山（[键道6官网](https://xkinput.github.io/)）
* 引擎：[flow_engine](https://github.com/xkjd27/flow_engine)（与 键道27・流 / 键道27C・流 共用）

本方案开源许可为 **GPL-3.0**（见 `LICENSE`）。
