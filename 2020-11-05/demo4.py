import os
import re
import subprocess
import sys
from tempfile import mkdtemp, mkstemp
from wordcloud import WordCloud
import base64
import json
import time


class OJ:
    def __init__(self, answer: dict, data: bytes, match: float = 1.0, debug: str = "False"):
        self.data = data
        self.match = match
        self.answer = answer
        self.debug = debug
        self.res = {"msg": "", "code": 1, "data": {}}

    def deal_code(self):
        try:
            # self.code = eval(self.data)["code"]
            code = base64.b64decode(self.data)
            code = base64.b64decode(code)
            self.data = str(code, encoding="utf-8") + "\n"
            if self.debug == "True":
                print("取出传入的值", self.data)
        except Exception as e:
            self.res.update(code=-1, msg=e)
            return json.dumps(self.res)

    def _word_cloud(self, code):
        tmp = code.decode('u8')
        # 获取词云文本内容text
        text = re.search("72F9882144A13C12(.*)72F9882144A13C12", tmp, re.S).group(1)
        # 获取词云词频freq
        freq = WordCloud().generate(text).words_
        tmp_word_count = 1
        for k, v in freq.items():
            if v in [1, 1.0]:
                tmp_word = k
                tmp_word_count = text.count(tmp_word)
        for k, v in freq.items():
            freq[k] = round(v * tmp_word_count)
        # 剔除词云标记
        # data1 = tmp.strip("\n").strip('72F9882144A13C12')
        data = tmp.replace('72F9882144A13C12' + text + '72F9882144A13C12\n', '')
        return data, freq

    def evaluating(self):
        self.deal_code()
        if self.debug == "True":
            print("进入运行阶段代码为{}".format(self.data))
        # pattern = 'WordCloud\([\s\w=]*\)\.generate\((.*)\)'
        pattern = 'WordCloud\([\s\w=]*\)\.generate\((.*)\)'
        tmp = re.search(pattern, self.data)
        if self.debug == "True":
            print("tem的值为:{}".format(tmp))
        code_mask = ""
        if tmp:
            tmp_obj = tmp.group(1)
            tmp_print = "\nprint(\"72F9882144A13C12\" + {} + \"72F9882144A13C12\")".format(tmp_obj)
            code_mask = self.data + tmp_print
        else:
            tmp_dir = mkdtemp(dir="/tmp")
            tmp_fp, tmp_file_name = mkstemp(suffix=".py", text=True, dir=tmp_dir)
            with open(tmp_file_name, "w+", encoding="u8") as f:
                f.write(self.data)
            cmd = ["python3", "-IB", tmp_file_name]
            cmd = " ".join(cmd)
            # print(cmd)
            res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            sout, serr = res.communicate(None)
            res.terminate()
            if self.debug == "True":
                print("sout 值为：{}".format(sout))
            sout1 = sout.decode(encoding="utf-8")
            if "Error" in sout1:
                if self.debug == "True":
                    print("用户看到的鸭子：{}".format(sout1))
                self.res.update(code=-1, msg=sout1)
                return json.dumps(self.res)
        if self.debug == "True":
            print("split前的代码为：{}".format(code_mask))
        lines = code_mask.split("\n")
        if self.debug == "True":
            print("split后的代码为：{}".format(lines))
        text = ""
        for line in lines:
            if ".show()" in line:
                lines.remove(line)
            else:
                text += line + "\n"
        if self.debug == "True":
            print("提出展示代码{}".format(text))
        tmp_dir = mkdtemp(dir="/tmp")
        tmp_fp, tmp_file_name = mkstemp(suffix=".py", text=True, dir=tmp_dir)
        with open(tmp_file_name, "w+", encoding="u8") as f:
            f.write(text)
        cmd = ["python", "-IB", tmp_file_name]
        cmd = " ".join(cmd)
        # print(cmd)
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = res.communicate(None)
        res.terminate()
        if self.debug == "True":
            print("sout值为：{}".format(sout))
        sout1 = sout.decode(encoding="utf-8")
        if "Error" in sout1:
            if self.debug == "True":
                print("用户看到的鸭子：{}".format(sout1))
            self.res.update(code=-1, msg=sout1)
            return json.dumps(self.res)

        if b'72F9882144A13C12' in sout:
            freq = {}
            (sout, freq) = self._word_cloud(sout)
            dict2 = freq
            differ = set(self.answer.items()) - set(dict2.items())
            marks = (len(self.answer) - len(differ)) / len(self.answer)
            if self.debug == "True":
                print("用户词频为 {}".format(dict2))
                print("answer为：{}".format(self.answer))
                print("词云差异为{}".format(differ))
                print("当前检测代码的运行结果符合度为：{}".format(marks))
            if marks >= self.match:
                self.res.update(code=1, msg="True")
                return json.dumps(self.res)
            else:
                self.res.update(code=0, msg="False")
                return json.dumps(self.res)

    def check_code(self):
        pass


if __name__ == '__main__':
    answer = {'friend': 2, 'good': 1, 'name': 1, 'Li': 1, 'Hua': 1, 'become': 1, 'two': 1, 'years': 1, 'kind': 1, 'step': 1, 'classroom': 1, 'first': 1, 'time': 1, 'helps': 1, 'familiar': 1, 'strange': 1, 'environment': 1, 'important': 1, 'thing': 1, 'share': 1, 'interest': 1, 'lot': 1, 'common': 1}

    data = """import wordcloud
c = wordcloud.WordCloud()
txt = 'I have a good friend, and her name is Li Hua. We have become friends for about two years. She is very kind. When I step into the classroom for the first time, she helps me to get familiar with the strange environment. The most important thing is that we share the same interest, so we have a lot in common. '
c = wordcloud.WordCloud().generate(txt)
img = c.to_image()
# img.show()""".encode('u8')
    data = base64.b64encode(data)
    data = base64.b64encode(data)
    o0 = OJ(answer, data, debug="True")
    dd = o0.evaluating()
    print(dd)
