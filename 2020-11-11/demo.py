import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from tempfile import mkstemp
from typing import Dict, List


def mock_word_cloud() -> None:
    src = "code_wc.py"
    path_key_word = "packages"
    for i in sys.path:
        if path_key_word in i:
            dest_dir_path = Path(i, "wordcloud")
            dest_file_path = dest_dir_path / "wordcloud.py"
            break
    else:
        raise FileNotFoundError("Can't find site packages path")
    dest_dir_path.mkdir(parents=True, exist_ok=True)
    if dest_file_path.exists():
        dest_file_path.unlink()
    shutil.copyfile(src, dest_file_path)
    print("review_wordcloud 后台文件生成成功！")


def review_word_cloud(code: str, answer: Dict, scores: Dict, debug: bool = False):
    # 将code写入文件
    tmp_fp, tmp_file_name = mkstemp(suffix=".py", dir='.', text=True)
    with open(tmp_file_name, 'w') as f:
        f.write(code)
    if debug:
        print(f'tmp_fp-->{tmp_fp} === tmp_file_name-->{tmp_file_name}')

    # 创建子进程执行代码
    cmd = ['python', '-sB', tmp_file_name]
    process = subprocess.Popen(
        args=cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True
    )

    # 评测词云，打分
    score = 0
    while True:
        try:
            line_data: bytes = process.stdout.readline()
            if not line_data:
                break
            if b'e485c73f5dd07c29' in line_data:
                review_data: str = line_data.decode('u8')
                review_data: Dict = json.loads(review_data)
                if debug:
                    print(f'debug:review_data-->{review_data}')
                for key, value in answer.items():
                    # 字符串或数值，则比较值是否相等
                    if isinstance(value, (str, int)):
                        tmp_score = scores.get(key) if value == review_data.get(key, None) else 0
                    elif isinstance(value, List):
                        tmp_score = scores.get(key) if set(value) == set(review_data.get(key, None)) else 0
                    elif isinstance(value, Dict):
                        tmp_score = scores.get(key) if value == review_data.get(key, None) else 0
                    else:
                        tmp_score = 0
                    score += tmp_score
            else:
                if debug:
                    print(f'debug:line_data-->{line_data.decode("u8")}')  # 打印其他数据
        except TimeoutError:
            lines_data: bytes = process.stdout.read(1024)
            if debug:
                print(f'debug:lines_data-->{lines_data.decode("u8")}')  # 数据不是多行，不走这里

    # 还原环境，删除临时文件
    os.remove(tmp_file_name)

    # 返回结果
    result = {
        'status': 200,
        'score': score,
    }

    # 程序异常情况
    out, err = process.communicate()
    if err:
        result['status'] = 400
        result['error'] = err.decode('u8')

    if debug:
        print(f'debug:result-->{result}')
    return result
    pass


if __name__ == "__main__":
    # 测试
    # 测试数据
    data = {
        'code': """
import wordcloud
c = wordcloud.WordCloud()
txt = 'I have a good friend, and her name is Li Hua. We have become friends for about two years. She is very kind. When I step into the classroom for the first time, she helps me to get familiar with the strange environment. The most important thing is that we share the same interest, so we have a lot in common. '
c = c.generate(txt)
img = c.to_image()
print(123)
# img.show()""",
        'answer': {
            'words': {'good': 1, 'friend': 2, 'name': 1, 'Li': 1, 'Hua': 1, 'become': 1, 'two': 1, 'years': 1,
                      'kind': 1,
                      'step': 1, 'classroom': 1, 'first': 1, 'time': 1, 'helps': 1, 'familiar': 1, 'strange': 1,
                      'environment': 1, 'important': 1, 'thing': 1, 'share': 1, 'interest': 1, 'lot': 1, 'common': 1},
            'width': 400,
            'height': 200,
            'min_font_size': 4,
            'max_font_size': 26,
            'font_step': 1,
            'font_path': 'DroidSansMono.ttf',
            'max_words': 200,
            'stopwords': ['what', "i'll", "won't", 'than', 'same', 'at', "they'll", "there's", 'should', 'through',
                          'was',
                          'for', 'else', 'while', "they've", 'own', 'if', 'has', 'most', 'there', 'or', 'the', 'hers',
                          'during', "that's", "they'd", 'as', 'com', "how's", 'him', "what's", 'yourself', 'he',
                          "hadn't",
                          "shouldn't", 'few', 'under', "he'd", 'all', 'myself', 'once', "we're", 'your', 'shall', 'an',
                          'r',
                          "mustn't", "i'd", 'with', 'ours', 'such', 'which', "who's", 'about', 'she', 'whom', 'since',
                          'where', 'yourselves', 'down', 'some', 'below', "we've", 'from', 'its', 'to', 'am', 'just',
                          'above', "you're", "let's", 'me', "she's", 'not', 'too', 'both', 'very', 'any', 'like',
                          'against',
                          'then', 'over', 'ever', 'are', 'who', 'also', 'by', "you'd", 'our', 'nor', 'of', 'between',
                          'out',
                          "wouldn't", 'why', 'does', "doesn't", 'his', 'each', 'would', 'on', 'itself', 'ought',
                          'therefore', 'how', 'more', "hasn't", "he's", 'get', 'is', 'but', 'here', 'further', "we'd",
                          'only', 'http', 'do', 'yours', 'her', "they're", 'until', 'however', 'himself', 'be', 'could',
                          "she'd", 'a', 'it', 'them', "why's", 'www', 'up', 'other', 'themselves', "he'll", 'this',
                          'so',
                          'they', "don't", 'their', 'being', 'into', 'after', "where's", "shan't", 'because', 'have',
                          'my',
                          'again', "couldn't", 'off', 'in', 'we', 'having', "isn't", "i'm", 'ourselves', "it's", 'you',
                          "wasn't", "i've", "you'll", 'were', "when's", 'had', 'cannot', 'i', "haven't", 'those',
                          "aren't",
                          'no', 'hence', 'been', 'k', "here's", "didn't", 'before', "we'll", 'doing', "weren't",
                          'herself',
                          'did', 'can', 'that', 'and', 'theirs', "can't", 'otherwise', "you've", "she'll", 'these',
                          'when'],
            'mask': '6adf97f83acf6453d4a6a4b1070f3754',
            'background_color': 'black'
        },
        'scores': {
            'words': 5,
            'width': 5,
            'height': 10,
            'min_font_size': 10,
            'max_font_size': 10,
            'font_step': 10,
            'font_path': 10,
            'max_words': 10,
            'stopwords': 10,
            'mask': 10,
            'background_color': 10
        },
    }

    # 替换词云源代码
    mock_word_cloud()

    # 测试结果
    _result = review_word_cloud(code=data.get('code'), answer=data.get('answer'), scores=data.get('scores'), debug=True)
    print(_result)
