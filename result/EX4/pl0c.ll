@n = common global i32 0, align 4
@x = common global i32 0, align 4
@i = common global i32 0, align 4
define void @prime(){
 %1 = alloca i32, align 4
 %2 = alloca i32, align 4
 %3 = load i32, i32* @x, align 4
 store i32 2, i32* %3, align 4
 %4 = load i32, i32* @x, align 4
 %5 = load i32, i32* @x, align 4
 %6 = load i32, i32* %2, align 4
 %7 = load i32, i32* %2, align 4
 %8 = mul nsw i32 %6, %7
 %9 = load i32, i32* %2, align 4
 %10 = sub nsw i32 %9, 1
 store i32 %10, i32* %2, align 4
 %11 = load i32, i32* %2, align 4
 %12 = load i32, i32* @x, align 4
}
define i32 @main(){
 %1 = alloca i32, align 4
 %2 = load i32, i32* @n, align 4
 %3 = load i32, i32* @i, align 4
 store i32 %3, i32* @x, align 4
}
