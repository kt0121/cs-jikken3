@n = common global i32 0, align 4
@sum = common global i32 0, align 4
define i32 @main(){
 %1 = alloca i32, align 4
 store i32 10, i32* @n, align 4
 store i32 0, i32* @sum, align 4
 br label %while.init.1
 while.init.1:
 %2 = load i32, i32* @n, align 4
 %3 = icmp sgt i32 %2, 0
 br i1 %3,label %while.do.1, label %while.end.1
 while.do.1:
 %4 = load i32, i32* @sum, align 4
 %5 = load i32, i32* @n, align 4
 %6 = add nsw i32 %4, %5
 store i32 %6, i32* @sum, align 4
 %7 = load i32, i32* @n, align 4
 %8 = sub nsw i32 %7, 1
 store i32 %8, i32* @n, align 4
 br label %while.init.1
 while.end.1:
}
