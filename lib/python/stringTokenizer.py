#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python string tokenizer

def tokenize_text(text):
	import MeCab
	
	tokenizer = MeCab.Tagger('-Owakati')

	line = tokenizer.parse(text)
	
	return line

if __name__ == '__main__':

	text = '内視鏡 内視鏡下手術 高速らせんCT（ヘリカルスキャンCT） NMR-CT（MRI） 骨塩量測定装置 超音波診断装置 3Dエコー X線テレビ装置 ホルター心電計 呼吸機能検査 眼底カメラ 人工呼吸器 除細動器'
	tokenize_text(text)
