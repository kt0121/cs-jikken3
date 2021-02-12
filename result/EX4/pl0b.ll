@n = common global i32 0, align 4
@x = common global i32 0, align 4
define i32 @prime(){
 %1 = alloca i32, align 4
 %2 = alloca i32, align 4
 %3 = load i32, i32* @x, align 4
 %4 = sdiv i32 %3, 2
 store i32 %4, i32* %2, align 4
 %5 = load i32, i32* @x, align 4
 %6 = load i32, i32* @x, align 4
 %7 = load i32, i32* %2, align 4
 %8 = sdiv i32 %6, %7
 %9 = load i32, i32* %2, align 4
 %10 = mul nsw i32 %8, %9
 %11 = load i32, i32* %2, align 4
 %12 = sub nsw i32 %11, 1
 store i32 %12, i32* %2, align 4
 %13 = load i32, i32* %2, align 4
 %14 = load i32, i32* @x, align 4
ret i32 0
}
define i32 @main(){
 %1 = alloca i32, align 4
 %2 = load i32, i32* @n, align 4
 %3 = load i32, i32* @n, align 4
 store i32 %3, i32* @x, align 4
 %4 = load i32, i32* @n, align 4
 %5 = sub nsw i32 %4, 1
 store i32 %5, i32* @n, align 4
ret i32 0
}
