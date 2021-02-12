@n = common global i32 0, align 4
@sum = common global i32 0, align 4
define i32 @main(){
 %1 = alloca i32, align 4
 store i32 10, i32* @n, align 4
 store i32 0, i32* @sum, align 4
 %2 = load i32, i32* @n, align 4
 %3 = load i32, i32* @sum, align 4
 %4 = load i32, i32* @n, align 4
 %5 = add nsw i32 %3, %4
 store i32 %5, i32* @sum, align 4
 %6 = load i32, i32* @n, align 4
 %7 = sub nsw i32 %6, 1
 store i32 %7, i32* @n, align 4
 ret i32 0
}
