'''
Basic test.
'''

from source.regex_fa import RegexToDFAConversor

print('3;{1,2,4,5};{{1,2,4,5},{3,5},{2,4,5}};{a,b};{1,2,4,5},a,{3,5};{1,2,4,5},b,{2,4,5};{3,5},b,{2,4,5};{2,4,5},a,{3,5}')
print(RegexToDFAConversor.convert('(&|b)(ab)*(&|a)'))

print('5;{1};{{2,3,8},{3,8}};{a,b};{1},a,{2,3,8};{2,3,8},a,{2,3,8};{2,3,8},b,{4,5};{4,5},a,{6,7};{4,5},b,{4,5};{6,7},a,{6,7};{6,7},b,{3,8};{3,8},b,{4,5}')
print(RegexToDFAConversor.convert('aa*(bb*aa*b)*'))

print('3;{1};{{2,3,4,5}};{a,b};{1},a,{2,3,4};{2,3,4},a,{2,3,4,5};{2,3,4},b,{2,3,4};{2,3,4,5},a,{2,3,4,5};{2,3,4,5},b,{2,3,4}')
print(RegexToDFAConversor.convert('a(a|b)*a'))

print('5;{1,6};{{2,3,11},{7,8,11}};{a,b};{1,6},a,{2,3,11};{1,6},b,{7,8,11};{2,3,11},a,{2,3,11};{2,3,11},b,{4,5};{7,8,11},a,{9,10};{7,8,11},b,{7,8,11};{4,5},a,{2,3,11};{4,5},b,{4,5};{9,10},a,{9,10};{9,10},b,{7,8,11}')
print(RegexToDFAConversor.convert('a(a*(bb*a)*)*|b(b*(aa*b)*)*'))
