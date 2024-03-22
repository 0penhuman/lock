此项目献给我最爱的区女士
# 该程序可用于文本加解密，加密方法是在凯撒密码的基础上通过选取无限不循环小数的某位上的值为位移量，使得安全性高于一般的凯撒密码，而效率优于非对称加密，加密后的内容会保存在程序所在的文件夹中，名称为coding.code
#### 在python3.10及以上环境运行lock.py效果会更好
## 在运行时，会有-->引导的命令行输入，你可以在后面输入命令，目前程序支持的命令有\exit,encode,decode三个，分别可使程序退出运行状态，进入加密状态和进入解密状态
## 输入encode，你会看到key-->，此时，你需要输入密钥，你应该提前与你希望可以解密的人沟通好密钥内容，密钥可以是数字或者字符串，支持几乎所有类型任意长度的文本内容，包括emoji表情
## 输入完密钥后按下回车，程序会进入加密状态，你会看到encode-->，你可以输入你希望加密的文本，但目前不支持加密段落，即文本中不能有回车
## 加密成功后程序会打印done，并且在程序所在的文件夹内生成coding.code文件，内容是6位16进制数为一组的密文，这样的原因是我本打算将加密后的文件变为RGB图片格式，但碍于技术不佳，没能实现
## 你可以把coding.code文件发给别人，这能帮助你躲避网络审查
## 他人收到coding.code文件后如果不知道密钥，是无法读取明文信息的，由于加密基于计算平方根，位移位数具有随机性，可以有效避免统计密文出现频率反推明文的情况，不过在极少数情况下可能会出现被开方数恰好是个完全平方数的情况，但概率极小，不必担心
## 如果他人得知密钥，他可以将coding.code文件置于程序所在的文件夹中，并运行程序，输入decode，进入解密状态
## 进入解密状态后程序会要求其输入密钥，然后要求其输入加密文档所在的位置，在上述情况下，直接输入coding.code便可，程序会在解密后将明文打印出来
<img width="366" alt="截屏2024-03-22 下午10 02 41" src="https://github.com/0penhuman/lock/assets/159608807/3c22a4f6-e94d-488b-97d3-04bfd6e720b9">
