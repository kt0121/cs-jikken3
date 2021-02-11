@n = common global i32 0, align 4
@temp = common global i32 0, align 4
define void @fact(){
 %1 = alloca i32, align 4
 %3 = load i32, i32* @n, align 4
 store i32 1, i32* @temp, align 4
 %4 = load i32, i32* @n, align 4
 store i32 %4, i32* %2, align 4
 %5 = load i32, i32* @n, align 4
 %6 = sub nsw i32 %5, 1
 store i32 %6, i32* @n, align 4
 %7 = load i32, i32* @temp, align 4
 %8 = load i32, i32* %2, align 4
 %9 = mul nsw i32 %7, %8
 store i32 %9, i32* @temp, align 4
}
define i32 @main(){
 %1 = alloca i32, align 4
 %2 = load i32, i32* @temp, align 4
}
