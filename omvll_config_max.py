#
# O-MVLL 混淆配置
# 开启所有稳定的混淆保护
#

import omvll
from functools import lru_cache

class MaxObfuscationConfig(omvll.ObfuscationConfig):
    """
    最高规格混淆配置类
    
    开启的混淆保护：
    - 控制流平坦化 (CFG Flattening) ✓
    - 控制流断裂 (Break CFG) ✓
    - 算术运算混淆 (Arithmetic) ✓
    - 不透明常量 (Opaque Constants) ✓
    - 不透明字段访问 (Opaque Field Access) ✓
    - 字符串编码 (String Encoding) ✓
    - 基本块复制 (Basic Block Duplicate) ✓
    - 函数外联 (Function Outline) ✓
    - 反 Hook 保护 (Anti-Hook) ✓
    """
    
    def __init__(self):
        super().__init__()
    
    # ========== 控制流平坦化 ==========
    def flatten_cfg(self, mod: omvll.Module, func: omvll.Function):
        """控制流平坦化 - 将控制流图展平为switch结构"""
        return omvll.ControlFlowFlatteningOpt(True)
    
    # ========== 控制流断裂 ==========
    def break_cfg(self, mod: omvll.Module, func: omvll.Function):
        """控制流断裂 - 打断基本块之间的直接连接"""
        return omvll.BreakControlFlowOpt(True)
    
    # ========== 算术运算混淆 ==========
    def obfuscate_arithmetics(self, mod: omvll.Module, func: omvll.Function):
        """算术运算混淆 - 替换为等价复杂表达式 (5轮)"""
        return omvll.ArithmeticOpt(5)
    
    # ========== 不透明常量 ==========
    def obfuscate_constants(self, mod: omvll.Module, func: omvll.Function):
        """不透明常量混淆 - 用复杂表达式替换常量"""
        return omvll.OpaqueConstantsBool(True)
    
    # ========== 不透明字段访问 ==========
    def obfuscate_struct_access(self, mod: omvll.Module, func: omvll.Function, struct):
        """结构体字段访问混淆"""
        return omvll.StructAccessOpt(True)
    
    def obfuscate_variable_access(self, mod: omvll.Module, func: omvll.Function, var):
        """全局变量访问混淆"""
        return omvll.VarAccessOpt(True)
    
    # ========== 字符串编码 ==========
    def obfuscate_string(self, mod: omvll.Module, func: omvll.Function, string: bytes):
        """字符串编码混淆 - 加密并在运行时解密"""
        return omvll.StringEncOptLocal()
    
    # ========== 基本块复制 ==========
    def basic_block_duplicate(self, mod: omvll.Module, func: omvll.Function):
        """基本块复制 - 增加分析复杂度 (100%概率)"""
        return omvll.BasicBlockDuplicateWithProbability(100)
    
    # ========== 函数外联 ==========
    def function_outline(self, mod: omvll.Module, func: omvll.Function):
        """函数外联混淆 - 提取为独立外联函数 (100%概率)"""
        return omvll.FunctionOutlineWithProbability(100)
    
    # ========== 反 Hook 保护 ==========
    def anti_hooking(self, mod: omvll.Module, func: omvll.Function):
        """反 Hook 保护 - 检测并对抗 Hook 框架"""
        return omvll.AntiHookOpt(True)


# 导出配置对象
@lru_cache(maxsize=1)
def omvll_get_config() -> omvll.ObfuscationConfig:
    return MaxObfuscationConfig()