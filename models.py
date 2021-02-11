
from enum import Enum

class Scope(Enum):
    LOCAL = 0
    GLOBAL = 1
    FUNC = 2
    CONSTANT = 3

class CmpType(Enum):
    EQ = 0  # eq (==)
    NE = 1  # ne (!=)
    SGT = 2  # sgt (>，符号付き)
    SGE = 3  # sge (>=，符号付き)
    SLT = 4  # slt (<，符号付き)
    SLE = 5  # sle (<=，符号付き)

    # def get_str(ctype):
    #     tab = {EQ: "eq", NE: "ne", SGT: "sgt", SGE: "sge", SLT: "slt", SLE: "sle"}
    #     return tab[ctype]
    def __str__(self):
        if self == CmpType.EQ:
            return "eq"
        if self == CmpType.NE:
            return "ne"
        if self == CmpType.SGT:
            return "sgt"
        if self == CmpType.SGE:
            return "sge"
        if self == CmpType.SLT:
            return "slt"
        if self == CmpType.SLE:
            return "sle"

class SymbolTable(object):
    def __init__(self):
        self.symbols = []

    def insert(self, token: str, flg, reg=None):
        print("----insert----")  #ここから
        #受け取ったトークンとその属性を追加
        self.symbols.append([token, Scope(flg).name, reg])
        for data in self.symbols:
            print("{} {}\n".format(str(data[0]), data[1], str(data[2])))


    def lookup(self, token: str):
        print("----lookup----")#ここから
        for data in reversed(self.symbols):
            # トークンの検索
            if str(data[0]) == token :
                print("{} {} {}\n".format(str(data[0]), data[1], str(data[2])))
                return data

    def delete(self):
        print("----delete----")
        for data in self.symbols:
            #局所変数なら削除
            if data[1] == "LOCAL":
                self.symbols.remove(data)
            #それ以外なら出力
            else:
                print("{} {}\n".format(str(data[0]), data[1]))

class Fundecl(object):
    def __init__(self, name):
        self.name = name
        self.codes = []
        self.cntr = 1
        self.rettype = "void"

    def get_register(self):
        t = self.cntr
        self.cntr += 1
        return t

    def print(self, fp):
        if self.name != "":
            print("define {} @{}(){{".format(self.rettype, self.name), file=fp)
            for l in self.codes:
                print(" {}".format(l), file=fp)
            print("}", file=fp)
        else:
            for l in self.codes:
                print(str(l), file=fp)

class Factor(object):
    def __init__(self, vtype, vname=None, val=None):
        self.type = vtype
        self.name = vname
        self.val = val

    def __str__(self):
        if self.type == Scope.GLOBAL:
            return "@{}".format(self.name)
        elif self.type == Scope.LOCAL:
            return "%{}".format(self.val)
        elif self.type == Scope.CONSTANT:
            return str(self.val)
        elif self.type == Scope.FUNC:
            return "@{}".format(self.name)
class LLVMCode(object):
    def __init__(self):
        pass

class LLVMCodeGlobal(LLVMCode):
    def __init__(self, retval):
        super().__init__()
        self.retval = retval

    def __str__(self):
        return str(self.retval) + " = common global i32 0, align 4"

class LLVMCodeAlloca(LLVMCode):
    def __init__(self, retval):
        super().__init__()
        self.retval = retval

    def __str__(self):
        return str(self.retval) + " = alloca i32, align 4"

class LLVMCodeStore(LLVMCode):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return "store i32 {}, i32* {}, align 4".format(str(self.arg1), str(self.arg2))

class LLVMCODELoad(LLVMCode):
    def __init__(self, arg1, retval):
        super().__init__()
        self.arg1 = arg1
        self.retval = retval

    def __str__(self):
        return "{} = load i32, i32* {}, align 4".format(str(self.retval), str(self.arg1))

class LLVMCodeBrCond(LLVMCode):
    def __init__(self, arg1, arg2, arg3):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
    def __str__(self):
        return "br il {},label {}, label {}".format(str(self.arg1), str(self.arg2), str(self.arg3))

class LLVMCodeBrUncond(LLVMCode):
    def __init__(self, arg1):
        super().__init__()
        self.arg1 = arg1

    def __str__(self):
        return "br label {}".format(str(self.arg1))

class LLVMCODELabel(LLVMCode):
    def __init__(self, arg1):
        super().__init__()
        self.arg1 = arg1
    def __str__(self):
        return "{}:".format(str(self.arg1))

class LLVMCodeAdd(LLVMCode):
    def __init__(self, arg1, arg2, retval):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.retval = retval

    def __str__(self):
        return "{} = add nsw i32 {}, {}".format(str(self.retval), str(self.arg1), str(self.arg2))

class LLVMCodeSub(LLVMCode):
    def __init__(self, arg1, arg2, retval):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.retval = retval

    def __str__(self):
        return "{} = sub nsw i32 {}, {}".format(str(self.retval), str(self.arg1), str(self.arg2))

class LLVMCodeMul(LLVMCode):
    def __init__(self, arg1, arg2, retval):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.retval = retval

    def __str__(self):
        return "{} = mul nsw i32 {}, {}".format(str(self.retval), str(self.arg1), str(self.arg2))

class LLVMCodeDiv(LLVMCode):
    def __init__(self, arg1, arg2, retval):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.retval = retval

    def __str__(self):
        return "{} = div nsw i32 {}, {}".format(str(self.retval), str(self.arg1), str(self.arg2))

class LLVMCodeIcmp(LLVMCode):
    def __init__(self, cmptype, arg1, arg2, retval):
        super().__init__()
        self.cmptype = cmptype
        self.arg1 = arg1
        self.arg2 = arg2
        self.retval = retval

    def __str__(self):
        return "{} = icmp {} i32 {}, {}".format(
            str(self.retval), self.cmptype, str(self.arg1), str(self.arg2),
        )

class LLVMCodeWriteFormat(LLVMCode):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return '@.str.write = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1'

class LLVMCodeReadFormat(LLVMCode):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return '@.str.read = private unnamed_addr constant [3 x i8] c"%d\\00", align 1'

class LLVMCodeWrite(LLVMCode):
    def __init__(self, arg, retval):
        super().__init__()
        self.arg = arg
        self.retval = retval

    def __str__(self):
        return f'{self.retval} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.write, i64 0, i64 0), i32 {self.arg})'

class LLVMCodeRead(LLVMCode):
    def __init__(self, arg, retval):
        super().__init__()
        self.arg = arg
        self.retval = retval

    def __str__(self):
        return f'{self.retval} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.read, i64 0, i64 0), i32* {self.arg})'

class LLVMCodeDeclarePrintf(LLVMCode):
    def __str__(self):
        return 'declare dso_local i32 @printf(i8*, ...) #1'

class LLVMCodeDeclareScanf(LLVMCode):
    def __str__(self):
        return 'declare dso_local i32 @__isoc99_scanf(i8*, ...) #1'

class LLVMCodeCallProc(LLVMCode):
    def __init__(self, arg, retval):
        super().__init__()
        self.arg = arg
        self.retval = retval

    def __str__(self):
        return f'{self.retval} = call i32 {self.arg}'