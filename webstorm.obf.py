#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   The MIT License (MIT)
   
   Copyright (C) 2016 Andris Raugulis (moo@arthepsy.eu)
   
   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:
   
   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.
   
   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.
"""
import sys, itertools, base64

WEBSTORM_KEY = b'\xdf\xaa'
WEBSTORM_ENC = 'utf-16-be'

def uord(v):
	return ord(v) if sys.version_info[0] == 2 else v

def str2hex(s):
	return base64.b16encode(s).lower()

def hex2str(s):
	return base64.b16decode(s.upper())

def xor_str(s, k):
	return bytearray(uord(a) ^ uord(b) for a, b in zip(s, itertools.cycle(k)))

def decrypt(s):
	x = xor_str(hex2str(s), WEBSTORM_KEY)
	x = x.decode(WEBSTORM_ENC)
	return x

def encrypt(s):
	x = xor_str(s.encode(WEBSTORM_ENC), WEBSTORM_KEY)
	x = str2hex(x).decode('ascii')
	return x

if __name__ == '__main__':
	if len(sys.argv) > 2 and sys.argv[1] in ('-e', '-d'):
		if sys.argv[1] == '-e':
			print(encrypt(sys.argv[2]))
		else:
			print(decrypt(sys.argv[2]))
	else:
		prog = sys.argv[0]
		print('Usage:\n  {0} -e <password>\n  {0} -d <password>'.format(prog))
