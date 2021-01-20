d = {'诗名': '新年', '内容': '爆竹声中辞旧岁\n桃符字里贺新年\n烟花璀璨迎春到\n除夕人间不夜天\n'}

tmp_p = {'诗名': '新年', '内容': '爆竹声中辞旧岁\n桃符字里贺新年\n烟花璀璨迎春到\n除夕人间不夜天\n'}
poem_title = tmp_p.get("诗名")
poem_content = tmp_p.get("内容")
p = poem_title+","+ ",".join(poem_content.splitlines())
print(p)
