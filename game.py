import time

print(
    '-----------\u6B22\u8FCE\u6765\u5230\u5730\u4E0B\u57CE\uFF0C\u9001\u6B7B\u7684\u51E1\u4EBA--------------')
print('''
     ,            _..._            ,
    {'.         .'     '.         .'}
    { ~ '.      _|=    __|_      .'  ~}
  { ~  ~ '-._ (___________) _.-'~  ~  }
 {~  ~  ~   ~.'           '. ~    ~    }
{  ~   ~  ~ /   /\     /\   \   ~    ~  }
{   ~   ~  /    __     __    \ ~   ~    }
 {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~}
  { ~   ;(      \/ .-. \/      );   ~ }
   { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  }
    '-._~ \   (`-._'-'_.-')   / ~_.-'
        '--\   `'._'+'_.'`   /--'
            \     \`-'/     /
             `\    '-'    /'
               `\       /'
                 '-...-' 
''')

hp = 0
att = 0
defend = 0
monsterLevel = 0

#input() \u8F93\u5165\u51FD\u6570
job = input('''\u8BF7\u9009\u62E9\u4F60\u7684\u804C\u4E1A\uFF08\u8F93\u5165a\u6216b\uFF09
            A:\u6218\u58EB
            B\uFF1A\u6CD5\u5E08
            ''')
while (job != "a" and job != "A" and job != "b" and job != "B"):
    print("\u8F93\u5165\u9519\u8BEF\uFF0C\u8BF7\u8F93\u5165 a \u6216\u8005 b ")
    job = input('''\u8BF7\u9009\u62E9\u4F60\u7684\u804C\u4E1A\uFF08\u8F93\u5165a\u6216b\uFF09
            A:\u6218\u58EB
            B\uFF1A\u6CD5\u5E08
            ''')

level = int(input('\u8BF7\u8F93\u5165\u4F60\u7684\u7B49\u7EA7\uFF1A'))
monsterLevel = int(input('\u8BF7\u8F93\u5165\u602A\u7269\u7684\u7B49\u7EA7\uFF1A'))

if job == "a" or job == "A":
    hp = 800 + level * 59
    att = 100 + level * 10
    defend = 20 + level * 5

if job == "b" or job == "B":
    hp = 500 + level * 35
    att = 120 + level * 19
    defend = 15 + level * 3

print('\u4F60\u7684\u7B49\u7EA7\u662F{}\uFF0C\u653B\u51FB\u529B\u662F{}\uFF0C\u8840\u91CF{}\uFF0C\u9632\u5FA1\u529B{}'.format(level, att, hp, defend))
print("------\u6218\u6597\u5F00\u59CB---------")
bosshp = 10000 + monsterLevel * 30
bossatt = 50 + monsterLevel * 8
bossdef = 50

while bosshp >= 0 and hp >= 0:
    hp = hp - bossatt
    print("\u602A\u7269\u653B\u51FB\u4E86\u4F60\uFF0CHP - {}\uFF0C\u5269\u4F59HP\uFF1A{}".format(bossatt, hp))
    bosshp = bosshp - att;
    print("\u4F60\u653B\u51FB\u4E86Boss\uFF0C\u780D\u6389\u4E86{} \u70B9\u8840\uFF0C\u5269\u4F59HP\uFF1A{}".format(att,
                                                                                                                    bosshp))
    print("----------------------------------------")

    time.sleep(0.5)

    if hp <= 0:
        print("\u6218\u8D25\uFF0C\u5927\u4FA0\u8BF7\u4ECE\u5934\u6765\u8FC7\uFF01\uFF01\uFF01")
        str = 'Hello'
        print(str[-1])
    if bosshp <= 0:
        print("\u606D\u559C\u4F60\u6218\u80DC\u4E86Boss\uFF0C\u7206\u5230\u5C60\u9F99\u5200\u4E00\u628A")
        print('''
           ,
          / \\
         {   }
         !   !
         ; : ;
         | : |
         | : |
         l ; l
         l ; l
         I ; I
         I ; I
         I ; I
         I ; I
         d | b 
         H | H
         H | H
         H I H
 ,;,     H I H     ,;,
;H@H;    ;_H_;,   ;H@H;
`\Y/d_,;|4H@HK|;,_b\Y/'
 '\;MMMMM$@@@$MMMMM;/'
   ~~~*; !8@8!; *~~~
         ;888;
         ;888;
         ;888;
         ;888;
         d8@8b
         O8@8O
         T808T
          `~` 
''')
