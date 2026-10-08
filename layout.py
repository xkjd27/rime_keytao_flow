#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""键道（KeyTao）方案布局表与构建元信息（``keytao_table_to_flow_dict.py --layout``）。

布局表来源：键道文档「键道音码」「飞键」
（https://keytao-docs.rea.ink/guide/learn-xkjd/phonetics-rules.html
  https://keytao-docs.rea.ink/guide/advance-in-xkjd/alt-code.html），
与 KeyTao 仓库的 ``keytao.single`` / ``keytao.phrase`` 码表核对过。
``SOURCE`` / ``OUT`` 若是相对路径，按本文件所在目录解析。
"""

# ---- 构建元信息 ----
NAME = 'keytao_flow'           # 输出前缀
TITLE = '键道・函流'            # 词库文件头里的中文名
SHAPE_SECTION = '形简'          # 形码段名（本方案不读上游 补充.txt，留着对齐格式）
SOURCE = 'engine/data'         # 本方案只读 KeyTao 仓库，这个字段不用
OUT = 'rime'                   # 输出目录

# ---- 布局表 ----
PY_TRANSFORM = {
    'qve': 'que', 'lve': 'lue', 'nve': 'nue', 'jve': 'jue', 'xve': 'xue',
    'yve': 'yue', 'm': 'en', 'ng': 'eng',
}

PY_SHENG = {
    'a': '~', 'ai': '~', 'an': '~', 'ang': '~', 'ao': '~',
    'e': '~', 'ei': '~', 'en': '~', 'eng': '~', 'er': '~',
    'o': '~', 'ou': '~',
}

# 与 27C 不同：y 开头的音节按「y + 原韵母」拼（也 = ye、有 = yd、眼 = yf、
# 样 = yp），不做 ia/ian/iang/iao/ie/iu 的还原；只有 ü 系要还原
# （ju/qu/xu/yu -> v，yue/yuan/yun 由去声母得到 ue/uan/un）。
PY_YUN = {
    'ju': 'v', 'qu': 'v', 'xu': 'v', 'yu': 'v',
    'a': 'a', 'ai': 'ai', 'an': 'an', 'ang': 'ang', 'ao': 'ao',
    'e': 'e', 'ei': 'ei', 'en': 'en', 'eng': 'eng', 'er': 'er',
    'o': 'o', 'ou': 'ou',
}

# 声母键（sh 固定 e，零声母 x；zh/ch 见 JD_S2K_YUN）
JD_S2K = {
    'b': 'b', 'p': 'p', 'm': 'm', 'f': 'f', 'd': 'd', 't': 't', 'n': 'n',
    'l': 'l', 'g': 'g', 'k': 'k', 'h': 'h', 'j': 'j', 'q': 'q', 'x': 'x',
    'r': 'r', 'z': 'z', 'c': 'c', 's': 's', 'y': 'y', 'w': 'w',
    'sh': 'e', '~': 'x',
}

# 韵母键（uang 是飞键：M / X 两个键都行）
JD_Y2K = {
    'a': 's', 'ia': 's', 'ai': 'h', 'an': 'f', 'ang': 'p', 'ao': 'z',
    'e': 'e', 'ei': 'w', 'en': 'n', 'eng': 'r', 'er': 'j', 'i': 'k',
    'ian': 'm', 'iang': 'x', 'iao': 'c', 'ie': 'd', 'in': 'b', 'ing': 'g',
    'iong': 'y', 'iu': 'q', 'o': 'l', 'uo': 'l', 'ong': 'y', 'ou': 'd',
    'u': 'j', 'v': 'l', 'ua': 'q', 'uai': 'g', 'uan': 't', 'uang': 'mx',
    'ue': 'h', 'ui': 'b', 'un': 'w',
}

# 飞键 / 拼合规则：{声母: [(键位, '韵母 列表'), ...]}
# 外侧韵母用 q / j，内侧用 f / w；飞键韵母两个键位都行（键位串写两个字母）。
JD_S2K_YUN = {
    'zh': [('q', 'an ang ei en eng u un'),
           ('f', 'a i ong ou ua uai uan uang ui uo'),
           ('qf', 'ai ao e')],
    'ch': [('j', 'ai an ang en eng u un'),
           ('w', 'a i ong ou ua uai uan uang ui uo'),
           ('jw', 'ao e')],
}

# 笔形键（丿 用 u，与 27C 的 e 不同）
JD_B = {'乛': 'a', '丿': 'u', '丨': 'i', '丶': 'o', '㇐': 'v'}
