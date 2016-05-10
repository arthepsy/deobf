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
import sys

OBF_PREFIX = 'OBF:'

def jetty_obfuscate(s):
	o = OBF_PREFIX
	if isinstance(s, bytes):
		s = s.decode('utf-8')
	b = bytearray(s, 'utf-8')
	l = len(b)
	for i in range(0, l):
		b1, b2 = b[i], b[l - (i + 1)]
		if b1 < 0 or b2 < 0:
			i0 = (0xff & b1) * 256 + (0xff & b2)
			o += 'U0000'[0:5 - len(x)] + x
		else:
			i1, i2 = 127 + b1 + b2, 127 + b1 - b2
			i0 = i1 * 256 + i2
			x = _to36(i0)
			j0 = int(x, 36)
			j1, j2 = i0 / 256, i0 % 256
			o += '000'[0:4 - len(x)] + x
	return o

def jetty_deobfuscate(s):
	if s.startswith(OBF_PREFIX):
		s = s[len(OBF_PREFIX):]
	l = len(s)
	b = bytearray([0] * int(l / 2))
	p = 0
	for i in range(0, l, 4):
		i0 = int(s[i:i+4], 36)
		if s[i] == 'U':
			b[p] = i0 >> 8
		else:
			i1, i2 = i0 / 256, i0 % 256
			b[p] = int((i1 + i2 - 254) / 2)
		p = p + 1
	return b.decode('utf8')

def _to36(value):
	if value == 0:
		return '0'
	if value < 0:
		sign = '-'
		value = -value
	else:
		sign = ''
	result = []
	while value:
		value, mod = divmod(value, 36)
		result.append('0123456789abcdefghijklmnopqrstuvwxyz'[mod])
	return sign + ''.join(reversed(result))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		s = sys.argv[1]
		if s.startswith(OBF_PREFIX):
			print(jetty_deobfuscate(s))
		else:
			print(jetty_obfuscate(s))
	else:
		print('Usage:\n  {0} [OBF:]password'.format(sys.argv[0]))
