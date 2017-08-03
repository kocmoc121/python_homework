# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
print('--------------------------1------------------')
#вывожу только по 1 символу слева и справа от верхних регистров
new_line = ''
i =0
while (i < len(line)):
       if line[i].isupper() and i!=0 and i!=len(line):
              new_line = new_line + line[i-1]
              while (line[i].isupper()):
                     i+=1
              new_line = new_line + line[i] + ' '
       i+=1

print (new_line)





# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
print('--------------------------2------------------')
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrXGC'

line_3 = ''
for char in range(len(line_2)):
       if char<2 or char>(len(line_2)-3):
              continue
       elif str(line_2[char]).isupper() and str(line_2[char-1]).islower() and str(line_2[char+1]).isupper() and str(line_2[char-2]).islower() and str(line_2[char+2]).isupper():
              line_3 = line_3 + str(line_2[char])
print(line_3)

# Задача-3:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле
print('--------------------------3------------------')
import random
f = open('test.txt', 'w')

for i in range(2500):
       i = random.randint(0,9)
       f.write(str(i))
f.close()
tmp_str = ''
length = 1
max_len = 1
tmp = 0
f = open('test.txt', 'r')
tmp_str = f.read()
f.close()
for i in range(len(tmp_str)):
       if i == 0:
              continue 
       if tmp_str[i] == tmp_str[i-1]:
              length+=1
       else:
              length = 1
       if max_len < length:
              max_len = length
              tmp=i
       i+=1

str2 = ''

for i in range(max_len):
      str2 += tmp_str[tmp-max_len+i+1]

print (str2)