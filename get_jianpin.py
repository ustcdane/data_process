#!/usr/bin/env python
#coding:gb18030
'''
#=============================================================================
#     FileName: get_jianpin.py
#         Desc: 判断拼音 汉字是否为全拼 
#  		yuefen 月份 -> y f
#       Author: Daniel Wang
#        Email: daneustc@gmail.com
#     HomePage: http://ustcdane.github.io/
#      Version: 0.0.1
#   LastChange: 2017-09-08 10:23:01
#      History:
#=============================================================================
'''

import sys
import os

pys=["a","ai","an","ang","ao","ba","bai","ban","bang","bao","bei","ben","beng","bi","bian","biao","bie","bin","bing","bo","bu","ca","cai","can","cang","cao","ce","cen","ceng","cha","chai","chan","chang","chao","che","chen","cheng","chi","chong","chou","chu","chua","chuai","chuan","chuang","chui","chun","chuo","ci","cong","cou","cu","cuan","cui","cun","cuo","da","dai","dan","dang","dao","de","dei","den","deng","di","dia","dian","diao","die","ding","diu","dong","dou","du","duan","dui","dun","duo","e","ei","en","eng","er","fa","fan","fang","fei","fen","feng","fiao","fo","fou","fu","ga","gai","gan","gang","gao","ge","gei","gen","geng","gong","gou","gu","gua","guai","guan","guang","gui","gun","guo","ha","hai","han","hang","hao","he","hei","hen","heng","hong","hou","hu","hua","huai","huan","huang","hui","hun","huo","ji","jia","jian","jiang","jiao","jie","jin","jing","jiong","jiu","ju","juan","jue","jun","ka","kai","kan","kang","kao","ke","kei","ken","keng","kong","kou","ku","kua","kuai","kuan","kuang","kui","kun","kuo","la","lai","lan","lang","lao","le","lei","leng","li","lia","lian","liang","liao","lie","lin","ling","liu","lo","long","lou","lu","luan","lue","lun","luo","lv","ma","mai","man","mang","mao","me","mei","men","meng","mi","mian","miao","mie","min","ming","miu","mo","mou","mu","na","nai","nan","nang","nao","ne","nei","nen","neng","ni","nian","niang","niao","nie","nin","ning","niu","nong","nou","nu","nuan","nue","nun","nuo","nv","o","ou","pa","pai","pan","pang","pao","pei","pen","peng","pi","pian","piao","pie","pin","ping","po","pou","pu","qi","qia","qian","qiang","qiao","qie","qin","qing","qiong","qiu","qu","quan","que","qun","ran","rang","rao","re","ren","reng","ri","rong","rou","ru","rua","ruan","rui","run","ruo","sa","sai","san","sang","sao","se","sen","seng","sha","shai","shan","shang","shao","she","shei","shen","sheng","shi","shou","shu","shua","shuai","shuan","shuang","shui","shun","shuo","si","song","sou","su","suan","sui","sun","suo","ta","tai","tan","tang","tao","te","tei","teng","ti","tian","tiao","tie","ting","tong","tou","tu","tuan","tui","tun","tuo","wa","wai","wan","wang","wei","wen","weng","wo","wu","xi","xia","xian","xiang","xiao","xie","xin","xing","xiong","xiu","xu","xuan","xue","xun","ya","yan","yang","yao","ye","yi","yin","ying","yo","yong","you","yu","yuan","yue","yun","za","zai","zan","zang","zao","ze","zei","zen","zeng","zha","zhai","zhan","zhang","zhao","zhe","zhei","zhen","zheng","zhi","zhong","zhou","zhu","zhua","zhuai","zhuan","zhuang","zhui","zhun","zhuo","zi","zong","zou","zu","zuan","zui","zun","zuo"]

#give py hz then output jianpin in out list
#if py not quanpin it will return true, otherwise return false
def quanPin(py, hz,out): #hz is gb18030 encode
	len_hz = len(hz)
	len_py = len(py)
	if not py or not hz:
		return False
	#print len_hz
	if len_hz == 1:
		if py in pys:
			print py
			out.append(py[0])
			return True
		else:
			return False
	if len_hz == 2:
		#print hz, len_hz
		for i in range(len_py-1,0,-1):
			if py[:i] in pys and py[i:] in pys:
				out.append(py[i:][0])
				out.append(py[:i][0])
				return True
		return False
	if len_hz > 2:#递归处理
		for i in range(len_py-1, 0, -1):
			if quanPin(py[i:], hz[-1:], out) and quanPin(py[:i], hz[:-1], out):
				return True
	return False

#yuefenaniquxian 月份啊你去西安
#yfanqxa
for line in sys.stdin:
	line = line.strip()
	#print line
	line = line.decode('gb18030')
	segs = line.split(' ')
	print segs[0], segs[1]
	out = []
	hz_len = len(segs[1])
	print hz_len
	if(quanPin(segs[0], segs[1],out)):
		print ''.join(out[::-1])[:hz_len]
	else:
		print  >> sys.stderr,"Error %s not quanpin!!" % line
