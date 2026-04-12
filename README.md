# Termux-clang-21.1.8的OLLVM混淆插件为libOMVLL.so

使用Termux的clang编译出了libOMVLL.so混淆插件

源码https://github.com/open-obfuscator/o-mvll.git 

开发者不放心的话，自行编译,小白自行选择

此版本适配Termux里的clang-21.1.8版本，应该是适配所有21版本的clang不要搭配错了，不然无法使用

…………………………………………………………………………………………………………………………………


先保存到Termux的home目录去，然后

ls -la ollvm混淆编译器.sh libOMVLL.so

chmod +x ollvm混淆编译器.sh libOMVLL.so

还有个omvll_config_max.py是混淆配置也就是python脚本，你看看可以改一改


使用方法:
./ollvm混淆编译器.sh [选项] <源文件> -o <输出>

编译选项:
    -c, -S, -o, -I, -L, -l, -D, -U, --target, -O, -g, -fPIC, -shared

混淆选项:
    --omvll-config <file>   自定义配置
    --no-omvll              禁用混淆
    --omvll-debug           调试输出

目标平台:
    aarch64-linux-android   Android ARM64
    armv7a-linux-androideabi Android ARM32
    x86_64-linux-android    Android x86_64

示例:
    ./ollvm混淆编译器.sh test.c -o test
    ./ollvm混淆编译器.sh -shared -fPIC lib.c -o libtest.so


…………………………………………………………………………………………………………………………………


我会把libOMVLL.so和ollvm混淆编译器.sh放一起，ollvm混淆编译器.sh里面是包含了libOMVLL.so和python脚本的。

使用环境需要有python和clang。

安装方式: pkg install python clang -y


最后使用ollvm混淆编译器.sh编译你想要的文件，混淆规格很高，还有如果混淆之后二进制文件运行失败，最可能的原因就是你的源码有问题，交给AI帮你改改就行了

…………………………………………………………………………………………………………………………………


如果觉得这个项目可以的话，可以点点⭐⭐吗？谢谢啦